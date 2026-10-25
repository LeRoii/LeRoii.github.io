# Design QA

- Source visual truth: `/Users/leroi/.codex/generated_images/01a17217-dbfb-7dc3-aa10-6ced2b6f4205/exec-fcd47386-65f5-4489-9093-ee9a61ee5d1a.png`
- Browser-rendered implementation: `qa/home-desktop.png`
- Side-by-side comparison: `qa/home-comparison-pass2.png`
- Additional evidence: `qa/home-mobile.png`, `qa/archive-desktop.png`, `qa/lecture-desktop.png`, `qa/lecture-mobile.png`
- Desktop viewport: 1440 × 1024 CSS px, device scale factor 1
- Mobile viewport: 390 × 844 CSS px, device scale factor 1
- Source pixels: 1486 × 1059
- Implementation pixels: 1440 × 1024
- Comparison normalization: both images scaled to 720 px width, top-aligned and padded to 720 × 520, then combined side by side
- State: initial page load, no hover or focus state

## Findings

No actionable P0, P1, or P2 findings remain.

- Fonts and typography: the source's editorial serif hierarchy is preserved with Songti/STSong/Noto Serif fallbacks, and supporting UI copy uses a compact sans/mono hierarchy. The lecture title now wraps only at a semantic boundary.
- Spacing and layout rhythm: desktop content starts at the same approximate left boundary as the reference; the removed right column remains empty; the homepage footer is suppressed; the 12 px button radius follows the user's rounded-rectangle instruction.
- Colors and visual tokens: warm ivory paper, near-black headings, electric blue links/actions, muted blue-gray text, and amber title punctuation match the selected direction with sufficient contrast.
- Image quality and asset fidelity: the implementation intentionally uses the lecture's real vector LED circuit instead of the reference mock's transistor sketch. It remains sharp at desktop and mobile sizes and directly represents the published material.
- Copy and content: the homepage labels, chapter names, summaries, and archive section reflect the actual site content. No placeholder copy remains.
- Responsiveness and accessibility: 390 px captures show no horizontal page overflow. Navigation, primary action, archive links, and chapter links are keyboard-reachable anchors with visible focus styling; decorative marks are hidden from assistive technology and the circuit image has alternative text.

## Full-view comparison evidence

The source and implementation are shown together in `qa/home-comparison-pass2.png`. The primary grid, editorial hierarchy, chapter rows, large right-side whitespace, color balance, and above-the-fold density align. The implementation's circuit graphic is an intentional content-specific substitution.

## Focused evidence

Separate captures were used because the source contains only the desktop homepage:

- `qa/lecture-desktop.png`: article typography, table treatment, title wrapping, and 800 px reading measure.
- `qa/home-mobile.png`: stacked hero, full-width rounded-rectangle button, chapter rows, and absence of the removed homepage footer.
- `qa/lecture-mobile.png`: mobile title wrapping, simplified breadcrumb, and table containment.
- `qa/archive-desktop.png`: preserved historical posts in the new “过往资料” section.

## Comparison history

1. Initial comparison found a P2 horizontal alignment mismatch: the implementation used a 1200 px shell and sat farther from the left edge than the reference. It also retained the removed footer on the mobile homepage. Fixed by widening the shell to 1312 px, tightening the hero gap, and hiding the footer only on the homepage. Post-fix evidence: `qa/home-comparison-pass2.png` and `qa/home-mobile.png`.
2. Article inspection found a P2 title-wrap problem where “第1-3章” split after the hyphen. Fixed with a non-breaking semantic span. Post-fix evidence: `qa/lecture-desktop.png`.
3. Mobile inspection found a P2 breadcrumb wrap that repeated the long page title and left “章）” alone on a line. Fixed by showing only the section return link below 720 px. Post-fix evidence: `qa/lecture-mobile.png`.

## Primary interactions tested

- “阅读讲义” opens `/workshop/electronics-foundations/`.
- “过往资料” opens `/archive/`.
- “电子创新工作室资料” opens `/workshop/`.
- The first chapter row opens the lecture at its chapter anchor.
- All tested pages returned HTTP 200; browser console errors and failed requests: none.

## Follow-up polish

- P3: the reference includes a search icon, but search was intentionally omitted because no search behavior was requested. It can be added later when the archive grows.

final result: passed
