# GitHub Pages publication

The public website repository is `MorningForge/MeshMogul`. Keep website work separate from the private product repository.

## Review candidates

Prepare and validate candidate content on a dedicated review branch. Run `python3 tools/check_site.py` and `git diff --check` before committing. A push to a review branch preserves the candidate; it is not a live Pages release. The 1.1.1 reconciliation does not merge, modify, or deploy `main`.

## Authorized publication

Publication is a separate action requiring authorization. The existing `.github/workflows/pages.yml` runs on pushes to `main` and on manual workflow dispatch; it checks the site, stages public web files, and deploys with official GitHub Pages Actions. Do not manually dispatch it as part of candidate review.

For an authorized release, verify **Settings → Pages → Build and deployment → Source → GitHub Actions**. After the authorized publication, wait for the Pages workflow to succeed and use its deployment URL to verify the home page, a nested guide, navigation, and an unknown-path 404. Repository existence or a branch push alone does not establish a live deployment.

The configured project address is `https://morningforge.github.io/MeshMogul/`; this document does not claim to have verified live hosting. There is no custom domain configuration. If the deployed address differs, reconcile the sitemap, custom 404 links, and project-path checks before publication.

The site needs no installation or build step. The public website deployment is separate from publishing mesh assets in Roblox Studio.
