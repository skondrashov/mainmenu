"""Data integrity tests for the software catalog.

Validates that all entries in data/*.json conform to the schema
and have consistent, valid values.
"""
import json
import glob
import os
import re
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
SCHEMA_PATH = os.path.join(ROOT, "schema.json")
TAXONOMY_PATH = os.path.join(ROOT, "taxonomy.json")

VALID_OS = {"windows", "macos", "linux", "web", "ios", "android"}
VALID_PRICING = {"free", "freemium", "paid", "subscription"}
VALID_LANGUAGES = {
    "python", "javascript", "typescript", "rust", "go", "c", "cpp", "java",
    "ruby", "php", "swift", "kotlin", "csharp", "dart", "elixir", "r",
    "julia", "lua", "zig", "haskell", "scala", "shell", "perl", "multi",
}
ID_PATTERN = re.compile(r"^[a-z0-9-]+$")


def get_valid_categories():
    with open(TAXONOMY_PATH, encoding="utf-8") as f:
        tax = json.load(f)
    cats = set()
    def walk(node):
        if "categories" in node:
            cats.update(node["categories"])
        for child in node.get("children", []):
            walk(child)
    walk(tax)
    return cats


def load_all_entries():
    entries = []
    for path in sorted(glob.glob(os.path.join(DATA_DIR, "*.json"))):
        with open(path, encoding="utf-8") as f:
            items = json.load(f)
        for item in items:
            item["_source_file"] = os.path.basename(path)
            entries.append(item)
    return entries


VALID_CATEGORIES = get_valid_categories()
ALL_ENTRIES = load_all_entries()


class TestRequiredFields:
    """Every entry must have the required fields."""

    @pytest.fixture(params=["id", "name", "description", "url", "category", "os", "pricing"])
    def required_field(self, request):
        return request.param

    def test_required_fields_present(self, required_field):
        missing = []
        for e in ALL_ENTRIES:
            if required_field not in e or not e[required_field]:
                missing.append(f"{e.get('id', '???')} in {e['_source_file']}")
        assert not missing, f"{len(missing)} entries missing '{required_field}': {missing[:10]}"


class TestFieldValues:
    """Field values must conform to schema constraints."""

    def test_ids_are_kebab_case(self):
        bad = [(e["id"], e["_source_file"]) for e in ALL_ENTRIES
               if "id" in e and not ID_PATTERN.match(e["id"])]
        assert not bad, f"{len(bad)} entries with invalid IDs: {bad[:10]}"

    def test_descriptions_under_200_chars(self):
        long = [(e["id"], len(e["description"]), e["_source_file"])
                for e in ALL_ENTRIES
                if len(e.get("description", "")) > 200]
        assert not long, f"{len(long)} entries with descriptions > 200 chars: {long[:10]}"

    def test_os_values_valid(self):
        bad = []
        for e in ALL_ENTRIES:
            invalid_os = [o for o in e.get("os", []) if o not in VALID_OS]
            if invalid_os:
                bad.append((e["id"], invalid_os))
        assert not bad, f"{len(bad)} entries with invalid OS values: {bad[:10]}"

    def test_pricing_values_valid(self):
        bad = [(e["id"], e["pricing"]) for e in ALL_ENTRIES
               if e.get("pricing") and e["pricing"] not in VALID_PRICING]
        assert not bad, f"{len(bad)} entries with invalid pricing: {bad[:10]}"

    def test_language_values_valid(self):
        bad = [(e["id"], e["language"]) for e in ALL_ENTRIES
               if e.get("language") and e["language"] not in VALID_LANGUAGES]
        assert not bad, f"{len(bad)} entries with invalid language: {bad[:10]}"

    def test_categories_exist_in_taxonomy(self):
        bad = [(e["id"], e["category"]) for e in ALL_ENTRIES
               if e.get("category") and e["category"] not in VALID_CATEGORIES]
        assert not bad, f"{len(bad)} entries with categories not in taxonomy: {bad[:10]}"

    def test_urls_look_valid(self):
        bad = [(e["id"], e["url"]) for e in ALL_ENTRIES
               if e.get("url") and not e["url"].startswith(("http://", "https://"))]
        assert not bad, f"{len(bad)} entries with non-http URLs: {bad[:10]}"

    def test_source_urls_look_valid(self):
        bad = [(e["id"], e["source"]) for e in ALL_ENTRIES
               if e.get("source") and not e["source"].startswith(("http://", "https://"))]
        assert not bad, f"{len(bad)} entries with non-http source URLs: {bad[:10]}"


class TestNoDuplicates:
    """No duplicate IDs across the entire catalog."""

    def test_no_duplicate_ids(self):
        seen = {}
        dupes = []
        for e in ALL_ENTRIES:
            eid = e.get("id", "")
            if eid in seen:
                dupes.append((eid, seen[eid], e["_source_file"]))
            else:
                seen[eid] = e["_source_file"]
        assert not dupes, f"{len(dupes)} duplicate IDs: {dupes[:10]}"


class TestCatalogHealth:
    """Overall catalog health checks."""

    def test_minimum_entry_count(self):
        assert len(ALL_ENTRIES) >= 1000, f"Only {len(ALL_ENTRIES)} entries — expected at least 1000"

    def test_minimum_category_count(self):
        cats = {e["category"] for e in ALL_ENTRIES if e.get("category")}
        assert len(cats) >= 50, f"Only {len(cats)} categories populated — expected at least 50"

    def test_no_empty_data_files(self):
        empty = []
        for path in glob.glob(os.path.join(DATA_DIR, "*.json")):
            with open(path, encoding="utf-8") as f:
                items = json.load(f)
            if not items:
                empty.append(os.path.basename(path))
        assert not empty, f"Empty data files: {empty}"

    def test_data_files_are_valid_json(self):
        bad = []
        for path in glob.glob(os.path.join(DATA_DIR, "*.json")):
            try:
                with open(path, encoding="utf-8") as f:
                    data = json.load(f)
                assert isinstance(data, list)
            except (json.JSONDecodeError, AssertionError):
                bad.append(os.path.basename(path))
        assert not bad, f"Invalid JSON files: {bad}"
