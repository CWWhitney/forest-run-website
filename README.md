# Forest Run website

Source for [forestrun.org](https://forestrun.org): the sauna and icosahedron
house at Forest Run in Camden, Maine. Hugo site, deployed by Netlify.

[![Netlify Status](https://api.netlify.com/api/v1/badges/235c4b03-c385-4045-917f-e631560f77a4/deploy-status)](https://app.netlify.com/)

- preview the site locally: `blogdown::serve_site()` (needs Hugo 0.130.0, the
  version Netlify uses: `blogdown::install_hugo("0.130.0")` and
  `options(blogdown.hugo.version = "0.130.0")`)

- edit pages in `content/`, menu and emails in `config.toml`

- add photos: put the originals in a folder outside this repo, then run
  `python3 -I scripts/process-photos.py "<folder>" build` (or `sauna`).
  Sketches: `python3 -I scripts/process-sketches.py "<folder>" drawings`.
  This makes small web copies with GPS data removed in `static/images/`.
  Show them on a page with `{{< gallery dir="images/sauna" >}}`
  (default `images/build`; add `fit="contain"` for drawings)

- publish: commit and push. Netlify builds the live site

Keep the git repo out of Dropbox (it corrupted `.git` once). Do not edit
`public/` or `themes/`.
