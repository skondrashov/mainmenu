#!/usr/bin/env python3
"""Aggregate data/*.json into data.js, api/v1/catalog.json, api/v1/categories.json, llms.txt, llms-full.txt, and inject noscript catalog into index.html."""
import json, glob, os, re, html as html_mod
from itertools import groupby

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "data")

entries = []
seen_ids = set()
files = sorted(glob.glob(os.path.join(data_dir, "*.json")))

for path in files:
    with open(path, encoding="utf-8") as f:
        items = json.load(f)
    for item in items:
        if "id" not in item:
            continue
        if item["id"] in seen_ids:
            print(f"  WARN: duplicate id '{item['id']}' in {os.path.basename(path)}, skipping")
            continue
        seen_ids.add(item["id"])
        entries.append(item)

entries.sort(key=lambda e: (e.get("category", ""), e.get("name", "")))

categories = {}
for e in entries:
    cat = e.get("category", "Uncategorized")
    categories[cat] = categories.get(cat, 0) + 1

sorted_categories = sorted(categories.items(), key=lambda x: -x[1])

# --- Output 1: data.js (frontend) ---
out_path = os.path.join(script_dir, "data.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("window.SOFTWARE = ")
    json.dump(entries, f, indent=2, ensure_ascii=False)
    f.write(";\n")

# --- Output 2: api/v1/catalog.json (machine-readable catalog) ---
api_dir = os.path.join(script_dir, "api", "v1")
os.makedirs(api_dir, exist_ok=True)

catalog_path = os.path.join(api_dir, "catalog.json")
with open(catalog_path, "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)
    f.write("\n")

# --- Output 3: api/v1/categories.json (category counts) ---
categories_path = os.path.join(api_dir, "categories.json")
with open(categories_path, "w", encoding="utf-8") as f:
    json.dump(dict(sorted_categories), f, indent=2, ensure_ascii=False)
    f.write("\n")

# --- Output 4: llms.txt (AI agent discovery manifest) ---
llms_lines = []
llms_lines.append("# main.menu")
llms_lines.append(f"> Universal software directory with {len(entries)} entries across {len(categories)} categories. Structured data for AI agents and developers.")
llms_lines.append("")
llms_lines.append("## Endpoints")
llms_lines.append("- Full catalog (JSON): /api/v1/catalog.json")
llms_lines.append("- Categories with counts: /api/v1/categories.json")
llms_lines.append("- Entry schema: /schema.json")
llms_lines.append("- Full text catalog: /llms-full.txt")
llms_lines.append("- Human browsable: /")
llms_lines.append("")
llms_lines.append("## Entry Schema")
llms_lines.append("{ id, name, description, url, category, os[], pricing, tags[], source?, language? }")
llms_lines.append("")
llms_lines.append("Pricing: free | freemium | paid | subscription")
llms_lines.append("OS: windows | macos | linux | web | ios | android")
llms_lines.append("")
llms_lines.append("## Categories")
for cat, count in sorted_categories:
    llms_lines.append(f"- {cat}: {count}")
llms_lines.append("")
llms_lines.append("## Querying")
llms_lines.append("Download /api/v1/catalog.json and filter by:")
llms_lines.append("- category: exact match on category field")
llms_lines.append("- os: check if desired OS is in the os[] array")
llms_lines.append("- pricing: exact match (free, freemium, paid, subscription)")
llms_lines.append("- tags: check if desired tag is in tags[] array")
llms_lines.append("- language: filter libraries by ecosystem (python, rust, go, javascript, etc.)")
llms_lines.append("- text search: match against name, description, tags")
llms_lines.append("")
llms_lines.append("## Example Queries")
llms_lines.append('- "Find free image editors for Linux": filter pricing=free, os contains "linux", category="Image Editors"')
llms_lines.append('- "Python HTTP libraries": filter language="python", category="HTTP Clients"')
llms_lines.append('- "All database tools": filter category in ["Databases", "Database Tools", "Database ORMs"]')

llms_path = os.path.join(script_dir, "llms.txt")
with open(llms_path, "w", encoding="utf-8") as f:
    f.write("\n".join(llms_lines))
    f.write("\n")

# --- Output 4b: llms-full.txt (complete catalog in plain text) ---
full_lines = []
full_lines.append("# main.menu — Full Catalog")
full_lines.append(f"> {len(entries)} entries across {len(categories)} categories")
full_lines.append("")

for cat, group in groupby(entries, key=lambda e: e.get("category", "Uncategorized")):
    cat_entries = list(group)
    full_lines.append(f"## {cat} ({len(cat_entries)})")
    full_lines.append("")
    for entry in cat_entries:
        full_lines.append(f"### {entry['name']}")
        full_lines.append(f"- URL: {entry.get('url', '')}")
        full_lines.append(f"- Description: {entry.get('description', '')}")
        os_list = entry.get("os", [])
        if os_list:
            full_lines.append(f"- OS: {', '.join(os_list)}")
        full_lines.append(f"- Pricing: {entry.get('pricing', '')}")
        tags = entry.get("tags", [])
        if tags:
            full_lines.append(f"- Tags: {', '.join(tags)}")
        source = entry.get("source")
        if source:
            full_lines.append(f"- Source: {source}")
        language = entry.get("language")
        if language:
            full_lines.append(f"- Language: {language}")
        full_lines.append("")

llms_full_path = os.path.join(script_dir, "llms-full.txt")
with open(llms_full_path, "w", encoding="utf-8") as f:
    f.write("\n".join(full_lines))

# --- Output 5: taxonomy.js (tree navigation data) ---
taxonomy_path_src = os.path.join(script_dir, "taxonomy.json")
if os.path.exists(taxonomy_path_src):
    with open(taxonomy_path_src, encoding="utf-8") as f:
        taxonomy = json.load(f)
    taxonomy_js_path = os.path.join(script_dir, "taxonomy.js")
    with open(taxonomy_js_path, "w", encoding="utf-8") as f:
        f.write("window.TAXONOMY = ")
        json.dump(taxonomy, f, indent=2, ensure_ascii=False)
        f.write(";\n")
    print(f"Built taxonomy.js from taxonomy.json")

# --- Output 6: inject noscript catalog into index.html ---
index_path = os.path.join(script_dir, "index.html")
if os.path.exists(index_path):
    with open(index_path, encoding="utf-8") as f:
        index_html = f.read()

    marker_pattern = re.compile(
        r"(<!-- NOSCRIPT_CATALOG -->).*?(<!-- /NOSCRIPT_CATALOG -->)",
        re.DOTALL,
    )

    if marker_pattern.search(index_html):
        # Group entries by category (preserving sorted order)
        cats_ordered = []
        cats_entries = {}
        for e in entries:
            cat = e.get("category", "Uncategorized")
            if cat not in cats_entries:
                cats_ordered.append(cat)
                cats_entries[cat] = []
            cats_entries[cat].append(e)

        # Build noscript HTML
        h = html_mod.escape
        lines = []
        lines.append("")
        lines.append("  <noscript>")
        lines.append(f"  <h1>Main Menu — Software for Everything</h1>")
        lines.append(f"  <p>{len(entries)} entries across {len(categories)} categories.</p>")
        for cat in cats_ordered:
            cat_entries = cats_entries[cat]
            lines.append(f"  <h2>{h(cat)}</h2>")
            for e in cat_entries:
                name = h(e.get("name", ""))
                url = h(e.get("url", ""))
                desc = h(e.get("description", ""))
                os_list = ", ".join(e.get("os", []))
                pricing = e.get("pricing", "")
                tags = ", ".join(e.get("tags", []))
                meta_parts = []
                if os_list:
                    meta_parts.append(f"OS: {h(os_list)}")
                if pricing:
                    meta_parts.append(f"Pricing: {h(pricing)}")
                if tags:
                    meta_parts.append(f"Tags: {h(tags)}")
                meta_str = " | ".join(meta_parts)
                lines.append(f"  <article>")
                lines.append(f"    <h3><a href=\"{url}\">{name}</a></h3>")
                lines.append(f"    <p>{desc}</p>")
                if meta_str:
                    lines.append(f"    <small>{meta_str}</small>")
                lines.append(f"  </article>")
        lines.append("  </noscript>")
        lines.append("  ")

        noscript_block = "\n".join(lines)
        # Build replacement: keep both marker comments with generated content between them
        def _replace_markers(m):
            return m.group(1) + noscript_block + m.group(2)
        index_html = marker_pattern.sub(_replace_markers, index_html)

        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_html)
        print(f"Injected noscript catalog into index.html ({len(entries)} entries)")
    else:
        print("WARN: noscript markers not found in index.html, skipping injection")
else:
    print("WARN: index.html not found, skipping noscript injection")

# --- Summary ---
print(f"Built data.js with {len(entries)} entries from {len(files)} files")
print(f"Built api/v1/catalog.json ({len(entries)} entries)")
print(f"Built api/v1/categories.json ({len(categories)} categories)")
print(f"Built llms.txt ({len(entries)} entries, {len(categories)} categories)")
print(f"Built llms-full.txt ({len(entries)} entries, {len(categories)} categories)")
for cat, count in sorted_categories:
    print(f"  {cat}: {count}")
