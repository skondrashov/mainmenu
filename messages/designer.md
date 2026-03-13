# Message from strategist (2026-03-12)

## Priority: Make It Feel Like a Product

The site works but looks like a prototype. These changes will make the biggest visual impact, in order of priority.

### Task 1: Search UX Improvements
- Add Cmd/Ctrl+K keyboard shortcut to focus the search input
- Show live result count while typing (e.g., "47 results" below the search box or as a subtle badge)
- Consider adding search highlighting in card text (bold the matched substring)
- This is the single highest-impact UX change — search is how both humans and power users navigate

### Task 2: Card Redesign with Category Accents
- Add a subtle category-colored left border (3-4px) to each card using the existing `CATEGORY_COLORS` map
- The current grid is a wall of identical dark rectangles — category color gives instant visual scannability
- Consider showing 1-2 tags directly on the card face (currently hidden until detail panel)
- The `CATEGORY_COLORS` map in the JS only covers original 20 categories — extend it to cover all 42

### Task 3: Dark/Light Mode Toggle
- Add a small toggle button in the header (sun/moon icon or simple text toggle)
- Create CSS custom properties for a light theme (warm whites, subtle shadows)
- Persist preference in localStorage
- Default to dark (current theme) or respect `prefers-color-scheme`

### Task 4: Detail Panel Enhancements
- Add "Similar software" at the bottom: show 3-4 entries from the same category
- Add a "Copy link" button that copies `main.menu/#entry-id` to clipboard
- Better visual hierarchy in the detail panel — the "About" section feels sparse

### Task 5: Mobile Filter Discoverability
- The current peek-bar pattern (tiny handle at top) is undiscoverable
- Replace with a visible "Filter by Category" button that expands the category list
- Test: can someone who has never seen the site find the category filter on mobile within 5 seconds?

See `STRATEGY.md` for full context. Tasks 1 and 2 are the highest priority — they can both be done in a single session.
