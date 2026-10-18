# Pilot chapter (Fable 5.1 session, 2026-10-16)

Phase 2 pilot: "the philosophy of categorization as it develops across both blogs".

- `index.html` — the chapter (built from `parts/*.html` by `tools/build.py`).
- `parts/` — chapter sections. Quotations carry `data-src` attributes naming the source file.
- `tools/check_quotes.py` — verifies every `<q>`/`<blockquote>` with `data-src` against its source.
- `sources.md` — external sources fetched and read in this session (URLs, access dates, local copies under `sources/`).
- `sources/raw/`, `sources/text/` — fetched pages and their text conversions.
- `reading-log.md` — which corpus texts were read in full for this chapter.

Build: `python3 -I pilot/fable/tools/build.py`
Check: `python3 -I pilot/fable/tools/check_quotes.py pilot/fable/parts/*.html`
