# MeshMogul

**Make reusable mesh assets from supported Roblox Studio builds.** Keep your original, inspect and approve a Preview, then publish and reuse confirmed results from a local Assets library.

This repository contains the **MeshMogul website and documentation**. The paid, proprietary Studio plugin is available through Creator Store; its source is not included here.

> **Current release: MeshMogul 1.3.0**, available on the Roblox Creator Store.

[Official website](https://morningforge.github.io/MeshMogul/) · [Creator Store listing](https://create.roblox.com/store/asset/126445067739142) · [Product guides](https://morningforge.github.io/MeshMogul/guides/)

## What MeshMogul does

Use MeshMogul when you have supported Parts, MeshParts, solid Unions, or Models built in Studio and want a reusable visual mesh result without first moving the build into an external modeling application. Inspect the retained Preview, choose when to publish, then reuse confirmed mesh IDs from Assets in Studio.

The workflow is **Build → Preview → Publish → Remember → Reuse**. Publishing requires reviewing and manually running the generated command in Studio’s Command Bar. Preview approval and the publication handoff are deliberate creator actions. MeshMogul preserves the source build.

## New in 1.3.0

Selection inspection now uses bounded hierarchy traversal and incremental, frame-sliced work to reduce expensive editor stalls, with safeguards for pathological selections. Preview has clearer staged progress and cancellation. These are editor-workflow improvements, not a measured FPS gain or guaranteed conversion-time improvement. One-click Preview and grouped outputs predate 1.3.

## Check compatibility first

MeshMogul supports specific inputs and appearance states. Unsupported descendants block the selected root instead of disappearing silently. Version 1.3.0 expands supported solid Union/CSG ingestion for mixed Part and wedge assemblies and multiple material groups. Supported transparent Glass Union workflows can keep Glass and opaque appearances in separate outputs. This does not make arbitrary Unions, all mixed geometry, or every Glass/material state compatible. Child Decal or Texture overlays and unreadable mesh content remain unsupported. Inspect each Preview; copied properties do not guarantee identical appearance in every place or lighting setup.

Confirmed outputs are remembered in local Studio plugin settings. A multi-output result stays together as one logical Assets record. This local library does not sync to the cloud or replace a backup of your editable source. MeshMogul does not automatically publish, update an existing Mesh AssetId, guarantee optimization, or convert arbitrary models.

## Find the right next step

- [See how the workflow works](https://morningforge.github.io/MeshMogul/how-it-works/)
- [Check supported inputs and limits](https://morningforge.github.io/MeshMogul/supported-inputs/)
- [Explore MeshMogul Foundations: 3D Building for the AI Era](https://morningforge.github.io/MeshMogul/guides/#foundations)
- [Write and inspect a reusable AI asset brief](https://morningforge.github.io/MeshMogul/guides/how-to-prompt-ai-for-roblox-3d-models/)
- [Prepare generated models for reuse](https://morningforge.github.io/MeshMogul/guides/proceduralmodel-assistant-output-to-mesh/)
- [Use Studio Texture Generator](https://morningforge.github.io/MeshMogul/guides/roblox-studio-texture-generator/)
- [Compare meshes before and after conversion](https://morningforge.github.io/MeshMogul/guides/compare-roblox-meshes-before-and-after/)
- [Read common questions](https://morningforge.github.io/MeshMogul/faq/)
- [Read release history](https://morningforge.github.io/MeshMogul/changelog/)
- [Report a bug or request a feature](https://github.com/MorningForge/MeshMogul/issues)

## Project and licensing

This public repository contains the website, documentation, and notices. MeshMogul plugin source is private and is not included or licensed by the website. Public access to this repository does not grant a license to reuse its code or artwork. See [website terms](https://morningforge.github.io/MeshMogul/legal/), [LICENSE.md](LICENSE.md), and [third-party notices](THIRD_PARTY_NOTICES.md). Third-party terms continue to apply.
