# MeshMogul Public Repository Agent Rules

This repository owns the public MeshMogul website and public documentation. Product capability claims remain subordinate to the accepted product release evidence.

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
- Run `python3 tools/check_site.py` and perform bounded desktop/mobile review for site changes.
- Do not modify product source, Creator Store, public main or deploy Pages unless explicitly authorized for that operation. A task-branch push is not merge or deployment authorization.
