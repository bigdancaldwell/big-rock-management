# bigrockmanagement.com

The umbrella website for the Big Rock group of companies: plain HTML/CSS on GitHub Pages.

## Editing

The pages are generated from `_src/build.py` so the header, footer, and quote form stay identical everywhere.
Edit the text there, then run:

    python3 _src/build.py

(GitHub Pages ignores the `_src` folder.) The styles are in `styles.css` and the patch artwork is in `assets/patches.svg`.

## Two settings in `main.js`

- `FORM_ENDPOINT`: paste your Formspree endpoint (free, at formspree.io, delivering to BigRockLMTD@gmail.com). Until then, the quote form opens the visitor's email app with their request filled in.

## Photos

Every photo in `assets/img/` except the logo is a free Unsplash placeholder. To swap in real job photos, replace the file with one of the same name and shape.
