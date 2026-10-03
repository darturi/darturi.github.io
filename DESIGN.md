---
name: Daniel Aarao Reis Arturi Portfolio
description: A cool archival evidence ledger for research, engineering, and independently inspectable work.
colors:
  signal-cobalt: "#0755F5"
  filter-cobalt: "#1F63D8"
  relation-red: "#C9211E"
  selected-wash: "#FFF1F2"
  hover-wash: "#EEF4FF"
  portrait-ground: "#EDF1F8"
  cool-paper: "#F7F8FA"
  midnight-ink: "#0A0C38"
  muted-ink: "#596286"
  annotation-ink: "#354069"
  column-ink: "#414B75"
  type-ink: "#303B68"
  origin-ink: "#1E2857"
  folio-ink: "#44517B"
  register-ink: "#36416D"
  reading-ink: "#333B65"
  ledger-rule: "#AEB8CF"
  ledger-rule-soft: "#D9DFEB"
typography:
  identity:
    fontFamily: "IBM Plex Sans Condensed, sans-serif"
    fontSize: "clamp(22px, 1.75vw, 28px)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.01em"
  display:
    fontFamily: "IBM Plex Sans Condensed, sans-serif"
    fontSize: "clamp(58px, 6.7vw, 96px)"
    fontWeight: 600
    lineHeight: 0.86
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "IBM Plex Sans Condensed, sans-serif"
    fontSize: "clamp(42px, 4.3vw, 68px)"
    fontWeight: 600
    lineHeight: 0.92
    letterSpacing: "-0.035em"
  section-headline:
    fontFamily: "IBM Plex Sans Condensed, sans-serif"
    fontSize: "clamp(42px, 4vw, 64px)"
    fontWeight: 600
    lineHeight: 0.95
    letterSpacing: "-0.035em"
  title:
    fontFamily: "IBM Plex Sans Condensed, sans-serif"
    fontSize: "clamp(19px, 1.6vw, 26px)"
    fontWeight: 500
    lineHeight: 1.08
  pursuit-title:
    fontFamily: "IBM Plex Sans Condensed, sans-serif"
    fontSize: "clamp(22px, 1.9vw, 30px)"
    fontWeight: 600
    lineHeight: 1.03
    letterSpacing: "-0.02em"
  lead:
    fontFamily: "IBM Plex Sans Condensed, sans-serif"
    fontSize: "clamp(19px, 1.55vw, 25px)"
    fontWeight: 400
    lineHeight: 1.3
  body:
    fontFamily: "IBM Plex Sans Condensed, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.45
  action:
    fontFamily: "IBM Plex Sans Condensed, sans-serif"
    fontSize: "clamp(11px, 0.7vw, 12px)"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.08em"
  label:
    fontFamily: "IBM Plex Sans Condensed, sans-serif"
    fontSize: "clamp(11px, 0.75vw, 12px)"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.18em"
  kind-stamp:
    fontFamily: "IBM Plex Sans Condensed, sans-serif"
    fontSize: "clamp(28px, 2.6vw, 40px)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.03em"
rounded:
  square: "0px"
  relation-trace: "10px"
spacing:
  hairline: "1px"
  xxs: "4px"
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "32px"
components:
  evidence-action:
    backgroundColor: "transparent"
    textColor: "{colors.signal-cobalt}"
    typography: "{typography.action}"
    rounded: "{rounded.square}"
    padding: "0.55rem 0.75rem"
    height: "39px"
  evidence-action-related:
    backgroundColor: "transparent"
    textColor: "{colors.relation-red}"
    typography: "{typography.action}"
    rounded: "{rounded.square}"
    padding: "0.55rem 0.75rem"
    height: "42px"
  filter-active:
    backgroundColor: "{colors.filter-cobalt}"
    textColor: "{colors.cool-paper}"
    typography: "{typography.body}"
    rounded: "{rounded.square}"
    padding: "0 0.75rem"
  current-pursuit:
    backgroundColor: "{colors.cool-paper}"
    textColor: "{colors.midnight-ink}"
    typography: "{typography.pursuit-title}"
    rounded: "{rounded.square}"
    padding: "1.4rem 1rem 1.4rem 0"
  portrait-placeholder:
    backgroundColor: "{colors.portrait-ground}"
    textColor: "{colors.annotation-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.square}"
  register-row:
    backgroundColor: "{colors.cool-paper}"
    textColor: "{colors.midnight-ink}"
    rounded: "{rounded.square}"
    padding: "1rem 0"
  related-record-disclosure:
    backgroundColor: "transparent"
    textColor: "{colors.signal-cobalt}"
    typography: "{typography.action}"
    rounded: "{rounded.square}"
    padding: "0.18rem 0"
  related-record-preview:
    backgroundColor: "rgba(238, 244, 255, 0.52)"
    textColor: "{colors.midnight-ink}"
    rounded: "{rounded.square}"
  evidence-drawer:
    backgroundColor: "{colors.cool-paper}"
    textColor: "{colors.midnight-ink}"
    rounded: "{rounded.square}"
    padding: "2rem 2.4rem"
