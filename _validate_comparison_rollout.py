#!/usr/bin/env python3
"""Semantic and anti-template gate for the comparison cluster.

The validator protects intent boundaries and core safety rules for every draft. Stronger
functional anti-template checks apply when pages claim READY_FOR_HUMAN_VALIDATION: a
READY cluster cannot merely rename H2s while recycling the same editorial cadence.
"""
from pathlib import Path
from collections import defaultdict
import json
import re

BASE = Path(__file__).resolve().parent
REWRITTEN = [
    "aspirateur-industriel",
    "aspirateur-chantier-puissant",
    "meilleur-aspirateur-de-chantier",
    "aspirateur-classe-m",
    "aspirateur-chantier-sans-fil",
    "aspirateur-eau-poussiere",
    "aspirateur-chantier-sans-sac",
    "petit-aspirateur-de-chantier",
]
ALL = ["aspirateur-professionnel"] + REWRITTEN
READY = "READY_FOR_HUMAN_VALIDATION"
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def html(slug):
    return (BASE / "comparatifs" / slug / "index.html").read_text(encoding="utf-8")


def data(slug):
    return json.loads((BASE / ".content" / "comparisons" / f"{slug}.json").read_text(encoding="utf-8"))


def editorial_body(slug):
    h = html(slug)
    match = re.search(r"<!-- COMPARISON_CONTENT_START -->(.*?)<!-- COMPARISON_CONTENT_END -->", h, flags=re.S)
    body = match.group(1) if match else h
    body = re.split(r'<h2\b[^>]*id=["\']sources["\'][^>]*>', body, maxsplit=1, flags=re.I)[0]
    return body


def functional_signature(slug):
    """Return the ordered editorial component cadence, ignoring wording/labels."""
    body = editorial_body(slug)
    token_re = re.compile(
        r'(?P<answer><div\b[^>]*class=["\'][^"\']*answer-box[^"\']*["\'][^>]*>)'
        r'|(?P<decision><section\b[^>]*class=["\'][^"\']*comparison-decision-module[^"\']*["\'][^>]*>)'
        r'|(?P<h2><h2\b[^>]*>)'
        r'|(?P<h3><h3\b[^>]*>)'
        r'|(?P<table><table\b[^>]*>)'
        r'|(?P<ul><ul\b[^>]*>)',
        flags=re.I,
    )
    mapping = {"answer": "A", "decision": "D", "h2": "H2", "h3": "H3", "table": "T", "ul": "L"}
    return tuple(mapping[m.lastgroup] for m in token_re.finditer(body))


def normalized_long_paragraphs(slug):
    paras = []
    for raw in re.findall(r"<p\b[^>]*>(.*?)</p>", editorial_body(slug), flags=re.S | re.I):
        text = re.sub(r"<[^>]+>", " ", raw)
        text = re.sub(r"\s+", " ", text).strip().lower()
        if len(text.split()) >= 40:
            paras.append(text)
    return paras


for slug in ALL:
    h = html(slug)
    d = data(slug)
    check('<meta name="robots" content="noindex, follow">' in h, f"{slug}: noindex/follow changed")
    check(d.get("notes", {}).get("affiliate_commission_used_in_ranking") is False, f"{slug}: affiliate independence missing")
    editorial = d.get("editorial", {})
    check(editorial.get("workflow_contract_version") == 2, f"{slug}: comparison workflow contract v2 missing")
    check(editorial.get("generator_role") == "shell_and_components_only", f"{slug}: generator role is not constrained")
    check(editorial.get("publish_review") in {READY, "REQUIRES_WORKFLOW_RERUN"}, f"{slug}: invalid publish-review state")

for slug in REWRITTEN:
    h = html(slug)
    d = data(slug)
    check(d.get("status") == "REWRITTEN_AFTER_CLUSTER_AUDIT", f"{slug}: rollout status missing")
    check(d.get("notes", {}).get("scoring_used") is False, f"{slug}: scoring must be disabled")
    check("Score ajusté" not in h and "Notre classement 2026" not in h, f"{slug}: legacy ranking language remains")
    check("scores" not in d and "ranking" not in d, f"{slug}: legacy score/ranking fields remain")
    check(len(d.get("recommendation_logic", [])) >= 3, f"{slug}: insufficient scenario/trade-off logic")
    check(all(r.get("main_tradeoff") for r in d.get("recommendation_logic", [])), f"{slug}: recommendation without trade-off")

industrial = html("aspirateur-industriel")
for needle in ["IVC 60/24-2", "IVR 60/30", "S3 L100", "VHO200", "process"]:
    check(needle.lower() in industrial.lower(), f"industrial: missing industrial-universe marker {needle}")
check("NT 50/1 Tact Te M ACD</strong></td>" not in industrial, "industrial: legacy NT50 ranking remains")

powerful = html("aspirateur-chantier-puissant")
check("ne crée volontairement pas de podium" in powerful, "powerful: measurement-comparability caveat missing")
check("à la turbine" in powerful, "powerful: measurement-point context missing")
check("/guides/depression-kpa-mbar-air-watt/" in powerful, "powerful: technical handoff missing")

