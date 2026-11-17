# AGENTROPOLIS ASDS-54 — Hybrid Cinematic Spatial Design Contract v0.1

Status: design-system proposal for reusable 3D blocking + AI video finishing; not a deployed renderer.

## Ownership and interfaces

ASDS-54 owns reusable spatial/cinematic tokens and shot contracts. VYBE-NOIR / Film District owns story, editorial decisions, shots and production artifacts. MATH54 owns measurements and reproducibility. CREATOR-CORE / CONSTRUCTION can consume the same contracts for buildings, films, games and worlds. 54-T gates third-party models, external tools and publishing. The distribution layer publishes only rights-cleared approved artifacts.

## Canonical shot document

Each shot JSON must contain:
- shot_id, project_id, sequence_id, duration_s, fps_target, aspect_ratio, unit_scale_m, world_coordinate_system
- scene_assets with asset IDs, rights and source hashes
- camera sensor_width_mm, focal_length_mm, position_m, quaternion_xyzw, focus_distance_m, aperture_f
- blocking character IDs, transforms and time-indexed poses
- lights type, color_temperature_K, energy, positions, orientation, volumetric_density
- materials with base_color, metallic, roughness, normal maps, texture source hashes
- animation camera and character keyframes, interpolation and motion constraints
- output render passes (beauty, depth, normal, object-ID, motion vectors, alpha), colorspace and exposure
- AI finishing model identifier, version, seed, prompts, source frame hashes, output hashes, licensing and rights review
- QC gates, evidence receipts, approval state and distribution rights

## Quantitative rules

Camera horizontal field of view: theta = 2 atan(sensor_width_mm / (2 focal_length_mm)).
Trajectory smoothness: J = integral ||d^3 position/dt^3||^2 dt; use as soft optimization, not mandatory straightening of deliberate cuts.
Temporal error: E = alpha E_identity + beta E_pose + gamma E_material; define normalized metrics and calibrate weights on approved project shots.
Projection and occlusion: preserve world coordinates, scene depth and stable camera transforms across 3D blocking, AI finishing and composites.
Lighting: energy-conserving PBR / rendering-equation-based materials; no claim of inferred physical lighting values from the reference screen recording.
Motion: time samples use presentation timestamps; never equate nominal capture frame rate to native film frame rate.

## Reference 001

Source: a user-supplied screen recording of a cinematic reference, not an original film master.
Capture sha256: c6c011f2a91a81d16bc89e8772a8d5e0e1652a9833d9de7b1c28e2b17a7660a5.
Measurement CSV sha256: 8902d80f3193195e94247c524ca7f84196b397613903fa16e091496810484fcb.
Measurement data: VYBE-NOIR `data/film54/reference-001/metrics.csv`, 47 timestamped samples.
The recording is 1080 x 2340 and 24.600589 seconds. ROI statistics include screen UI and are not reference master luminance.
**Do not train on or redistribute third-party video** without explicit rights. Measurement-only features and design principles are not an authorization to copy a creator's film.

## Build pipeline

1. Storyboard / scene graph -> create versioned shot JSON.
2. Generate proxy geometry and staging in Blender/Three.js; lock camera and actor paths.
3. Render blocking plates + depth, normals, motion vectors, masks, frame/time manifests.
4. Apply approved AI video enhancement to the source-pinned plates; preserve provenance.
5. Reproject, composite, grade, and verify temporal coherence against plates.
6. MATH54 computes camera consistency, frame discontinuities, identity/material stability, perceptual quality and artifact metrics.
7. Human director approves; 54-T/rights checks gate any public distribution.
8. Export approved shot package to VYBE-NOIR and other district consumers through versioned interfaces.

## Initial tests

- Schema validation and unique shot IDs.
- Valid focal length, nonnegative duration, normalized quaternion, monotonic timestamps.
- Stable projected object coordinates under locked camera; frame alignment with source plates.
- Color pipeline metadata and complete render-pass provenance.
- Explicit FAIL/PENDING for missing rights, missing source hashes, absent model licenses, or unapproved distribution.
- CPU-first reference measurement and lightweight Blender Eevee preview; optional cloud rendering with approved provider, budget cap and receipts.

## Next implementation

Implement JSON schema, one Blender scene export, a Three.js preview consumer, a reference fixture, and a CI validator. The current document is the contract, not proof those components are implemented.