---

# Design System: Daniel Aarao Reis Arturi Portfolio

## Overview

**Creative North Star: "The Evidence Ledger"**

The Evidence Ledger treats a professional portfolio as an open archival index: cool paper, midnight ink, fine rules, semantic kind stamps, and explicit detail controls. Its authority comes from structure and specificity rather than decoration. The mood is academic, restrained, editorial, and technically exact.

The opening behaves like a working portrait within that archive. An About pane establishes Daniel's combined research and engineering identity, while a Current Work pane gives two live pursuits direct routes into their detail views. A pale cobalt line-only wireframe ribbon twists across the full introduction as a quiet architectural signature. The work-and-research index remains the exhaustive collection below, so the introduction provides orientation without duplicating it.

The system supports broad perusal. Research, publications, engineering, experience, and education remain independently inspectable, while reference-colored transit traces identify only verified relationships. A filtered row can disclose a hidden counterpart without duplicating the register or weakening the canonical destination. The visual language is intentionally light and rejects the former warm, rounded, card-led aesthetic as well as any purely dark presentation.

**Key Characteristics:**

- Cool, nearly white paper with dense blue-black typography.
- A two-pane working portrait followed by a ruled, open work-and-research index.
- A barely-there procedural wireframe ribbon of crisp cobalt paths, anchored across the full introduction.
- Cobalt for navigation and detail access; red only for verified relationships.
- Bidirectional filtered relationships that always lead back to canonical entries.
- Square controls and flat surfaces with no decorative gradients or soft cards.
- Desktop density that becomes a deliberate linear reading order on mobile.

## Colors

The palette resembles a technical archive marked with blue indexing ink and one restrained red cross-reference pencil.

### Primary

- **Signal Cobalt:** Primary links, semantic kind stamps, portrait registration marks, outlines, and detail actions.
- **Filter Cobalt:** The stronger selected state used behind active category filters.

### Secondary

- **Relation Red:** Reserved for verified role-to-output relationships, their routes, and selected detail actions.
- **Selected Wash:** A barely tinted ground behind related rows; never a free-standing decorative panel.
- **Hover Wash:** A cool-blue response for evidence rows and linked register groups.

### Neutral

- **Cool Paper:** The single continuous page and drawer surface.
- **Portrait Ground:** A cool archival image field inside the placeholder frame.
- **Midnight Ink:** Headlines, primary record text, and the strongest reading voice.
- **Muted Ink:** Supporting prose, affiliations, and secondary metadata.
- **Annotation, Column, Type, Origin, Folio, Register, and Reading Inks:** Closely related cool-blue text roles that preserve hierarchy at high density.
- **Ledger Rule / Soft Ledger Rule:** Structural and subordinate one-pixel dividers.

### Named Rules

**The Verified Red Rule.** Relation Red appears only where a real role-to-output or role-to-project relationship has been established; it is not a generic emphasis color. Cobalt carries the remaining verified routes.

**The Continuous Paper Rule.** Major regions share Cool Paper. Separate them with rules and spatial bands, never floating white cards.

## Typography

**Display Font:** IBM Plex Sans Condensed (with sans-serif fallback)

**Body Font:** IBM Plex Sans Condensed (with sans-serif fallback)

**Identity Font:** IBM Plex Sans Condensed (with sans-serif fallback)

**Character:** IBM Plex Sans Condensed carries the entire scholarly index efficiently without feeling like a terminal. Four self-hosted weights, 400, 500, 600, and 700, keep the identity stable without relying on network font delivery. The nameplate remains distinctive through scale and weight rather than a separate display face.

### Hierarchy

