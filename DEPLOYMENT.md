# Verify a GitHub Pages release

`MorningForge/MeshMogul` already exists, with a public `main` branch and a Pages
workflow. Repository creation is not pending. This document does not authorize
merging, pushing to main, workflow dispatch or deployment.

The established origin is `https://morningforge.github.io/MeshMogul/`. The release content describes MeshMogul Founding 1.2.1. Website changes must not
be described as live until the deployed revision has been verified.

## Pre-deployment verification

1. Run `python3 tools/check_site.py`; review the proposed diff and Git identity.
2. Preview under `/MeshMogul/`. Inspect desktop and narrow home, legal, a nested
   guide, FAQ disclosures, keyboard focus and 404 recovery links.
3. Review approved media for identity/privacy and confirm its captions do not
   present old UI as current release evidence.
4. Confirm the explicit staging list includes `legal/`, `LICENSE.md` and
   `THIRD_PARTY_NOTICES.md`, alongside existing public routes and assets. Exclude
   private source, audit documents, tooling, logs and credentials.

## After separately authorized release

1. Confirm **Settings → Pages → Source** is **GitHub Actions**. Do not recreate
   the repository or change hosting architecture.
2. Verify the intended commit is on the authorized release branch. The workflow
   runs on a push to `main` or manual dispatch; neither is implied by permission
   to push a task branch.
3. Inspect the workflow result and deployment environment URL. Confirm the
   deployed commit, not merely that an earlier deployment succeeded.
4. Check home, a nested guide, FAQ, an unknown-path 404, legal, license and notices
   at the deployed origin. Confirm mobile acquisition links still target Creator
   Store asset `126445067739142`.
5. Only then report that this release and
   `https://morningforge.github.io/MeshMogul/legal/` are live. If hosting changes,
   reconcile sitemap, canonical metadata, 404 paths and checker origin first.

The workflow uses an explicit public-file allowlist and official GitHub Pages
Actions. No paid hosting, build framework or runtime dependency is needed.

## Copy checklist for the 1.3 website update

Keep the current 1.2.1 identity until the Product Owner confirms the actual
Creator Store release. A source change or successful candidate test is not
release confirmation. This editorial candidate does not announce 1.3.

| Surface | Smallest change after release confirmation |
| --- | --- |
| Home and README | Update the current version, release link, and matching social metadata. Describe only the capabilities included in the delivered plugin. |
| Compatibility | Replace individual Union/CSG or Glass refusal rows only for the accepted, released input scope. Keep unreadable-content, overlay, permission, fidelity, and size limits explicit. |
| How it works and FAQ | Match the delivered controls and workflow. Preserve approval of the exact retained Preview, manual Command Bar publication, source retention, and local Assets boundaries. |
| Changelog | Add a current release section with accepted customer changes; retain earlier versions as history. |
| Guides | Update version-specific compatibility statements. Describe native texturing separately from any explicitly released derivative tracking; do not infer tracking from geometry publication. |
| Site checker and sitemap | Update the deliberate version guard and release assertions together with the copy. Change the sitemap only when routes change. |

Before deployment, review the release wording and run the existing checks plus
desktop/mobile and keyboard review. Union/CSG, Glass, and textured-derivative
lifecycle claims each need their own accepted scope; none is inferred from the
release number. Merge and Pages deployment remain separately authorized actions.
