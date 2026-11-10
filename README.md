# MeshMogul

**Turn supported Roblox Studio builds into inspectable, publishable, reusable mesh assets.** MeshMogul keeps your original source, gives you a Preview to inspect, and helps you reuse confirmed results from a local Assets library.

> **1.2.1 site candidate:** Creator Store delivery is still awaiting verification. The candidate describes the admitted 1.2.1 product changes; it is not a statement that the Store listing already serves 1.2.1.

[Official website](https://morningforge.github.io/MeshMogul/) · [Creator Store listing](https://create.roblox.com/store/asset/126445067739142) · [Product guides](https://morningforge.github.io/MeshMogul/guides/) · [Compatibility](https://morningforge.github.io/MeshMogul/supported-inputs/) · [Report a bug or suggest a feature](https://github.com/MorningForge/MeshMogul/issues)

## What MeshMogul does

Use MeshMogul when you have supported Parts, MeshParts, or Models built in Studio and want a reusable visual mesh result without first moving the build into an external modeling application. Inspect the retained Preview, choose when to publish, then reuse confirmed mesh IDs from Assets in Studio.

The workflow is **Build → Preview → Publish → Remember → Reuse**. Publishing requires reviewing and manually running the generated command in Studio’s Command Bar. Preview approval and the publication handoff are deliberate creator actions. MeshMogul preserves the source build.

## Check compatibility first

MeshMogul supports specific inputs and appearance states. Unsupported descendants block the selected root instead of disappearing silently. Direct Union/CSG conversion, child Decal or Texture overlays, and unreadable mesh content are not supported. Inspect each Preview; copied properties do not guarantee identical appearance in every place or lighting setup.

Confirmed outputs are remembered in local Studio plugin settings. A multi-output result stays together as one logical Assets record. This local library does not sync to the cloud or replace a backup of your editable source. MeshMogul does not automatically publish, update an existing Mesh AssetId, guarantee optimization, or convert arbitrary models.

## Find the right next step

- [See how the workflow works](https://morningforge.github.io/MeshMogul/how-it-works/)
- [Check supported inputs and limits](https://morningforge.github.io/MeshMogul/supported-inputs/)
- [Browse practical Roblox Studio guides](https://morningforge.github.io/MeshMogul/guides/)
- [Read common questions](https://morningforge.github.io/MeshMogul/faq/)
- [Read release history](https://morningforge.github.io/MeshMogul/changelog/)
- [Report a bug or request a feature](https://github.com/MorningForge/MeshMogul/issues)

## Project and licensing

This public repository contains the website, documentation, and notices. MeshMogul plugin source is private and is not included or licensed by the website. Public access to this repository does not grant a license to reuse its code or artwork. See [website terms](https://morningforge.github.io/MeshMogul/legal/), [LICENSE.md](LICENSE.md), and [third-party notices](THIRD_PARTY_NOTICES.md). Third-party terms continue to apply.