- **Identity** (600, responsive 22 to 28px, 1.0): The full-name masthead only.
- **Display** (600, responsive 58 to 96px, 0.86): The opening About statement.
- **Headline** (600, responsive 42 to 68px, 0.92): The Current Work heading.
- **Section Headline** (600, responsive 42 to 64px, 0.95): Work-index and foundations openings.
- **Title** (500, responsive 19 to 26px, 1.08): Work-index entries and detail titles.
- **Pursuit Title** (600, responsive 22 to 30px, 1.03): Current-work subjects.
- **Lead** (400, responsive 19 to 25px, 1.3): The first-person positioning statement.
- **Body** (400, 16px, 1.45): Explanations, metadata, and drawer reading copy.
- **Action** (600, responsive 11 to 12px, tracked uppercase): Compact outlined controls.
- **Label** (600, responsive 11 to 12px, widely tracked uppercase): Short column headings, folios, and detail-section labels only.
- **Kind Stamp** (600, responsive 22 to 34px, 1.0): Semantic entry kinds such as ROLE, PAPER, SYSTEM, STUDY, and DEGREE.

### Named Rules

**The Dense-but-Legible Rule.** Condensation provides density; body copy never borrows the extreme tracking or line height of labels and display type.

**The One-Family Rule.** The name, records, controls, and prose all use IBM Plex Sans Condensed. Hierarchy comes from scale, weight, spacing, and structural rules rather than an isolated signature face.

## Layout

The desktop opening is a full-viewport evidence ledger. A slim masthead and folio frame a 58% / 42% split: the wider About pane carries the introduction and a narrower 4:5 portrait frame, while the Current Work pane holds two ruled pursuits with direct detail buttons. The vertical divider is a structural part of the composition. The wireframe ribbon is absolutely positioned at `top: 0`, `left: 0`, `width: 58%`, and `height: 84.1vh`, with `preserveAspectRatio="none"`. The intro spread and the SVG both permit visible overflow at desktop widths, so this 58% viewport is a placement frame rather than a containment boundary. Desktop mesh mode multiplies every generated horizontal coordinate by `1 / .58`. Its upper and lower halves follow cubic Hermite curves through explicit top, waist, and bottom anchors. A shared waist tangent removes the visible corner where each longitude reverses sides, while shallow zero-slope bows of `18` and `20` units preserve the intended contour. The rendered top terminal extends from the left edge to roughly 30% of page width, the central waist sits about 54% down the section near the portrait's lower edge, and the bottom terminal remains anchored from about 51% to the far right. The exterior paths remain gently curved but visually close to straight. The work-and-research index below has a separate purpose: it contains every independently browsable entry, including unpaired work, with category filters and detail controls. Its header's first cell holds two opposing ruled planes derived from the geometric construction on E. M. Hartley's *Cartesian Geometry of the Plane*: an upper plane curves into a lower-left pinch and a lower plane reverses that bias into an upper-right pinch. The pinches remain cleanly separated across a small diagonal gap with no bridge strokes or overlap. The reference's black and mint block is translated into the site's unfilled cobalt drafting language.

The index is data-driven and relationship-grouped. The current research-scientist role, Lea system, and accepted Lea workshop paper lead as one verified group, followed by other role-to-output groups in priority order, then independent entries. The All view remains exhaustive and duplicate-free. In a category view, each canonical row can reveal verified counterparts hidden by that filter, including when multiple members of the group remain visible. Opening the disclosure reveals a compact, inward-tabbed preview beneath the row, and only one disclosure may be open at a time. Every member can reveal and locate its hidden counterparts. Filters change only the visible subset; they never rewrite an entry or invent a connection. Long titles may wrap, and publication or project additions should extend the index vertically without requiring a new composition.

The preview's locate action switches to the counterpart's primary category, renders the canonical destination there, scrolls it to the center, moves programmatic focus to the row, and briefly highlights it with the same route color. The preview is a locator, not a second detail view: details open only from the canonical row.

At the compact breakpoint (980px), the opening becomes a linear document. About copy comes first, Current Work comes second, and the portrait follows third so current work is not displaced by the image. The ribbon uses `top: 21%`, `right: -18%`, `left: auto`, `width: min(110vw, 440px)`, `height: auto`, `transform: rotate(-31deg)`, and `opacity: .58`. Below 769px, the breakpoint-aware mesh builder selects mobile mode and intentionally keeps its prior geometry: horizontal centerline controls `[70, 230, 250, 680]`, vertical controls `[0, 100, 360, 760]`, cosine twist, and unscaled coordinates. Current Work receives `17rem` top padding so the complete broad terminal, central pinch, and reversed reopening occupy their own white interlude without crossing primary copy. Pursuit actions become a two-column row, masthead links remain visible, work-index filters form a two-column matrix, and the details drawer fills the viewport. Related previews reduce their indentation, show the counterpart kind beside title and context, and place the locate action full width on its own row. Horizontal overflow is prohibited at 390px. Between 981px and 1120px, the five-column index tightens its fractional columns and gaps while remaining a desktop grid.

