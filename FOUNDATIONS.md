# MeshMogul Foundations candidate

This candidate expands the existing Guides section into a free, 16-article
Roblox engineering library. All eight visual topics are now integrated from the supplied Studio capture
collection. The candidate is ready for Product Owner aesthetic review, with
the specific authenticity limitations below. Merge, Pages deployment, and Roblox asset publication are not part
of this candidate.

## Implemented

- All 16 complete articles across four subjects, preserving the ten existing
  routes and adding six guide routes. Every article is in the sitemap with a
  matching canonical URL and social metadata.
- Three guided learning paths with ordered steps, article-level progress,
  previous/next links, prerequisites, and related reading.
- Symptom discovery, subject navigation, difficulty metadata, and full-text
  search by title, technical terminology, symptoms, tags, and article content.
- Responsive article typography, collapsible contents, keyboard-scrollable
  comparison tables and Luau examples, a selectable AI brief, and the unchanged
  downloadable brief. All legacy fragment anchors remain, including the brief
  field and its help text.
- Documentation review dates from the editorial review of November 15, 2026,
  with next-review dates. These dates do not claim fresh native Studio tests.
  Evidence notes and primary references replace repetitive paragraph badges.
  Current Smart UV UI uncertainty remains explicit.
- One deferred, same-origin search script and one generated static index.
  Search words stay in memory on the page. No cookies, telemetry, fingerprinting,
  external runtime dependencies, URL query transmission, or browser storage.
  The full library remains browsable with JavaScript disabled or the index
  unavailable. Privacy copy explains this bounded enhancement.

The existing site branding, commercial pages, pricing, product limitations,
release history, license notices, and legal page are preserved. Shared CSS adds
Foundations components and improves containment of long article content.
The visual additions use actual Studio scene captures. Staged teaching fixtures
are explicitly labeled; no measured performance result or unverified plugin
state is presented as runtime proof.

## Verification

Completed in Chromium on the local project-path preview:

- `python3 tools/check_site.py`: 25 HTML pages, 1,112 links/assets, 24 sitemap
  entries; route, canonical, anchor, heading, alt, release, legal, privacy,
  public-content, and runtime-resource checks pass.
- `python3 tools/build_search_index.py --check`: generated index matches all
  article HTML and public metadata. The public catalog contains no private
  manuscript locations or editorial production instructions.
- `python3 tools/test_search_policy.py`: the exact deferred script is allowed
  only on the hub. External and protocol-relative scripts, other local scripts,
  inline script bodies, duplicate scripts, extra execution attributes, and
  inline event handlers are rejected. The checker pins the inspected search
  implementation by SHA-256; this is not a general local-JavaScript waiver.
- `node tools/check_foundations_browser.cjs`: search terms including
  `CollisionPrecision`, `MikkTSpace`, `GenerationError`, `WorldPivot`, `MeshId`,
  and dark-smudge symptoms find the expected guides. Combined subject/difficulty
  filters, zero results, reset, safe handling of markup-like input, subject
  jumps after filtering, keyboard tab order, labelled controls, and live result
  announcements pass.
- The hub and every direct article URL return successfully at 1280, 390, and
  320 pixels without page-level horizontal overflow. Tables and code scroll
  within their containers. Representative screenshots were visually inspected.
- JavaScript-disabled browsing exposes all 16 articles, all three path
  sequences, and the exact selectable/downloadable brief. Failed-network and
  malformed-index checks also preserve the complete static catalog.
- Browser requests stay on the local site origin; no cookies or browser storage
  are created, and no page errors occur. Accessible names and status roles were
  inspected through Chromium's accessibility tree. A spoken screen-reader
  session and native Studio runtime tests have not been performed.

Browser screenshots are website evidence, not Roblox Studio evidence:

| Width | Hub | Search | Article |
| --- | --- | --- | --- |
| 1280 | [View](review/foundations/hub-1280.png) | [View](review/foundations/search-1280.png) | [View](review/foundations/article-1280.png) |
| 390 | [View](review/foundations/hub-390.png) | [View](review/foundations/search-390.png) | [View](review/foundations/article-390.png) |
| 320 | [View](review/foundations/hub-320.png) | [View](review/foundations/search-320.png) | [View](review/foundations/article-320.png) |

These review files and this report are outside the Pages staging allowlist.

## Eight-station visual intake and delivery

All 48 supplied assets exist and match their manifest byte sizes and SHA-256
hashes. The directory contains 44 PNGs (including 11 motion frames), two GIFs,
and two MP4 frame sequences. Station 04 has six motion frames; the capture
report's five-frame summary was inaccurate. No original was edited or moved.
The collection also contains eight manifests and one progress report, which
are metadata rather than part of the 48-media-file total.

