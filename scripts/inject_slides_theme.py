#!/usr/bin/env python3
"""Inject GW site ink+teal theme into a marimo-exported HTML slides file.

Forces marimo dark mode (export often bakes theme=light) and remaps semantic
tokens to the site ink field so the deck does not render as a white island.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

THEME_BLOCK = """
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap"
  rel="stylesheet"
/>
<script id="gw-slides-force-dark">
  // Marimo reads display.theme from the embedded config; also stamp dark classes
  // before paint so light-dark() / .dark token sheets resolve to the dark branch.
  document.documentElement.classList.add("dark", "dark-theme");
  document.documentElement.style.colorScheme = "dark";
  document.documentElement.setAttribute("data-theme", "dark");
  document.addEventListener("DOMContentLoaded", function () {
    document.body.classList.add("dark", "dark-theme");
    document.body.style.colorScheme = "dark";
    document.body.setAttribute("data-theme", "dark");
  });
</script>
<style id="gw-slides-theme">
  :root,
  .dark,
  .dark-theme,
  .marimo {
    color-scheme: dark;
    --ink: #0a0e12;
    --ink-elevated: #121820;
    --ink-muted: #1a222d;
    --text: #e6ebe8;
    --text-muted: #9aa8a0;
    --text-faint: #6b7a72;
    --accent: #3dcfb6;
    --accent-dim: #2a9a88;
    --accent-glow: rgba(61, 207, 182, 0.18);
    --border-site: rgba(230, 235, 232, 0.08);

    --marimo-text-font: "IBM Plex Sans", "Segoe UI", system-ui, sans-serif;
    --marimo-heading-font: "Fraunces", "Source Serif 4", Georgia, serif;
    --marimo-monospace-font: "IBM Plex Mono", ui-monospace, monospace;

    --background: #0a0e12 !important;
    --foreground: #e6ebe8 !important;
    --card: #121820 !important;
    --card-foreground: #e6ebe8 !important;
    --muted: #1a222d !important;
    --muted-foreground: #9aa8a0 !important;
    --popover: #121820 !important;
    --popover-foreground: #e6ebe8 !important;
    --border: rgba(230, 235, 232, 0.08) !important;
    --primary: #3dcfb6 !important;
    --primary-foreground: #0a0e12 !important;
    --secondary: #1a222d !important;
    --secondary-foreground: #e6ebe8 !important;
    --accent-foreground: #0a0e12 !important;
    --cm-background: #121820 !important;
  }
  html, body, #root, .marimo {
    background: #0a0e12 !important;
    color: #e6ebe8 !important;
    font-family: var(--marimo-text-font) !important;
  }
  h1, h2, h3, h4, h5, h6 {
    font-family: var(--marimo-heading-font) !important;
    color: #e6ebe8 !important;
    font-weight: 500;
  }
  .paragraph, .markdown, .prose, .prose *,
  [class*="markdown"], [class*="prose"] {
    color: #e6ebe8 !important;
  }
  a { color: #3dcfb6 !important; }
  code, pre, .cm-editor {
    font-family: var(--marimo-monospace-font) !important;
  }
  img {
    max-width: 100%;
    height: auto;
    border-radius: 2px;
  }
  .bg-background, .bg-primary, .bg-secondary, .bg-card, .bg-muted,
  [class*="bg-background"], [class*="bg-card"],
  [data-theme="light"], .light {
    background-color: #0a0e12 !important;
    color: #e6ebe8 !important;
  }
</style>
""".strip()

MARKER_START = "<!-- gw-slides-theme:start -->"
MARKER_END = "<!-- gw-slides-theme:end -->"


def force_dark_theme_config(html: str) -> str:
    """Rewrite baked marimo display.theme light → dark in the export payload."""
    updated, n = re.subn(
        r'("theme"\s*:\s*")light(")',
        r"\1dark\2",
        html,
        count=4,
    )
    if n:
        print(f"Rewrote theme=light → dark ({n} occurrence(s))")
    return updated


def inject(html_path: Path) -> None:
    html = force_dark_theme_config(html_path.read_text(encoding="utf-8"))
    block = f"{MARKER_START}\n{THEME_BLOCK}\n{MARKER_END}"

    if MARKER_START in html and MARKER_END in html:
        before, rest = html.split(MARKER_START, 1)
        _, after = rest.split(MARKER_END, 1)
        html = before + block + after
    elif "</head>" in html:
        html = html.replace("</head>", f"{block}\n</head>", 1)
    else:
        html = block + "\n" + html

    html_path.write_text(html, encoding="utf-8")
    print(f"Injected theme into {html_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="Path to marimo-exported index.html")
    parser.add_argument("--talk", default="", help="Talk slug (informational only)")
    args = parser.parse_args()
    if not args.html.is_file():
        raise SystemExit(f"Missing HTML: {args.html}")
    inject(args.html)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
