# ASDS54 ThemePack v0.1: Obsidian Signal

Canonical files: `contracts/theme-pack.v0.1.schema.json` and `themes/obsidian-signal.v0.1.json`.

This is an original **design specification**, not a claim of a universal Android launcher replacement or native WebMCP availability. A ThemePack declares local visual appearance across POCKET, web preview and separate cinematic exports. It does not grant device/agent authority or permit billable video calls.

## Visual system
Obsidian `#0a0a12`; cyan `#5ee9f0`; red `#ee1b2e`; cream `#f2f0ea`. Background, glow and foreground layers have signed depth values `0.05`, `0.12`, `-0.25` respectively. Foreground moves in the opposite direction. Pulsing glow: 70–100% opacity / 4000 ms. Smooth rotation-vector motion is clamped and attenuated. Reduced-motion user preference takes priority.

## Implementation and governance
- **POCKET:** independently buildable Android WallpaperService demo, settings for 0.5–2x strength, user-approved wallpaper chooser, non-spying widget and in-app icon tiles. No launcher takeover.
- **PARALLAX:** read-only preview-inspection adapter. Existing PARALLAX identity/mandate/policy/capture proof remains separate. Preview movement is not authorization.
- **CONSTRUCTION:** validation of ThemePack JSON, rights, prohibited spend and required settings before release.
- **Hermes:** optionally provide cinematic scene media only through preexisting included subscription usage verified to incur **$0 additional charge**. Unknown charge or allowance = stop, no top-ups or fallback providers.
- This v0.1 uses locally drawn geometric artwork; it does not contain or need third-party assets, GPUs, video generation or external runtime services. Browser preview uses a CSS/software representation and is not proof of an APK.

See `preview/obsidian-signal.html` for the read-only interactive preview. Same tokens and layer ordering, distinct platform-specific renderers.