### Named Rules

**The Full-Spread Anchor Rule.** On desktop, keep the SVG viewport at `58%` by `84.1vh`, preserve visible overflow on both the intro spread and the SVG, and remap generated horizontal coordinates by `1 / .58`. The top terminal must reach roughly 30% of page width, the waist must fall about 54% down the section beside the portrait's lower edge, and the bottom terminal must remain anchored from about 51% to the far right.

**The White Interlude Rule.** On compact screens, reserve `17rem` above Current Work for the ribbon and keep its full broad-terminal, pinch, and reopening silhouette clear of primary copy.

## Elevation & Depth

The system is flat. One-pixel rules, subtle selected washes, and the book-like divider provide separation. There are no card shadows, glass layers, gradients, or ambient glows. The modal backdrop is the sole tonal depth cue, and the drawer is separated by a one-pixel edge shadow.

The opening divider enters through a 700ms clip-path reveal with the system's restrained acceleration curve. It reads as a rule being drawn, not as an object sliding onto the page. Related previews expand over 280ms while their transit route draws over 320ms after a 40ms delay. Located rows receive a 1.45-second inset color trace that resolves back to paper. Reduced-motion preferences collapse animations, transitions, and smooth scrolling to near-instant feedback.

### Named Rules

**The Rule-before-Shadow Rule.** Use a structural hairline before considering elevation. Shadows are reserved for the modal edge and nowhere else.

**The Drawn-Rule Rule.** Entrance motion may reveal a structural rule, but content remains stable and immediately legible.

## Shapes

The form language is square, typeset, and geometrically exact. Buttons, filters, rows, drawers, page regions, and the archival portrait frame use zero-radius corners. The portrait maintains a strict 4:5 ratio with an ink border, cobalt registration corners, and centered crosshairs until a photograph replaces it. Verified relationship routes are the deliberate exception: they use rounded turns and hollow circular station nodes inspired by transit diagrams. In filtered views, the route turns inward from the canonical row to a compact indented preview, representing a path between records rather than a generic component silhouette.

The signature architectural ribbon is a runtime-generated, line-only SVG in a 920 by 760 viewBox. Its deterministic surface collapses to a broad central turn and reopens with reversed orientation. Desktop geometry joins a top center of `142.5` with half-width `142.5`, a waist at `(330, 410)` with a `36`-unit half-height, and a bottom center of `680` with half-width `220` at `y = 760`. Cubic Hermite interpolation gives the upper and lower halves one shared tangent at the waist. Shallow `18`-unit and `20`-unit squared-sine bows have zero slope at every anchor, so the exterior lines retain their gentle contour without forming a corner at the twist. Mobile intentionally retains centerline controls `[70, 230, 250, 680]` and `[0, 100, 360, 760]`, its cosine twist, and unscaled coordinates. Desktop distortion is restrained to `0.018` for longitudes and `0.006` for rib offsets, while mobile retains `0.065` and `0.022`. The result is 17 longitude paths and 31 cross-rib paths with coherent cells. Two stronger outline paths with end caps establish the silhouette, while subtly offset terminal depth lines keep the broad ends spatially legible. Desktop horizontal coordinates are remapped by `1 / .58`, allowing the geometry to extend beyond its narrow SVG viewport while retaining the intended page-level anchors. It uses no fill, gradient, blur, or material imitation.

### Named Rules

**The Exact Geometry Rule.** Generate the signature from deterministic anchor geometry and clean non-scaling hairline paths. Desktop joins its top, waist, and bottom anchors with cubic Hermite curves, a shared waist tangent, and shallow zero-slope `18`-unit and `20`-unit bows. Mobile keeps controls `[70, 230, 250, 680]` and `[0, 100, 360, 760]`, cosine twist, and unscaled coordinates. Do not make the desktop outline ruler-straight or return it to an aggressive hook. Do not soften the result into gradients, blur, generic blobs, filled facets, or literal illustrative imitation.

**The Runtime Wireframe Rule.** Build the 920 by 760 signature at runtime from 17 warped longitudes, 31 curved cross-ribs, two outline paths with end caps, and offset terminal depth lines. Use the established 0.05, 0.14, 0.095, 0.12, and 0.18 opacity hierarchy at 0.8px, 0.9px, 0.72px, 0.78px, and 1.05px respectively, with no fill.

