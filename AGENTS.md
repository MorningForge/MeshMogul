# MeshMogul Public Repository Agent Rules

This repository owns the public MeshMogul website and public documentation. Product capability claims remain subordinate to the accepted product release evidence.

## Release-only destination and workflow

- This public repository is a release-only destination for the live customer website and public documentation.
- Drafting, experiments, exploratory work, and unfinished feature development belong in private workspaces (local checkouts or private repositories).
- Do not create public work-in-progress (WIP) branches, draft PRs, or intermediate review threads on GitHub without explicit Product Owner authorization.
- Deliver updates as one cohesive, verified release commit per approved publication, preserving clean rollback history and release checkpoints on `main`.
- Never force-push or rewrite public history. Testing and review must be completed before publication to `main`.
- Product Owner retains final publication authority. Private product repositories are unaffected.

## Repository layout

- Root is reserved for customer landing and essential governance: `README.md`, `LICENSE.md`, `AGENTS.md`, and the `site/` directory.
- All deployable public website files, routes, images, and static assets reside under `site/`.
- Site verification tooling resides under `.github/scripts/check_site.py`.
- Internal developer notes, roadmaps, and candidate handoffs belong in private Brain tracking, not in the public repository.

## Git identity

- Every agent or automated commit must use exactly `MorningForge <311570204+MorningForge@users.noreply.github.com>` for both author and committer. Alternate names and email addresses are not authorized.
- Before committing, inspect identity configuration and environment overrides without printing personal values. Pin this repository with:
  - `git config --local user.name "MorningForge"`
  - `git config --local user.email "311570204+MorningForge@users.noreply.github.com"`
- Immediately before commit, verify `git var GIT_AUTHOR_IDENT` and `git var GIT_COMMITTER_IDENT` resolve to that exact identity. After commit and push, verify author and committer metadata again. Authentication does not establish authorship.
- Preserve unrelated work. Stage only task-owned files. Never force-push or rewrite history without explicit authorization.

## Public content and privacy

- Public identity may use only MorningForge, MeshMogul, or MeshMogul by MorningForge. Refer to a decision maker neutrally as Product Owner.
- The only authorized public contact email is `morningforge@proton.me`, where intentionally needed. It is not an alternate Git author or committer address.
- Never publish personal/legal/account names, personal email addresses, personal usernames, machine paths, private workspace URLs, private repository locations, private specifications or internal investigations.
- Review all tracked text, image content, image metadata and candidate Git metadata before publication. Do not repeat removed personal information in reports, comments or commit messages.
- Keep third-party license attributions intact; they identify their respective contributors, not MorningForge's public identity.

## Site and release boundaries

- Preserve semantic HTML, CSS, keyboard access, responsive layout and reduced-motion behavior. No framework, backend, analytics, accounts or unnecessary JavaScript/runtime dependency.
- Keep supported-input limitations and explicit guided Studio Command Bar publication visible. Do not promise universal conversion, arbitrary texture/PBR baking, automatic publishing, same-ID updates, cloud sync or guaranteed optimization.
- Run `python3 .github/scripts/check_site.py` and perform bounded desktop/mobile review for site changes.
- Do not modify product source, Creator Store, public main or deploy Pages unless explicitly authorized for that operation.
