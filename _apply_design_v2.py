#!/usr/bin/env python3
"""Apply the editorial V2 shell to all public site pages.

Idempotent by design: generators can run first, then this script restores the
shared design classes/assets without touching editorial content.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SECTIONS = ("accessoires", "comparatifs", "guides", "marques", "modeles", "usages")
STATIC = (
    "a-propos/index.html",
    "contact/index.html",
    "mentions-legales/index.html",
    "methode-de-test/index.html",
    "transparence-affiliation/index.html",
)


def page_classes(rel: str) -> list[str]:
    if rel == "index.html":
        return ["design-v2", "design-home"]

    parts = Path(rel).parts
    section = parts[0]
    is_hub = len(parts) == 2 and parts[1] == "index.html"

    if section == "comparatifs":
        return ["design-v2", "design-hub", "design-comparison-hub"] if is_hub else ["design-v2", "design-comparison"]
    if section == "guides":
        return ["design-v2", "design-hub", "design-guide-hub"] if is_hub else ["design-v2", "design-guide"]
    if section == "modeles":
        return ["design-v2", "design-hub", "design-model-hub"] if is_hub else ["design-v2", "design-model"]
    if section == "marques":
        return ["design-v2", "design-hub", "design-brand-hub"] if is_hub else ["design-v2", "design-brand"]
    if section == "usages":
        return ["design-v2", "design-hub", "design-usage-hub"] if is_hub else ["design-v2", "design-usage"]
    if section == "accessoires":
        return ["design-v2", "design-hub", "design-accessory-hub"] if is_hub else ["design-v2", "design-accessory"]
    return ["design-v2", "design-static"]


def is_model_leaf(rel: str) -> bool:
    parts = Path(rel).parts
    return len(parts) == 3 and parts[0] == "modeles" and parts[-1] == "index.html"


def needs_home_model_polish(rel: str) -> bool:
    return rel == "index.html" or is_model_leaf(rel)


def needs_model_v3(rel: str) -> bool:
    return is_model_leaf(rel)


def merge_body_classes(html: str, wanted: list[str]) -> str:
    match = re.search(r"<body(?:\s+class=\"([^\"]*)\")?\s*>", html, flags=re.I)
    if not match:
        return html
    existing = (match.group(1) or "").split()
    classes = existing[:]
    for cls in wanted:
        if cls not in classes:
            classes.append(cls)
    replacement = '<body class="' + " ".join(classes) + '">'
    return html[: match.start()] + replacement + html[match.end() :]


def ensure_assets(html: str, rel: str) -> str:
    links = []
    if '/design-v2.css' not in html:
        links.append('  <link rel="stylesheet" href="/design-v2.css">')
    if '/design-v2-rollout.css' not in html:
        links.append('  <link rel="stylesheet" href="/design-v2-rollout.css">')
    if needs_home_model_polish(rel) and '/home-model-polish.css' not in html:
        links.append('  <link rel="stylesheet" href="/home-model-polish.css">')
    if needs_model_v3(rel) and '/model-pages-v3.css' not in html:
        links.append('  <link rel="stylesheet" href="/model-pages-v3.css">')
    if links:
        html = html.replace('</head>', "\n".join(links) + '\n</head>', 1)
    if '/design-v2.js' not in html:
        html = html.replace('</body>', '  <script src="/design-v2.js" defer></script>\n</body>', 1)
    return html


def public_pages() -> list[Path]:
    pages = [ROOT / "index.html"]
    for section in SECTIONS:
        base = ROOT / section
        if base.exists():
            pages.extend(sorted(base.rglob("index.html")))
    pages.extend(ROOT / rel for rel in STATIC)
    # Deduplicate while preserving deterministic order.
    return list(dict.fromkeys(pages))


def apply_page(path: Path) -> bool:
    if not path.exists():
        return False
    rel = path.relative_to(ROOT).as_posix()
    original = path.read_text(encoding="utf-8")
    html = merge_body_classes(original, page_classes(rel))
    html = ensure_assets(html, rel)
    if html == original:
        return False
    path.write_text(html, encoding="utf-8")
    print(f"✓ {rel}: {' '.join(page_classes(rel))}")
    return True


def main() -> None:
    changed = sum(apply_page(path) for path in public_pages())
    print(f"Editorial V2 applied: {changed} page(s) changed; {len(public_pages())} page(s) checked.")


if __name__ == "__main__":
    main()
