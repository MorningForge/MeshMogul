# MeshMogul public website

This repository owns the public MeshMogul marketing website and public notices.
The plugin source is private and is not published or licensed by this website.
Current release: **Founding 1.1.1**.

The site uses semantic HTML, CSS and original SVG artwork. It has no framework,
runtime JavaScript, backend, analytics, visitor accounts or external font/image
dependency. Keep supported-input limitations visible; do not turn appearance
preservation into a universal PBR, texture-baking or optimization promise.

## Preview and checks

Serve the parent directory and open the project path:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory ..
```

Open `http://127.0.0.1:8000/MeshMogul/`. Run:

```sh
python3 tools/check_site.py
python3 tools/check_site.py --check-git-identity
```

The checks cover local links/anchors, project-path handling, metadata, sitemap,
release identity, legal/footer coverage, approved contact and Git identity,
privacy patterns, static dependencies and public artifact staging. Also inspect
desktop/mobile layouts and keyboard focus/disclosures. Static checks do not
prove runtime product behavior or comprehensive accessibility compliance.

## Public surfaces

- Home: `index.html`; Build → Preview → Publish → Remember → Reuse.
- Workflow and boundaries: `how-it-works/`, `supported-inputs/`.
- Seven practical draft articles: `guides/`.
- Questions, release history and data boundaries: `faq/`, `changelog/`, `privacy/`.
- Website ownership and complete plugin notices: `legal/`, `LICENSE.md`,
  `THIRD_PARTY_NOTICES.md`. Plugin notices are not website runtime dependencies.
- Styling and explanatory artwork: `assets/`; approved media belongs in
  `assets/media/`. The concept diagram is artwork, not a runtime capture.

1.1.1 includes grouped Preview and Assets, multiple outputs for supported
appearance groups, improved supported appearance preservation, freshness and
partial-result handling, ordered source MeshId copy, inspection/navigation,
exact-instance Find, Reset Position and in-plugin What’s New. Publication remains
an explicit guided Studio Command Bar handoff. No direct Union conversion,
automatic publishing, same-ID updates, team/cloud sync or guaranteed optimization.

The verified acquisition destination is
[MeshMogul on Creator Store](https://create.roblox.com/store/asset/126445067739142).
Do not add pricing or imply the website installs the plugin.

## Hosting and release

The public repository exists at `MorningForge/MeshMogul`. The established site
origin is `https://morningforge.github.io/MeshMogul/`; canonical metadata, sitemap
and 404 paths use that project prefix. A local branch does not prove its changes
are deployed. The new legal route is an intended deployment surface until its
specific release has been deployed and verified.

The Pages workflow checks and stages only explicit public files. Pushing to
`main` or manual workflow dispatch triggers deployment; a task branch push does
not. Do not merge, dispatch or deploy without authorization. See
[DEPLOYMENT.md](DEPLOYMENT.md) for release verification.

## Ownership and identity

Use only MorningForge, MeshMogul or MeshMogul by MorningForge publicly. Public
contact, where needed: `morningforge@proton.me`. Every agent commit must use
exactly `MorningForge <311570204+MorningForge@users.noreply.github.com>` for both
author and committer. Public access is not an open-source license; see
[LICENSE.md](LICENSE.md). Third-party permissions remain effective.
