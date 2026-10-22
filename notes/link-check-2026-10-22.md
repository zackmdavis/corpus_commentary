# Live link check, 22 Oct 2026 (before the v1 freeze)

`python3 -I tools/check_live_links.py notes/link-check-2026-10-22.tsv` fetched all 473 distinct external links in `study/*.html` (curl GET, redirects followed). 297 returned 2xx. The other 176:

- **170 LessWrong links** returned 403 to every scripted request (bot protection, not missing pages). All were verified through the LessWrong GraphQL API instead: 54 posts exist, and all 140 linked comments exist, belong to the post named in the link, and are not deleted.
- **5 DOIs** returned 403 from the publishers' sites (PNAS, Taylor & Francis ×2, SAGE, MDPI). Checked at doi.org without following redirects: all five resolve (302) to the article pages.
- **1 IEP link** (iep.utm.edu/epistemic-injustice/) returned 500; the IEP home page also returned 500, so the site was down at the time. The link is kept; the Wayback availability API was rate-limited (429).

No link was changed. Draft links into the blogs' Gitweb repositories (pinned to commits) and links to both blogs all returned 2xx.
