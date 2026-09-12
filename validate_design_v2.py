#!/usr/bin/env python3
"""Fail when a public page falls out of the Editorial V2 shell."""
from pathlib import Path
from _apply_design_v2 import ROOT, needs_home_model_polish, needs_model_v3, public_pages, page_classes

CORE_ASSETS = ("/design-v2.css", "/design-v2-rollout.css", "/design-v2.js")
POLISH_ASSET = "/home-model-polish.css"
MODEL_V3_ASSET = "/model-pages-v3.css"


def main() -> None:
    errors: list[str] = []
    pages = public_pages()
    for path in pages:
        rel = path.relative_to(ROOT).as_posix()
        if not path.exists():
            errors.append(f"{rel}: missing page")
            continue
        html = path.read_text(encoding="utf-8")
        body_open = html.split("<body", 1)[1].split(">", 1)[0] if "<body" in html else ""
        for cls in page_classes(rel):
            if cls not in body_open.split('class="', 1)[-1]:
                errors.append(f"{rel}: missing body class {cls}")
        for asset in CORE_ASSETS:
            count = html.count(asset)
            if count != 1:
                errors.append(f"{rel}: expected one {asset}, found {count}")
        polish_count = html.count(POLISH_ASSET)
        expected_polish = 1 if needs_home_model_polish(rel) else 0
        if polish_count != expected_polish:
            errors.append(f"{rel}: expected {expected_polish} {POLISH_ASSET}, found {polish_count}")
        model_v3_count = html.count(MODEL_V3_ASSET)
        expected_model_v3 = 1 if needs_model_v3(rel) else 0
        if model_v3_count != expected_model_v3:
            errors.append(f"{rel}: expected {expected_model_v3} {MODEL_V3_ASSET}, found {model_v3_count}")

    if errors:
        print("EDITORIAL_V2: FAIL")
        for error in errors:
            print(f" - {error}")
        raise SystemExit(1)

    print(f"EDITORIAL_V2: PASS — {len(pages)} public pages covered")


if __name__ == "__main__":
    main()
