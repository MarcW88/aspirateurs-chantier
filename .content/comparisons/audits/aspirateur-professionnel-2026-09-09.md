# Comparison AUDIT — `/comparatifs/aspirateur-professionnel/`

Date: 2026-09-09
Mode: `AUDIT`
Decision: `DEEP_REWRITE`
Confidence: high
Indexing: keep `noindex, follow`

## Intent / JTBD

Target query: `aspirateur chantier professionnel`.

The useful decision is broader than `aspirateur classe M`: a professional first needs to identify the dust-risk requirement, then choose between mobility, continuous filter cleaning, tool integration, capacity and operating constraints.

The page should therefore remain scenario-led and explicitly route class-M-only intent to `/comparatifs/aspirateur-classe-m/`.

## What to preserve

- the current principle that there is no universal professional winner;
- the distinction `professionnel != classe M`;
- the separation from the dedicated class-M comparison;
- the desk-research disclosure and absence of fake hands-on claims;
- the existing site visual system, answer box, table, sidebar and contextual internal links;
- `noindex, follow`.

## Blockers

### 1. HTML / evidence-ledger drift

The current JSON persists a 3-product class-M scoring exercise (Kärcher / Bosch / Festool), while the rendered page presents four scenario references dominated by Bosch plus Makita. The published reasoning can no longer be reconstructed from the persisted methodology.

### 2. Candidate scope is not strong enough for a professional comparison

Three of the four displayed references are Bosch. The page works as a professional buying guide, but the cross-brand comparison value is too weak.

### 3. Old scoring no longer matches the editorial thesis

The persisted hard gate `classe M` contradicts the rendered page's core thesis that class M is contextual, not a universal requirement for every professional use case. The numeric ranking is therefore removed from this pilot rather than recalculated.

### 4. Measurement comparability needs to be explicit

Bosch publishes airflow/depression maxima at the turbine for several GAS models. Other manufacturers do not necessarily publish the same measurement context. These figures can be reported, but should not be used as a direct cross-brand ranking unless measurement points/protocols are demonstrably equivalent.

## Primary-source checks used for the pilot

- Bosch Professional GAS 18V-10 L: class L, 18 V, 10 L gross / 6 L net, 34 L/s and 115 mbar at turbine, 4.7 kg without battery, manufacturer-stated runtime 4 min/Ah.
- Bosch Professional GAS 12-25 PL: class L, 25 L gross / 21 L net, SFC semi-automatic filter cleaning, Auto-start via integrated socket, 65 L/s and 200 mbar at turbine.
- Bosch Professional GAS 35 M AFC: class M, 35 L gross / 23 L net, AFC, 74 L/s and 254 mbar at turbine, 12.4 kg.
- Kärcher NT 30/1 Tact Te M ACD: class M, 30 L, sensor-controlled Tact, integrated auto-start socket, full antistatic system, ACD, 74 L/s and 273 mbar published by Kärcher.
- Festool CTM MIDI I AC: class M, 15/12.5 L container/filter bag, AUTOCLEAN, 2,400 W socket allowance, 11.8 kg without accessories, Bluetooth.
- Makita VC4210MX: class M, 42 L gross / 34 L dust / 30 L liquid, InfiniClean, integrated tool socket, 16.0 kg without cable.

## Rewrite brief

### Thesis

`Professionnel` is not a performance tier. It is a set of working constraints. Determine the required dust class first, then choose the machine architecture that creates the least friction for the actual job.

### Candidate roles

- Bosch GAS 18V-10 L — mobile class-L interventions.
- Bosch GAS 12-25 PL — simple corded class-L workflow with tool Auto-start.
- Festool CTM MIDI I AC — compact class-M / service and fitting work.
- Bosch GAS 35 M AFC — balanced 35 L class-M reference with AFC.
- Kärcher NT 30/1 Tact Te M ACD — class-M workflow where Tact, antistatic equipment and ACD are decision-relevant.
- Makita VC4210MX — high-capacity class-M option when 42 L and InfiniClean matter more than compactness.

These are representative current references, not an exhaustive market census and not a numerical ranking.

### Structure

1. Direct answer: risk class first, then workflow.
2. Decision table by professional situation.
3. Why `professional` and `class M` are separate intents.
4. The four variables that actually change the choice.
5. Short product trade-offs, asymmetrical by model.
6. Measurement caveat: do not rank by airflow/depression across unequal protocols.
7. Route to class-M / cordless / usage / guide pages.
8. Sources + desk-research disclosure.

## Expected post-draft result

Target: `PASS — READY_FOR_HUMAN_VALIDATION`, while remaining `noindex, follow` until explicit human/indexation approval.