## Components

### Buttons

- **Shape:** Square outlined controls with compact padding and a minimum 39px desktop height.
- **Default:** Transparent Cool Paper, Signal Cobalt text, and a one-pixel cobalt border.
- **Related:** Relation Red replaces cobalt only for actions tied to a selected verified relationship.
- **Hover / Focus:** The outline color fills the control and text reverses to white; focus remains visibly equivalent to hover.

### Current Pursuits

- **Structure:** Two flat, ruled entries inside the Current Work pane, each with a title followed by a semantic kind and subject metadata, then a synopsis and direct detail actions.
- **State:** A nearly imperceptible cobalt wash appears on hover without lifting the row.
- **Actions:** Desktop controls occupy a narrow right column. At the compact breakpoint they become a full-width two-column row below the synopsis.

### Portrait Placeholder

- **Frame:** A square-cornered 4:5 archival window with a one-pixel Midnight Ink border.
- **Marks:** Signal Cobalt crosshairs and four registration corners indicate a deliberate image slot, not a generic empty state.
- **Caption:** Small uppercase annotation text records that the image is pending and should be replaced with a photograph.

### Architectural Wireframe Ribbon

- **Geometry:** Runtime JavaScript constructs 17 longitude paths, 31 cross-rib paths, two stronger outline paths with end caps, and subtle offset terminal depth lines against a 920 by 760 SVG viewBox. Desktop joins explicit top, waist, and bottom anchors with cubic Hermite curves, one shared waist tangent, and zero-slope `18`-unit and `20`-unit bows. Its longitude and rib distortion values are `0.018` and `0.006`. Mobile keeps controls `[70, 230, 250, 680]` and `[0, 100, 360, 760]`, its cosine twist, unscaled coordinates, and distortion values of `0.065` and `0.022`.
- **Line Hierarchy:** Signal Cobalt depth paths use 0.05 opacity at 0.8px. Terminal depth lines use 0.14 at 0.9px. Cross-ribs use 0.095 at 0.72px. Longitudes use 0.12 at 0.78px. Outline paths and end caps use 0.18 at 1.05px. Every mark is unfilled with rounded caps and joins.
- **Desktop Placement:** Use `top: 0`, `left: 0`, `width: 58%`, `height: 84.1vh`, and `preserveAspectRatio="none"`, with visible overflow on the parent intro spread and the SVG. Remap horizontal coordinates by `1 / .58`. The top terminal starts at the left edge and reaches roughly 30% of page width, the central waist sits about 54% down the section near the portrait's lower edge, and the bottom terminal stays anchored from about 51% to the far right. Preserve the shallow exterior bows between these anchors.
- **Compact Placement:** Use `top: 21%`, `right: -18%`, `left: auto`, `width: min(110vw, 440px)`, `height: auto`, `transform: rotate(-31deg)`, and `opacity: .58`. Keep the prior mobile geometry, cosine twist, and unscaled coordinates. Give Current Work `17rem` top padding so the full terminal, pinch, and reopening silhouette occupies a white interlude without crossing primary copy.
- **Behavior:** Deterministic at runtime and ignored by assistive technology. It is a spatial signature, not a separate illustration or content layer. Desktop and mobile generation are selected through a media-query listener so each mode rebuilds with its intended coordinate scale. Because its geometry depends on JavaScript execution, omit it from static sidecar previews instead of substituting an inaccurate sample.

### Register Field Study

- **Geometry:** A deterministic 180 by 240 line-only SVG with two opposing ruled planes, each built from thirteen warped contours and eleven cross-ribs. The upper and lower pinches are diagonally displaced, their curvature biases reverse, and a clean gap keeps the two meshes fully separate.
- **Scale:** Fill the complete first cell of the desktop index header with no inset. On compact layouts, fill a 112px-tall full-width divider band. The cell clips the planes cleanly at its own rules.
- **Line Hierarchy:** Signal Cobalt only, with ribs at 0.095 opacity, contours at 0.14, and outlines at 0.25. Use no fill, gradient, blur, label, count, unrelated seam lines, or motion.
- **Behavior:** Runtime-built, non-interactive, and hidden from assistive technology. It is decor only; live entry totals remain in the filter controls and status text.

### Filters

- **Style:** Full-width, square, text-and-count rows without pills or icons.
- **State:** Inactive filters remain transparent; the selected filter uses Filter Cobalt with white text.
- **Behavior:** Publications and broader research share one combined filter because publications are a subset of the research work. An entry may belong to multiple filters without being duplicated in the index. Counts must be derived from actual entry categories.

