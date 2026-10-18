Title: Blogging Technology Interlude
LessWrong-URL: https://www.lesswrong.com/posts/zDxxFw5wedrKAEurX/blogging-technology-interlude
Posted: 2026-07-21
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 1 (commentCount field: 1)

#### [-] Brendan Long · 4 karma · 2026-07-22 · https://www.lesswrong.com/posts/zDxxFw5wedrKAEurX/blogging-technology-interlude?commentId=HxwdRDvCHC5gnWBGf
If you find that managing the VPS is annoying, I host a similar Pelican blog by uploading everything directly to a CDN and using edge rules for anything fancy (like your redirects or Markdown content negotiation). I use BunnyCDN because [their storage zones are fast even for cache misses](https://www.brendanlong.com/even-faster-website-with-bunny-cdn-and-micromorph.html), and Claude can configure it with Terraform.

