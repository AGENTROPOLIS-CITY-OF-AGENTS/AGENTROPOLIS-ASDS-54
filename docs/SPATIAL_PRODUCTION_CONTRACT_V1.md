# ASDS-54 Spatial Production Contract v1
Status: proposed integration contract; NOT a claim of implemented runtime.

## Ownership and reuse
- ASDS-54 owns system-wide spatial interface, accessibility, rendering profiles, scene and asset contracts.
- AGENTROPOLIS-CREATOR is the existing Construction District and Foundry. Do not replace its generation, previews, packaging, rights tracking, or MCP workflows.
- AGENTROPOLIS-CREATOR-CORE owns shared creator runtime, provider adapters, semantic review, and provenance.
- AGENTROPOLIS-AGENT-MCP mediates tool access; 54-T security controls gate untrusted skills and execution.
- Scenario 3D OS is a candidate optional adapter; verify its actual upstream repository, license, capabilities and dependencies before installation. Do not imply it is installed.
- HERMES CITY, ROM RIOT, AGENTICtv, WORLDQ and other consumers adopt approved versioned contracts rather than copy-pasting renderer implementations.

## Spatial tokens (initial proposal)
```json
{
  "schema": "asds54.tokens.v1",
  "colors": {"obsidian": "#080B10", "red": "#E11932", "cyan": "#00D9F5", "tennisLime": "#B8F53C"},
  "navigation": {"primary": "immersive-city", "fallback": "accessible-lite", "buildingEntry": "explicit-user-action"},
  "accessibility": {"reducedMotion": true, "keyboardNavigation": true, "screenReaderAlternative": true, "sensoryControl": true}
}
```
Values are design proposals, not recovered existing canonical token values. Reconcile against existing district design assets before adoption.

## Asset manifest
Every exported asset SHOULD include:
- asset_id, version, creator, source_uri, content_sha256, license_id, rights_evidence_uri
- format (glb/gltf/usdz/other), coordinate_system, units, dimensions
- triangle_count, texture_bytes, animation_clips, rig_type, collision_policy
- lod_variants, target_profiles, accessibility_alternative
- source_tool, adapter_version, review_status, provenance_receipt_id
Unknown fields remain null and block promotion when required by target policy. Never invent licenses or receipts.

## Device quality profiles
- mobile-low: progressive loading, constrained geometry/textures, reduced effects
- desktop-standard: balanced lighting and interactive scene
- tv-remote: focus navigation, readable controls, remote-only operation
- xr-comfort: comfort locomotion, frame-rate guardrails, gesture fallback
- lite-accessible: 2D functional equivalent, keyboard and assistive technology support
Performance thresholds are device-tested and must not be fabricated as universal constants.

## Governed production corridor
Intent -> CREATOR prompt contract -> CREATOR-CORE adapter selection -> AGENT-MCP permission gate -> isolated tool execution -> asset export -> Math54 geometry/performance validation -> rights/provenance review -> ASDS-54 contract validation -> preview/diff -> human approval -> versioned publish -> receipt/audit.

No automatic remote code installation, privileged shell access, secrets in prompts, production publish, or external billing without explicit approvals. Prefer local Blender/Godot/free tools when technically viable; do not claim all workloads cost $0.

## Scenario capability mapping (candidate, unverified)
Art/previs -> CREATOR storyboards.
Modeling -> Foundry asset generation.
Animation -> rigging/motion workflows.
Look development -> materials and lighting.
Worlds -> spatial scene assembly.
Pipeline -> retopology/UV/exports.
Expert tools -> guarded AGENT-MCP adapters.
Before integrating, inventory existing skills and compare feature-by-feature; add only missing adapters.

## Acceptance gates
1. Inventory existing ASDS-54, CREATOR, CREATOR-CORE and consumer code; identify authoritative implementations.
2. Confirm upstream Scenario URL/license and enumerate actual skills.
3. Validate manifest schema and at least one real GLB scene with reproducible test.
4. Test city entry/exit, remote/keyboard navigation, reduced-motion and fallback.
5. Benchmark mobile, desktop, TV and XR on actual target hardware.
6. Verify provenance, permissions, rollback and audit receipts.
7. Merge only after repository-required CI and human review.
