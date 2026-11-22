# ASDS54 Hybrid Cinematic Shot Standard v0.1

**Blender directs; the AI video provider interprets.** The AI output is not a texture overlay on the 3D frame and should not be evaluated for pixel-exact overlap.

The canonical data contract is `contracts/hybrid-shot.v0.1.schema.json`. It describes an individual shot and does not grant permission to issue an inference request.

Sequence: **original creative intent → Blender blocking (set/stand-ins/camera) → raw layout → blurred grayscale composition reference → identity/wardrobe/environment references → governed Hermes video handoff → audio-first conform → verification receipt**.

## Reusable design rules

- 3D source specifies lens, camera elevation, framing, positions and motion. Stand-ins are rough controls, not final character models.
- Blur/grayscale reference is explicitly **composition only**. The AI result may differ spatially; reveal transitions use a soft wipe, not a misleading exact-match split.
- Maximum five references per shot *subject to actual provider limits*. Portrait and wardrobe references are locked to approved entity identities.
- Lighting and never-list are part of each shot contract. No dialogue when `no_dialogue=true`.
- Audio is established before edit timing; cinematic finishing targets 1080p delivery and -14 LUFS, with measured verification rather than presumed conformance.
- ASDS54 palette defaults: Obsidian `#0a0a12`, Cyan `#5ee9f0`, Red `#ee1b2e`, Cream `#f2f0ea`. This is presentation canon, not an AI model guarantee.
- Under the strict zero-additional-spend lane, a Hermes video generation request **cannot be executed** without verified included entitlement and per-request zero additional charge. Uncertain = block.
- A generated cinematic video is **not** proof of playable geometry. Interactive Three.js/Godot exports must rely on the underlying world graph, not the video frames.

## Ownership boundary

CREATOR-CORE owns creative intent. ENTITY54/WORLDQ own persistent world identity. ASDS54 owns design tokens and shot semantics. CONSTRUCTION builds and conforms. PARALLAX MCP verifies authorized scene edits and captures. POCKET consumes lightweight rendered media and native controls. AEGIS/VERITY/54T govern permissions and evidence.

Example shot manifest is maintained by CONSTRUCTION at `examples/identity-plaza-shot.json` as a consumer of this schema. Do not fork the canonical schema into applications.
