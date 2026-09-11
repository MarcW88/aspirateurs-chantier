#!/usr/bin/env python3
"""Validate /usages/ workflow governance and structural safety.

This is deliberately a machine floor, not an editorial/JTBD reviewer. It checks the
80/20 skill contract, provenance, required workflow files, known usage routes and draft
robots state. Substantive decisions remain in usage-analysis-workflow.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
STACK = ROOT / ".agents" / "skills" / "usage-skill-stack.json"
CONFIG = ROOT / "usage-workflow.config.yaml"
ANALYSIS = ROOT / ".agents" / "skills" / "usage-analysis-workflow" / "SKILL.md"
CONTENT = ROOT / ".agents" / "skills" / "usage-content-workflow" / "SKILL.md"

USAGE_SLUGS = [
    "aspirateur-atelier",
    "aspirateur-bois-sciure-copeaux",
    "aspirateur-bricolage-renovation",
    "aspirateur-gravats",
    "aspirateur-platre",
    "aspirateur-ponceuse",
    "aspirateur-scie",
]

errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

check(STACK.exists(), "missing usage-skill-stack.json")
check(CONFIG.exists(), "missing usage-workflow.config.yaml")
check(ANALYSIS.exists(), "missing usage-analysis-workflow/SKILL.md")
check(CONTENT.exists(), "missing usage-content-workflow/SKILL.md")

if STACK.exists():
    stack = json.loads(STACK.read_text(encoding="utf-8"))
    gov = stack.get("governance", {})
    shared_resp = gov.get("shared_responsibilities", [])
    custom_resp = gov.get("custom_responsibilities", [])
    total = len(shared_resp) + len(custom_resp)
    shared_ratio = len(shared_resp) / total if total else 0
    custom_ratio = len(custom_resp) / total if total else 1
    check(shared_ratio >= float(gov.get("target_shared_ratio_min", 0.8)), f"shared responsibility ratio too low: {shared_ratio:.1%}")
    check(custom_ratio <= float(gov.get("target_custom_ratio_max", 0.2)), f"custom responsibility ratio too high: {custom_ratio:.1%}")

    shared = stack.get("shared", [])
    custom = stack.get("custom", [])
    check(len(custom) == 2, f"expected exactly 2 custom usage orchestrators, got {len(custom)}")
    check({x.get("name") for x in custom} == {"usage-analysis-workflow", "usage-content-workflow"}, "custom usage skills must be exactly the two workflow orchestrators")

    for item in shared:
        name = item.get("name")
        check(bool(name), "shared skill without name")
        check(item.get("source_repo") == "MarcW88/bloc-notes-numerique", f"{name}: shared provenance must pass through MarcW88/bloc-notes-numerique")
        check(bool(item.get("source_sha")), f"{name}: missing source_sha provenance")
        skill_file = ROOT / ".agents" / "skills" / str(name) / "SKILL.md"
        check(skill_file.exists(), f"{name}: shared skill missing locally")

for path in [ANALYSIS, CONTENT]:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        check("source_repo: MarcW88/bloc-notes-numerique" in text, f"{path}: source workflow provenance missing")
        check('orchestration_target: ">=80% existing skills"' in text, f"{path}: 80/20 orchestration target missing")

for slug in USAGE_SLUGS:
    page = ROOT / "usages" / slug / "index.html"
    check(page.exists(), f"{slug}: usage page missing")
    if page.exists():
        html = page.read_text(encoding="utf-8")
        check('<meta name="robots" content="noindex, follow">' in html, f"{slug}: draft noindex/follow missing")
        h1_count = len(re.findall(r"<h1\b", html, flags=re.I))
        check(h1_count == 1, f"{slug}: expected exactly one H1, got {h1_count}")

if errors:
    print("USAGE_WORKFLOW: FAIL")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)

print("USAGE_WORKFLOW: PASS")
print(f" - shared responsibilities: {len(shared_resp)}/{total} ({shared_ratio:.1%})")
print(f" - custom responsibilities: {len(custom_resp)}/{total} ({custom_ratio:.1%})")
print(f" - shared skills with bloc-notes provenance: {len(stack.get('shared', []))}")
print(" - custom skills restricted to usage-analysis-workflow and usage-content-workflow")
print(f" - {len(USAGE_SLUGS)} usage drafts exist and remain noindex, follow")
print("NOTE: machine PASS is not an editorial/JTBD PASS; use usage-analysis-workflow / PUBLISH_REVIEW.")
