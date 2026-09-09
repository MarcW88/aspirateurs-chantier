#!/usr/bin/env python3
"""Semantic gate for the audited comparison rollout.

This validator checks page roles and cluster boundaries. It deliberately does not
require fixed H2 labels, word counts, scores or rankings.
"""
from pathlib import Path
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
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def html(slug):
    return (BASE / "comparatifs" / slug / "index.html").read_text(encoding="utf-8")


def data(slug):
    return json.loads((BASE / ".content" / "comparisons" / f"{slug}.json").read_text(encoding="utf-8"))


for slug in ALL:
    h = html(slug)
    d = data(slug)
    check('<meta name="robots" content="noindex, follow">' in h, f"{slug}: noindex/follow changed")
    check(d.get("notes", {}).get("affiliate_commission_used_in_ranking") is False, f"{slug}: affiliate independence missing")

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

# The general and powerful pages must no longer be the same three-product universe.
g = {p["id"] for p in data("meilleur-aspirateur-de-chantier").get("product_universe", [])}
p = {p["id"] for p in data("aspirateur-chantier-puissant").get("product_universe", [])}
check(g != p, "cluster: general and powerful still use the exact same product universe")

# Distinct H2 signatures are a useful anti-template gate for the eight rewritten pages.
signatures = {}
for slug in REWRITTEN:
    sig = tuple(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", x)).strip().lower() for x in re.findall(r"<h2\b[^>]*>(.*?)</h2>", html(slug), flags=re.S | re.I))
    signatures.setdefault(sig, []).append(slug)
for sig, slugs in signatures.items():
    check(len(slugs) == 1, "cluster: identical H2 architecture remains: " + ", ".join(slugs))

if errors:
    print("COMPARISON_ROLLOUT: FAIL")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)

print("COMPARISON_ROLLOUT: PASS")
print(" - 8 audited comparison pages use bespoke decision structures")
print(" - professional pilot preserved as reference")
print(" - general/powerful overlap reduced and industrial intent respecified")
print(" - all 9 comparison pages remain noindex, follow")
