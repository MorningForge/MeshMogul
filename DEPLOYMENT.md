# Verify a GitHub Pages release

`MorningForge/MeshMogul` already exists, with a public `main` branch and a Pages
workflow. Repository creation is not pending. This document does not authorize
merging, pushing to main, workflow dispatch or deployment.

The established origin is `https://morningforge.github.io/MeshMogul/`. This
candidate represents **MeshMogul 1.3.0**, confirmed published to the existing
Creator Store listing by the Product Owner. Store publication and website
deployment are separate: do not describe these website changes as live until
the deployed revision has been verified.

## Pre-deployment verification

1. Run `python3 tools/check_site.py` and
   `python3 tools/check_site.py --check-git-identity`; review the proposed diff
   and both author and committer identity. On Windows, use the installed Python
   interpreter if the `python3` alias is unavailable.
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

## Release-accuracy checklist for the 1.3 website

The Product Owner has confirmed the Creator Store release. Current copy and
metadata must identify 1.3.0, while earlier changelog entries remain history.
A future source change or successful candidate test alone does not authorize
another shipped-release claim.

| Surface | Required review |
| --- | --- |
| Home and README | Identify 1.3.0 and link its release notes. Match titles, descriptions, and social metadata. |
| Compatibility | Describe supported solid Union/CSG mixed assemblies and supported transparent Glass Union workflows, including separate Glass/opaque outputs. Keep unreadable-content, overlay, permission, fidelity, and size limits explicit. |
| How it works and FAQ | Explain improved Preview progress/cancellation. Preserve approval of the exact retained Preview, manual Command Bar publication, source retention, and local Assets boundaries. |
| Changelog | Explain expanded inputs and bounded, incremental selection inspection. One-click Preview and grouped outputs predate 1.3. Preserve earlier release sections. |
| Guides | Update version-specific compatibility statements. Describe native texturing separately from any explicitly released derivative tracking; do not infer tracking from geometry publication. |
| Site checker and sitemap | Check the current release and historical labels. Add a sitemap entry for each new indexable route. |

Before deployment, run the checks plus desktop/mobile and keyboard review.
Distinguish editor responsiveness during inspection from conversion time,
resulting mesh complexity, and measured game runtime performance. No universal
FPS improvement or safe handling of every enormous Workspace is promised.
Native texturing and downstream textured derivatives remain separate workflows;
do not infer automatic tracking from geometry publication. Review public text,
media, metadata and Git identity for privacy. Merge and Pages deployment remain
separately authorized actions.
