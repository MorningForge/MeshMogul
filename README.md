# MeshMogul public website

This repository contains the public MeshMogul marketing website only. Product source remains private elsewhere. No plugin implementation, internal specifications, customer fixtures, or private tooling belongs here.

The site is semantic HTML, CSS, and original SVG artwork. It has no framework, runtime JavaScript, paid dependency, backend, visitor accounts, analytics, or external font/image requirement. Roblox and GitHub documentation links are optional reading.

## Preview

From this directory, run:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Visit `http://127.0.0.1:8000/`. Links are relative so ordinary pages also work at the GitHub Pages project path `/MeshMogul/`. For an exact project-path preview, place the checkout in a directory named `MeshMogul`, serve its parent directory, and visit `/MeshMogul/`.

Run the static checks:

```sh
python3 tools/check_site.py
```

No installation or build is needed. Edit the checked-in HTML and CSS directly. The seven initial guide articles are explicitly marked editorial drafts and have useful content rather than empty search-target pages.

## Ownership and publication

MorningForge owns this website. The public repository is `MorningForge/MeshMogul`. Never use the private product repository as a deployment destination or copy product files here.

`.github/workflows/pages.yml` checks the site, stages only public web files, and deploys with official GitHub Pages Actions. A push to `main` or a manual workflow dispatch triggers it. Deployment needs Pages configured with **GitHub Actions** as its source. The workflow does not create a repository, enable Pages, or alter repository settings. GitHub Pages hosting on a public repository requires no paid hosting service.

Candidate content belongs on a review branch. Pushing that branch is not a live Pages release; merging or deploying requires a separate authorized action. See [DEPLOYMENT.md](DEPLOYMENT.md) for the publication boundary. This reconciliation does not deploy Pages or change `main`.

The anticipated default address is `https://morningforge.github.io/MeshMogul/`; it is not a verified live URL. The sitemap uses that intended default address. If the actual deployment uses a different host/path, update every sitemap location, the custom 404 links, and the `PROJECT_BASE` check constant before publishing. Canonical and `og:url` tags are intentionally omitted until the actual public origin is confirmed, avoiding an unverified canonical destination. Titles, descriptions, Open Graph titles/descriptions/types, a sitemap, and robots rules are included.

## Content and media

- Home: `index.html`
- Workflow: `how-it-works/`
- Compatibility: `supported-inputs/`
- Guide index and seven draft articles: `guides/`
- FAQ, changelog, and factual data boundaries: `faq/`, `changelog/`, `privacy/`
- Styling and original illustrations: `assets/`
- Approved future screenshots/demos: `assets/media/`

The home-page concept illustration is labeled as artwork. The screenshot/demo slot remains a visibly marked placeholder. The Creator Store CTA links to [MeshMogul by MorningForge](https://create.roblox.com/store/asset/126445067739142), verified against Roblox’s public Creator Store search and item details. Do not add unverified destinations or pricing claims.

The content describes upcoming Founding `1.1.1`, without asserting a release date or that the version is distributed on Creator Store. Mogul Insights highlights the selected build before Preview; Technical Details provides supporting evidence; Model Info explains composition, appearance, and source. References shows known source Mesh IDs when available, ordered consistently with source details, selectable for the explicit Ctrl+C copy workflow. The update also improves MeshPart access diagnostics, supported embedded-color round trips, and publication progress/results. The changelog retains `1.1.0` history, including multi-output, grouped Preview, and grouped Assets behavior.

Keep limitations prominent: supported input only, manual Studio Command Bar publication, local records, no direct Union/CSG conversion, no universal PBR fidelity, no guaranteed optimization, no same-ID update flow, and no team/cloud sync. Studio rendering does not guarantee editable MeshPart geometry access; unavailable geometry is reported rather than discarded. Permissions, ownership, and sharing are possible causes, not guaranteed diagnoses. References does not promise other asset or texture-map inventories. Public attribution uses only MorningForge or MeshMogul by MorningForge; do not add human personal names. Recheck claims when the product changes.

The custom 404 uses `/MeshMogul/` absolute links because GitHub serves it at arbitrary missing request paths. All normal pages and assets use relative links. GitHub Pages provides its own 404 status; the file is not an application router.
