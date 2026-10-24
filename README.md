# Forest Run website

Source for [forestrun.org](https://forestrun.org): Forest Run in Camden, Maine.
This is a Hugo site in an RStudio project, served locally with blogdown and
built by Netlify. Site pages are Markdown in `content/`; settings and navigation
are in `config.toml`. There are no `.Rmd` pages in the current site.

- Preview locally: `blogdown::serve_site()` (needs Hugo 0.130.0, the version
  Netlify uses: `blogdown::install_hugo("0.130.0")` and
  `options(blogdown.hugo.version = "0.130.0")`)
- Edit pages in `content/` and menu or email settings in `config.toml`.
- Rebuild the selected house and sauna web photos from their originals with
  `scripts/process-photos.py`. The CSV selection files record exactly which
  source files are used and their web names. For example:

  ```sh
  python3 -I scripts/process-photos.py \
    "/Users/corywhitney/Library/CloudStorage/Dropbox/Personal/House/Camden/Cabin/Cabin_Photos" \
    house scripts/house-photo-selection.csv
  python3 -I scripts/process-photos.py \
    "/Users/corywhitney/Library/CloudStorage/Dropbox/Personal/House/Camden/Cabin/Sauna_photos" \
    sauna scripts/sauna-photo-selection.csv
  ```

  The script corrects image orientation, resizes to at most 1400 pixels,
  strips metadata, and writes web JPEGs to `static/images/`. It leaves the
  original photos in their source folders. Update a selection CSV to change
  which photos are used.
- Publish by committing and pushing. Netlify builds the live site.

Keep the git repo out of Dropbox (it corrupted `.git` once). Do not edit
`public/` or `themes/`.
