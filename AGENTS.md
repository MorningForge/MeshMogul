# MeshMogul Public Repository Agent Rules

This repository owns the public MeshMogul website and related public documentation. Product capability claims remain subordinate to the canonical MeshMogul product repository and accepted release evidence.

## Git identity / privacy

- Every commit created by an agent, Codex task, local worker, or automated MorningForge workflow must use the **MorningForge** identity only. Personal names and personal email addresses are forbidden in Git author or committer metadata unless Will explicitly authorizes that exact identity for that exact commit.
- Before any commit, do not trust inherited Git, Windows, IDE, container, or workspace identity. Inspect identity sources with `git config --show-origin --show-scope --get-regexp '^user\\.(name|email)$' || true` and inspect any `GIT_AUTHOR_*` / `GIT_COMMITTER_*` environment overrides.
- For ordinary agent/local Git commits, explicitly pin this worktree/repository before committing:
  - `git config --local user.name "MorningForge"`
  - `git config --local user.email "311570204+MorningForge@users.noreply.github.com"`
- Immediately before commit, `git var GIT_AUTHOR_IDENT` and `git var GIT_COMMITTER_IDENT` must both resolve to MorningForge with a MorningForge-controlled address. After commit, verify `git show -s --format='author=%an <%ae>%ncommitter=%cn <%ce>%nsha=%H' HEAD`.
- Approved MorningForge-controlled addresses are the GitHub noreply address above and brand-owned MorningForge mailboxes such as `morningforge@proton.me` / `morningforge@protonmail.com`. A personal mailbox is never acceptable merely because authentication succeeded.
- Authentication and authorship are separate. GitHub login, Windows credentials, IDE state, or repository ownership do not authorize personal commit metadata.
- After push, verify the remote commit's author and committer metadata before declaring PASS. If a personal identity appears, STOP; do not merge, release, or continue publication until that commit is rewritten or otherwise removed from reachable branch/tag history as appropriate.


## Public-content privacy

- Public content must identify the product/company as **MeshMogul** and/or **MorningForge**. Do not publish Will's personal/legal/account name or personal contact information unless he explicitly authorizes that exact public use.
- Before any public-site release, sweep both content and Git metadata for personal identity leakage.
