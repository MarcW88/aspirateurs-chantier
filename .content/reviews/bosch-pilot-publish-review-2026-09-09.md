# Bosch brand pilot — PUBLISH_REVIEW

Date : 2026-09-09  
URL : `/marques/bosch/`  
Workflow : `brand-analysis-workflow / PUBLISH_REVIEW`  
Rendered page blob reviewed : `48c7255396384af5ba84c10453bf26e04a8a41b2`  
Evidence data blob reviewed : `79c721ae89cf8bbf51efd67aa8de433bf6840fea`

## Result

**PASS — READY_FOR_HUMAN_VALIDATION**

The page must remain `noindex, follow` until explicit human approval and an explicit instruction to make it indexable.

## Shared stack execution

The pilot used the repository 80/20 stack:

- search intent / page role;
- content audit and deep-refresh decision;
- affiliate value;
- fact check;
- evidence-based review boundaries;
- internal linking audit;
- humanizer / general writing / cadence / anti-AI-slop principles;
- SEO technical and best-practice checks;
- editorial QA;
- Bosch-specific brand analysis and publish gate.

The stack validator and repository brand validator both passed in GitHub Actions during generation. The Bosch override was also checked for idempotence.

## Intent and role — PASS

Primary role: `BRAND_HUB`.

Primary reader problem: understand which Bosch universe is relevant before choosing a model.

The page now routes the reader through three distinct decisions:

1. Home & Garden / wet & dry;
2. GAS Professional / dust class and filter cleaning;
3. 18 V platform choice.

It no longer duplicates a model page or follows the generic brand sequence `range → ecosystem → strengths → limitations → choose → avoid`.

## Original affiliate value — PASS

The page remains useful without affiliate links because it:

- decodes Bosch DIY versus Professional;
- maps the expanded 2026 DIY range into useful segments;
- separates class L from class M rather than ranking on suction numbers;
- shows that GAS 35 M AFC and GAS 55 M AFC share the same maximum turbine figures and differ mainly in capacity / mobility;
- explains the incompatibility between POWER FOR ALL and Professional 18V / AMPShare;
- routes to model pages only after the decision context is established.

## Evidence / fact check — PASS

Primary sources verified on 2026-09-09:

- Bosch DIY wet/dry range: https://www.bosch-diy.com/fr/fr/outils-de-nettoyage/aspirateurs-eau-et-poussiere
- PAS30-240PRS: https://www.bosch-diy.com/fr/fr/p/pas30-240prs-06033e73w0
- AdvancedVac 20: https://www.bosch-diy.com/fr/fr/p/advancedvac-20-06033d12w0
- AdvancedVac 18V-8: https://www.bosch-diy.com/fr/fr/p/advancedvac-18v-8-06033e1000
- GAS 18V-10 L: https://www.bosch-professional.com/fr/fr/products/gas-18v-10-l-06019C6302/
- GAS 35 M AFC: https://www.bosch-professional.com/fr/fr/products/gas-35-m-afc-06019C31W0
- GAS 55 M AFC: https://www.bosch-professional.com/fr/fr/products/gas-55-m-afc-06019C33W0
- AMPShare: https://www.bosch-professional.com/fr/fr/ampshare/

### Claims confirmed

- Bosch DIY France currently lists PAS15-200, UniversalVac 15, PAS15-220, AdvancedVac 18V-8, PAS20-220P, AdvancedVac 20 and PAS30-240PRS.
- PAS30-240PRS: 30 L, 67 l/s and 265 mbar at turbine, semi-automatic filter cleaning and Auto-Start.
- AdvancedVac 20: 20 L, 70 l/s and 260 mbar at turbine, automatic start/stop with connected tool.
- AdvancedVac 18V-8: 8 L, 29 l/s at turbine, POWER FOR ALL 18V.
- GAS 18V-10 L: class L, 10 L gross / 6 L net, 34 l/s, 115 mbar, 4.7 kg without battery, Click & Clean, Professional 18V / AMPShare.
- GAS 35 M AFC: class M, 35 L gross / 23 L net, 74 l/s, 254 mbar, AFC, Click & Clean, L-BOXX, 12.4 kg.
- GAS 55 M AFC: class M, 55 L gross / 43 L net, 74 l/s, 254 mbar, AFC, Click & Clean, L-BOXX, 16.2 kg.
- Bosch explicitly states that AMPShare / Professional 18V and POWER FOR ALL batteries are not compatible.

No merchant source is used to establish the principal specifications.

## Safety and claim boundaries — PASS

- No dust class is inferred from HEPA, power, airflow or pressure.
- Class L and M are stated only for products documented by Bosch.
- Airflow and pressure are labelled as manufacturer maxima at the turbine where used.
- No cross-manufacturer performance comparison is made from non-equivalent metrics.
- The text does not give personalised regulatory advice about hazardous dust.
- No first-hand test language is used.

## Structure / anti-template gate — PASS

Bosch H2 strategy is now bespoke:

- choose the Bosch universe;
- Home & Garden / PAS / AdvancedVac;
- GAS Professional;
- two 18 V systems;
- selection by actual job;
- Bosch-specific decision limits;
- routing to next pages;
- sources.

The old generic headings `forces`, `limites`, `choisir` and `eviter` are no longer used as a shared skeleton. Visual consistency is kept through `answer-box`, `table-wrap`, related content and sidebar components.

## Internal linking — PASS

Contextual links point to existing Bosch model pages and relevant decision guides / comparisons. Links are introduced at the point where the reader's next question arises rather than collected to meet a quota.

## SEO / technical — PASS WITH DRAFT INDEXATION

- title and H1 are aligned with the Bosch brand-hub intent;
- canonical remains `/marques/bosch/`;
- the TOC reflects the bespoke H2s;
- `noindex, follow` is deliberately preserved;
- no generated page-type quota is used.

## Remaining human check

Human validation should focus on:

1. whether the Bosch decision-tree angle matches the commercial/editorial positioning desired for the site;
2. whether PAS30-240PRS deserves a dedicated `/modeles/` page later;
3. whether the density of technical tables feels right visually on desktop and mobile.

No indexation change is authorised by this review.