### Entries / Containers

- **Corner Style:** Square.
- **Background:** Continuous Cool Paper; a selected verified pair may use Selected Wash.
- **Border:** Soft one-pixel horizontal rules. Index rows do not become cards.
- **Content Behavior:** Kind, dates, title, context, and detail action remain separately scannable. Internal relationship codes never appear as visitor-facing labels.
- **Relationship Groups:** When two or more entries in a verified group are visible, keep them adjacent inside one lightly washed ledger band. A three-pixel route with hollow circular stations joins the rows from the margin, with one station centered on each visible row. The route follows actual row heights and disclosure expansion. The AI-safety relationship uses Relation Red; other routes use Signal Cobalt. When a category filter hides members, each visible entry remains canonical and can disclose its hidden counterparts beneath it.

### Related Work Disclosure

- **Trigger:** A canonical row in a category view adds an explicit uppercase type-specific control such as `Related role`, `Related paper`, or `Related system` only when a verified counterpart is hidden by the active filter. The All view adds no disclosure.
- **Expansion:** At most one disclosure is open. The compact preview sits beneath and inward from the canonical row, repeats only the counterpart's kind, title, and context, and uses the relationship's route color, station geometry, and subtle wash.
- **Destination:** `View [kind]` changes the active filter and lands on the canonical counterpart. It centers the row, moves focus to it, and briefly applies a route-colored locate trace.
- **Accessibility:** The trigger exposes its expanded state and controlled region. Collapsed preview content is both hidden from accessibility APIs and inert. Focus returns to the disclosure trigger after expansion or collapse. Reduced-motion preferences remove smooth scrolling and collapse all related transitions.
- **Responsive:** Desktop preserves an indented four-column preview. Compact layouts use reduced indentation, stacked metadata, and a full-width locate action.

### Navigation

The masthead is a horizontal identity strip with the full name, role, and four plain cobalt links: résumé, GitHub, LinkedIn, and contact. It is not sticky, translucent, or pill-based. At the compact breakpoint, the name, role, and link group become three measured rows rather than a hamburger menu.

### Evidence Drawer

The signature disclosure is a native modal dialog aligned to the right edge on desktop and full-width on mobile. It preserves complete source detail, supporting links, awards, and technical tags. Its entrance is a 42px rightward translation with a restrained opacity fade; reduced-motion preferences collapse transitions.

## Do's and Don'ts

### Do:

- **Do** keep every entry independently openable and every repeated action uniquely named for assistive technology.
- **Do** disclose verified counterparts hidden by a category filter and route visitors to the counterpart's canonical row.
- **Do** use the opening to orient visitors to identity and current work, then let the work-and-research index carry the exhaustive archive.
- **Do** lead with the current research-scientist role and Lea project, then keep verified role-to-output pairs adjacent before independent records; filters may expose any relevant subset.
- **Do** keep relationship codes internal, using them only to group verified role-to-output or role-to-project relationships.
- **Do** place Current Work before the portrait in the compact reading order.
- **Do** extend the register vertically when publications or roles are added.
- **Do** maintain the cool paper, midnight ink, cobalt, and rare relation-red hierarchy.
- **Do** preserve the wireframe ribbon's deterministic structure, 17 longitudes, 31 ribs, line-weight hierarchy, broad terminals, narrow throat, shallow desktop bows, desktop `1 / .58` horizontal coordinate remap, visible overflow, full-section terminal anchors, and the prior unscaled cosine-twist mobile mode.

### Don't:

- **Don't** reintroduce the warm cream, rounded-card, gradient, glass, blur, generic blob, or generic dark portfolio aesthetic.
- **Don't** turn red into a general-purpose accent or imply relationships that are not documented.
- **Don't** render related previews in the All view, duplicate detail actions inside previews, or leave collapsed preview controls focusable.
- **Don't** make one research niche dominate the entire portfolio; hierarchy comes from ordering, not exclusion.
- **Don't** duplicate the work-and-research index inside the opening or hide primary browsing behind a narrative sequence, carousel, or hamburger-only route.
- **Don't** expose internal relationship codes as visitor-facing taxonomy.
- **Don't** let a placeholder portrait outrank current work on compact screens.
- **Don't** shrink mobile controls into unlabeled arrows or permit horizontal scrolling.
- **Don't** add fills, gradients, blur, material imitation, literal building imagery, a pictorial scene, or an imitation of another visual reference to the architectural wireframe ribbon.