general = html("meilleur-aspirateur-de-chantier")
for path in [
    "/comparatifs/aspirateur-classe-m/",
    "/comparatifs/aspirateur-chantier-sans-fil/",
    "/comparatifs/aspirateur-eau-poussiere/",
    "/comparatifs/aspirateur-chantier-puissant/",
    "/comparatifs/aspirateur-industriel/",
]:
    check(path in general, f"general: missing specialist handoff {path}")
check("gagnant universel" in general.lower(), "general: umbrella decision framing missing")

class_m = data("aspirateur-classe-m")
check(len(class_m.get("product_universe", [])) >= 5, "class M: candidate coverage still too narrow")
for item in class_m.get("product_universe", []):
    check("m" in str(item.get("role", "")).lower() or "m" in str(item.get("name", "")).lower() or item.get("id") in {"karcher-nt-30-1-tact","bosch-gas-35-m-afc","makita-vc4210mx","festool-ctm-midi-ac","bosch-gas-18v-12-mc"}, f"class M: unexpected candidate {item.get('id')}")
class_m_html = html("aspirateur-classe-m")
check("pré-requis" in class_m_html.lower() or "prérequis" in class_m_html.lower() or "point d’entrée" in class_m_html.lower(), "class M: certification gate framing missing")

cordless = html("aspirateur-chantier-sans-fil")
for needle in ["DeWalt DCV586M", "GAS 18V-12 MC", "GAS 18V-10 L", "WD 3-18 S"]:
    check(needle in cordless, f"cordless: missing candidate {needle}")
check("Classe L" in cordless and "classe M" in cordless, "cordless: class distinction missing")

wetdry = html("aspirateur-eau-poussiere")
check("Nilfisk Multi II 30 T" in wetdry, "wet/dry: non-Kärcher coverage missing")
check("Wet & dry n’est pas une classe de poussière" in wetdry, "wet/dry: safety boundary missing")

bagless = html("aspirateur-chantier-sans-sac")
for needle in ["Conçu explicitement sans sac", "Peut collecter en cuve", "Devrait utiliser un système de collecte"]:
    check(needle in bagless, f"bagless: collection-mode distinction missing: {needle}")

compact = html("petit-aspirateur-de-chantier")
check("moins de 15" not in compact.lower() and "< 15" not in compact, "compact: arbitrary litre threshold remains")
check("poids" in compact.lower() and "encombrement" in compact.lower(), "compact: handling definition incomplete")

hub = (BASE / "comparatifs" / "index.html").read_text(encoding="utf-8")
for stale in ["Dépression &gt; 25 kPa", "&lt; 15 litres", "Grande capacité", "Poussières dangereuses modérées"]:
    check(stale not in hub, f"comparison hub: stale scope label remains: {stale}")
for fresh in ["Débit et dépression contextualisés", "Mobilité et encombrement", "Process, continu, huiles et copeaux", "Certification classe M"]:
    check(fresh in hub, f"comparison hub: new role label missing: {fresh}")

# The general and powerful pages must no longer be the same product universe.
g = {p["id"] for p in data("meilleur-aspirateur-de-chantier").get("product_universe", [])}
p = {p["id"] for p in data("aspirateur-chantier-puissant").get("product_universe", [])}
check(g != p, "cluster: general and powerful still use the exact same product universe")

# Exact H2 cloning is still useful as a low-level draft check.
signatures = defaultdict(list)
for slug in REWRITTEN:
    sig = tuple(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", x)).strip().lower() for x in re.findall(r"<h2\b[^>]*>(.*?)</h2>", html(slug), flags=re.S | re.I))
    signatures[sig].append(slug)
for slugs in signatures.values():
    check(len(slugs) == 1, "cluster: identical H2 architecture remains: " + ", ".join(slugs))

# READY pages get a stronger functional anti-template gate. Components can be shared,
# but three READY pages may not have the exact same ordered component cadence.
ready_slugs = [slug for slug in ALL if data(slug).get("editorial", {}).get("publish_review") == READY]
functional = defaultdict(list)
for slug in ready_slugs:
    functional[functional_signature(slug)].append(slug)
for sig, slugs in functional.items():
    if sig and len(slugs) >= 3:
        check(False, "cluster: READY pages share the same functional editorial cadence: " + ", ".join(slugs))

# Long editorial prose copied verbatim into 3+ READY pages is also a blocker.
paragraph_owners = defaultdict(set)
for slug in ready_slugs:
    for paragraph in normalized_long_paragraphs(slug):
        paragraph_owners[paragraph].add(slug)
for owners in paragraph_owners.values():
    if len(owners) >= 3:
        check(False, "cluster: long editorial paragraph cloned across READY pages: " + ", ".join(sorted(owners)))

if errors:
    print("COMPARISON_ROLLOUT: FAIL")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)

print("COMPARISON_ROLLOUT: PASS")
print(" - intent and safety boundaries preserved across all 9 comparison drafts")
print(f" - {len(ready_slugs)} page(s) currently claim READY_FOR_HUMAN_VALIDATION")
print(" - READY pages are subject to functional-cadence and long-paragraph anti-template gates")
print(" - all 9 comparison pages remain noindex, follow")