| Station | Media files | Website treatment | Article |
| --- | ---: | --- | --- |
| 01 · Gate pivot | 10 | Leaf-center / hinge-edge crops and optional motion sequence | [AI asset brief](guides/how-to-prompt-ai-for-roblox-3d-models/#visual-01) |
| 02 · Texture Generator | 6 | Fast / Quality surface crops retaining native completion toasts | [Texture Generator](guides/roblox-studio-texture-generator/#visual-02) |
| 03 · Hidden geometry | 4 | Stacked / stretched wall crops, excluding unmeasured draw-call signs | [Rendering costs](guides/draw-calls-instancing-and-hidden-faces/#visual-03) |
| 04 · Doorway collision | 11 | Filled / open frame crops and optional staged avatar sequence | [Doorway collision](guides/collision-fidelity-and-invisible-doorways/#visual-04) |
| 05 · Normals and budgets | 5 | Three panels: edges, map direction, texture tiers | [Surface data](guides/normals-uv-seams-and-texture-budgets/#visual-05) |
| 06 · Appearance grouping | 4 | Mixed-source / appearance-domain fixture crops | [Multi-material groups](guides/why-models-split-into-multiple-meshparts/#visual-06) |
| 07 · Preflight and Preview | 4 | Primitive row / staged freshness-warning comparison | [Preflight](guides/preflight-and-retained-previews/#visual-07) |
| 08 · Assembly pivot | 4 | Distant / intentional origin comparison | [Assembly preparation](guides/preparing-studio-builds-for-finalization/#visual-08) |

Seventeen panels use 32 metadata-free WebP files, with responsive variants
where the source resolution permits. Two silent H.264 clips use the existing
FFmpeg encoding and ffprobe QA approach. Total optimized media: 625,015 bytes
(about 610 KiB), including every image variant and both clips. The clips are
collapsed, user-controlled, looping, and `preload="none"`; nothing autoplays.
Images have descriptive alt text, explicit dimensions, lazy loading, and
asynchronous decoding. HTML labels reflow into a single column on mobile.

[Source attribution and derivative identities](assets/foundations/attribution.json)
record all 48 source hashes and all 34 output hashes, crop rectangles, dimensions,
encoding settings, sizes, and clip durations. They contain no private paths,
account details, raw manifests, or asset IDs. Public image metadata is empty;
video metadata contains only encoding/container information. No raw captures
or GIFs were added to the website.

### Evidence boundaries

- **Actual captured evidence:** Studio scene geometry and appearance; native
  re-texturing completion toasts in station 02. Other full-window source captures
  include native Studio overlays. Capture provenance does not establish every
  technical claim written on an in-world sign.
- **Educational illustrations:** pivot arrows and rotation arcs; stacked-block
  cutaways; colored collision volumes and staged avatar routes; normals/map
  direction marks and texture tiers; grouping hierarchy boards; and the
  freshness/blank-MeshId board. These remain useful lessons and are labeled as
  illustrations in the article captions.
- **Not independently established by this collection:** measured draw-call or
  frame-time savings; active collision settings or a physics-driven walkthrough;
  controlled split-normal/normal-map shading or a UV layout; current generation
  mode controls, map assignments, resolution, or UV settings; an actual
  MeshMogul conversion and native Explorer output count; a genuine stale-source
  refusal or blank MeshId in Properties; and actual pivot/PrimaryPart property
  values or post-finalization pivot retention. These are specific proof gaps,
  not reasons to discard the accepted captures or repeat the capture sessions.
- The supplied MP4s contain short stepped frame sequences, not continuous
  runtime recordings. Captions and playback descriptions preserve that distinction.

### Media verification

The expanded browser suite checks all eight visual stations at 1280, 390, and
320 pixels: images decode, alt text and responsive sources exist, and pages
remain free of horizontal overflow. Screenshots of all 24 station/width
combinations were captured, with desktop and mobile examples visually reviewed.
The review corrected the doorway, texture-tier, and grouping crops. Both clips
played through to completion in Chromium with no audio stream. No MP4 request
occurs before playback; reduced-motion starts still. Existing search, safe-text,
keyboard, accessible-name, no-JavaScript, failed-index, local-network-only,
no-cookie, and no-storage checks still pass. Source hashes were checked again
after production, and each derivative matches its recorded hash and dimensions.

Website implementation and technical verification are complete for this
candidate. Product Owner aesthetic acceptance remains pending. Native proof
limitations remain disclosed; merge, deployment, and publication are not authorized.

## Maintenance and rerunning checks

Article HTML is the served content. Edit it directly, update the public
`assets/foundations-catalog.json` when discovery metadata changes, and run:

```sh
python3 tools/build_search_index.py
python3 tools/check_site.py
python3 tools/test_search_policy.py
```

No build step or package installation is needed to serve the site. Browser
verification additionally uses Playwright and Chromium as development tools;
these are not loaded by the website. Serve the repository under `/MeshMogul/`
and run `node tools/check_foundations_browser.cjs`. Set `FOUNDATIONS_BASE_URL`
and `CHROMIUM_PATH` when using a different local preview or Chromium location.
The browser check writes temporary screenshots to ignored `.local/`, including
`visual-01` through `visual-08` at each required width. On Windows use UTF-8
Python mode (`PYTHONUTF8=1`) and LF checkout text for the existing exact-byte
script digest and downloadable-brief checks. Playwright is a local development
tool; it adds no website dependency.

Search is intentionally plain text, case-insensitive and punctuation-tolerant;
all words must match within an article. It does not use fuzzy or semantic
ranking. Difficulty ranges include their intermediate levels.
