# MeshMogul Foundations — editorial plan and candidate handoff

Foundations is a free educational collection inside the existing static Guides
section: **3D Building for the AI Era**. It serves creators with or without
MeshMogul. It is not a separate company, certification, membership, or product.

## Current candidate

- [Foundations entry](https://morningforge.github.io/MeshMogul/guides/#foundations)
- [Cornerstone AI asset brief and inspection guide](https://morningforge.github.io/MeshMogul/guides/how-to-prompt-ai-for-roblox-3d-models/)
- [Downloadable plain-text brief](guides/how-to-prompt-ai-for-roblox-3d-models/ai-asset-brief.txt)

The website URLs above describe intended routes. This candidate has **not been
merged or deployed**. Review the files on PR #5's branch until release is
separately authorized. The existing nine guides remain; only one article and
its reusable brief are new.

The four tracks are Build with AI, Understand 3D, Finish and publish, and Test
and optimize. Existing articles do the detailed work; do not create competing
pages to fill a navigation category.

## Next three priorities

1. **Observe a component-preservation exercise.** Try one wheel or hinged gate
   on an authorized disposable example. Compare a vague visual request with the
   structured brief. Record the actual hierarchy, pivots, independent movement,
   output count and source retention, including failures. Extend the cornerstone
   with observed results only after running the exercise; do not claim the
   current three prompts are validated.
2. **Verify one UV-to-publication handoff.** Extend the existing Texture
   Generator and reference guides with a controlled before/after case. Record
   the Studio version and available Smart UV controls, geometry and image
   references, permissions, and save/reopen behavior. A new mesh reference and
   its images must stay together. Any upload needs separate authorization.
3. **Add a measured collision/performance case.** Extend the existing comparison
   guide with matched source and derivative scenes, traversable openings,
   representative devices and repeatable measurements. Separate inspection
   responsiveness, conversion time, mesh complexity and runtime cost. Publish
   conditions and limitations rather than a universal triangle or FPS rule.

A small requested-versus-actual worksheet or revised prompt template may follow
those exercises. Consider an agent skill only after repeated use reveals a
stable task and its failure cases; first inspect existing tooling and ownership.
No skill, agent integration or new execution permission is supplied by this
editorial plan.

## Evidence and content boundaries

- DOCUMENTED: linked primary sources describe behavior. OBSERVED: an actual
  check on a named output. RECOMMENDED: editorial advice. UNVERIFIED: not yet
  established. Preserve those distinctions when updating articles.
- The cornerstone examples are untested starting points. No Studio generation,
  asset publication, benchmark, or prompt-success experiment was performed for
  this website assignment.
- Current Khronos GitHub guidance identifies version 2.0.0, updated August 2025.
  Distinguish its general principles from glTF, Blender, Substance and Roblox
  conventions. The older Khronos registry still lists version 1.0.0.
- Smart UV controls are documented in the original Roblox announcement but not
  described on the current Creator Hub Texture Generator page. Current native
  availability across Studio versions remains unverified.
- This work does not add plugin capabilities, cloud synchronization, arbitrary
  mesh/appearance support, automatic publication or same-ID updates.

## Files and verification record — November 13, 2026

Release corrections: `index.html`, `README.md`, `how-it-works/index.html`,
`supported-inputs/index.html`, `faq/index.html`, `changelog/index.html`,
`guides/index.html`, the Parts-to-mesh, no-Blender and Assistant/ProceduralModel
guides, `DEPLOYMENT.md`, and `tools/check_site.py`.

Foundations: `guides/index.html`,
`guides/how-to-prompt-ai-for-roblox-3d-models/index.html`, its
`ai-asset-brief.txt`, `assets/site.css`, `sitemap.xml`, README and
Assistant/ProceduralModel crosslinks, deployment/checker updates, and this plan.

- Both checker modes pass: **19 HTML pages, 550 links/assets, 18 sitemap
  entries**. Checks include project-path links and fragments, sitemap,
  canonical/social metadata, heading hierarchy, static resources, release
  assertions, approved legal notices, privacy and effective Git identity.
- `git diff --check` passes. All four earlier release bodies are preserved;
  only the current/historical label changed for 1.2.1. No stale 1.2.1 current
  copy remains outside the changelog history.
- Release review sampled 11 desktop routes at 1280 px and five representative
  routes at both 390 and 320 px. Foundations entry/guide and homepage were
  rechecked at all three widths after integration: no document overflow,
  clipped headings or broken images in those samples. Acquisition and track
  navigation targets are 44 px high. This is bounded review, not full
  accessibility certification.
- Keyboard checks: visible skip-link focus and Enter-to-main, FAQ disclosure
  activation, track-anchor activation, guide navigation, and whole-field
  selection in the read-only brief with visible focus. The field wraps on
  narrow screens. Reduced-motion CSS remains intact.
- The download returns HTTP 200 and is byte-identical to the source brief;
  the displayed field matches the same text. All ten guides appear once in
  the four track card lists. Only one new indexable HTML route was added.
- All ten source/license links in the cornerstone returned HTTP 200. Its
  intended canonical URL is not deployed yet. For existing references,
  AssetService returned HTTP 502 through the local client but was retrieved
  successfully through web browsing; an all-references-HTTP-200 result is not
  claimed.
- Public text and PNG metadata were reviewed. No private locations,
  credentials or internal test IDs were introduced. Existing explicitly
  illustrative URI numbers and third-party license attributions are retained.
  New commits use MorningForge author and committer with the authorized
  GitHub noreply address, verified before commit and against remote metadata.

## Durable checkpoints and takeover

Existing branch: `codex/meshmogul-public-1-3-site-editorial-v1`.
Existing review: [PR #5](https://github.com/MorningForge/MeshMogul/pull/5).

- Release accuracy: `e35232b16f96aabd0f65b966857a8ad2cf77990a`.
- Cornerstone guide and brief: `2ca459d40abca050566aa92949cadd09aa7a8dad`.
- Track integration and editorial plan: the commit containing this record.

The PR description was deliberately left unchanged at the Product Owner's
request after an unavailable edit form. Use the current branch files and
commits for review; do not rely on its older description of the release.

Before takeover, verify the remote branch/HEAD and local dirty state. Preserve
unrelated work. One mutating owner at a time. Run both site-checker modes and
recheck affected layouts and primary sources after any further change. Commit
and push only coherent verified work to this existing branch.

The next owner is the Lead/Product Owner for candidate review and a later
publication decision. Merge to main, GitHub Pages deployment, Creator Store
changes, plugin-source edits and Roblox asset publication are not authorized by
this handoff.
