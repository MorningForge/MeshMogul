# Verify a GitHub Pages release

`MorningForge/MeshMogul` already exists, with a public `main` branch and a Pages
workflow. Repository creation is not pending. This document does not authorize
merging, pushing to main, workflow dispatch or deployment.

The established origin is `https://morningforge.github.io/MeshMogul/`. The refresh
branch is a candidate; its legal page and other changes must not be described
as live until the deployed revision has been verified.

## Candidate verification

1. Run `python3 tools/check_site.py`; review the candidate diff and Git identity.
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
