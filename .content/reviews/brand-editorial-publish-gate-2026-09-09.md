# Brand Editorial Publish Gate — audit initial — 09/09/2026

## Scope

Pages auditées :

- `/marques/karcher/`
- `/marques/bosch/`
- `/marques/makita/`
- `/marques/festool/`
- `/marques/dewalt/`
- `/marques/parkside/`
- `/marques/nilfisk/`
- `/marques/mirka/`

Gate utilisé : `.agents/skills/brand-editorial-publish-gate/SKILL.md`.

Décision globale : **FAIL — KEEP NOINDEX**.

Le nouvel audit ne remet pas en cause la QA structurelle du Brand Content Workflow. Il ajoute une barrière éditoriale plus exigeante avant toute future indexation.

## Blockers communs aux 8 hubs

### 1. Statuts internes visibles par le lecteur

Le générateur affiche directement des codes éditoriaux comme `CURRENT`, `PREVIOUS_GENERATION`, `CURRENT_OR_CATALOG`, `CURRENT_STOCK_DEPENDENT`, `CURRENT_BY_MARKET` ou variantes proches.

Ces codes sont utiles dans `.content/brands/*.yaml`, mais pas dans la prose publiée. Ils doivent devenir des formulations naturelles telles que :

- « gamme actuelle » ;
- « génération précédente » ;
- « encore présent au catalogue selon le marché » ;
- « disponibilité variable selon les stocks ».

Gate impacté : **Tone & editorial relevance — FAIL**.

### 2. Métadiscours éditorial répété

Le template contient plusieurs passages qui décrivent le travail éditorial au lieu de répondre directement au lecteur, notamment la logique du tableau, le fonctionnement des pages comparatives et le rôle de la rédaction.

Une courte précision méthodologique sur l'absence de test physique reste utile et peut être conservée. En revanche, les explications du type « nos pages comparatives utilisent… » ou « ce tableau sert à… » doivent être supprimées ou reformulées en information lecteur.

Gate impacté : **Tone & editorial relevance — FAIL**.

### 3. Template trop uniforme entre les marques

Les 8 hubs partagent le même enchaînement, les mêmes paragraphes de transition et plusieurs formulations quasi identiques autour du coût total, des usages, du choix/éviter, des alternatives et des sources.

La structure commune peut rester, mais les paragraphes doivent être différenciés selon la réalité de chaque marque. Le niveau actuel crée un signal `HIGH` de répétition mécanique entre pages.

Gate impacté : **Anti-AI-slop — FAIL**.

### 4. Jargon peu naturel

Le mot « workflow » apparaît dans plusieurs pages alors qu'une formulation française concrète est généralement plus naturelle dans cet univers : « chaîne outil-aspiration », « organisation de travail », « parc d'outillage », « système de ponçage ».

Gate impacté : **Tone & editorial relevance — FAIL**.

### 5. Coquille visible

Le meta-tag affiche actuellement `Verifié` au lieu de `Vérifié` sur les pages générées.

Gate impacté : **Tone & editorial relevance — FAIL**.

---

# Résultats par page

## Kärcher

URL: `/marques/karcher/`  
Page type: `BRAND_HUB`  
Status: **FAIL**

### Gate results
- Intent & relevance: PASS
- Original value: PASS
- Evidence & factuality: PASS
- Trust / E-E-A-T: PASS
- GEO / entities: PASS
- Tone & editorial relevance: FAIL
- Anti-AI-slop: FAIL
- SEO editorial: PASS
- Page-type fit: PASS

### Chantier-specific checks
- Dust class L/M/H: PASS
- HEPA vs whole-vacuum class: PASS
- Airflow / vacuum / watts: PASS
- Tank capacity semantics: PASS
- Tool socket / compatibility: PASS
- Filter cleaning terminology: PASS
- ACD / ATEX / Z22: PASS
- Hazardous dust safety: PASS
- Current model / market status: PASS

### Residual risk
La distinction WD / NT et l'avertissement ACD sont pertinents. Conserver ces éléments lors de la correction éditoriale.

---

## Bosch

URL: `/marques/bosch/`  
Page type: `BRAND_HUB`  
Status: **FAIL**

### Gate results
- Intent & relevance: PASS
- Original value: PASS
- Evidence & factuality: PASS
- Trust / E-E-A-T: PASS
- GEO / entities: PASS
- Tone & editorial relevance: FAIL
- Anti-AI-slop: FAIL
- SEO editorial: PASS
- Page-type fit: PASS

### Chantier-specific checks
- Dust class L/M/H: PASS
- HEPA vs whole-vacuum class: PASS
- Airflow / vacuum / watts: PASS
- Tank capacity semantics: PASS
- Tool socket / compatibility: PASS
- Filter cleaning terminology: PASS
- ACD / ATEX / Z22: N/A
- Hazardous dust safety: PASS
- Current model / market status: PASS

### Residual risk
Conserver la séparation Power for All 18 V / Professional 18 V et le contexte « valeurs à la turbine ».

---

## Makita

URL: `/marques/makita/`  
Page type: `BRAND_HUB`  
Status: **FAIL**

### Gate results
- Intent & relevance: PASS
- Original value: PASS
- Evidence & factuality: PASS
- Trust / E-E-A-T: PASS
- GEO / entities: PASS
- Tone & editorial relevance: FAIL
- Anti-AI-slop: FAIL
- SEO editorial: PASS
- Page-type fit: PASS

### Chantier-specific checks
- Dust class L/M/H: PASS
- HEPA vs whole-vacuum class: PASS
- Airflow / vacuum / watts: PASS
- Tank capacity semantics: PASS
- Tool socket / compatibility: PASS
- Filter cleaning terminology: PASS
- ACD / ATEX / Z22: N/A
- Hazardous dust safety: PASS
- Current model / market status: PASS, avec vigilance sur les références uniquement documentées par catalogue

### Residual risk
Ne pas perdre la distinction LXT / XGT ni la prudence sur les suffixes et variantes de marché.

---

## Festool

URL: `/marques/festool/`  
Page type: `BRAND_HUB`  
Status: **FAIL**

### Gate results
- Intent & relevance: PASS
- Original value: PASS
- Evidence & factuality: PASS
- Trust / E-E-A-T: PASS
- GEO / entities: PASS
- Tone & editorial relevance: FAIL
- Anti-AI-slop: FAIL
- SEO editorial: PASS
- Page-type fit: PASS

### Chantier-specific checks
- Dust class L/M/H: PASS
- HEPA vs whole-vacuum class: PASS
- Airflow / vacuum / watts: PASS
- Tank capacity semantics: PASS
- Tool socket / compatibility: PASS
- Filter cleaning terminology: PASS
- ACD / ATEX / Z22: N/A
- Hazardous dust safety: PASS
- Current model / market status: PASS

### Residual risk
Le mapping CTL / CTM / CTH doit rester attaché aux références documentées et ne pas devenir une règle extrapolée hors gamme.

---

## DeWalt

URL: `/marques/dewalt/`  
Page type: `BRAND_HUB`  
Status: **FAIL**

### Gate results
- Intent & relevance: PASS
- Original value: PASS
- Evidence & factuality: PASS
- Trust / E-E-A-T: PASS
- GEO / entities: PASS
- Tone & editorial relevance: FAIL
- Anti-AI-slop: FAIL
- SEO editorial: PASS
- Page-type fit: PASS

### Chantier-specific checks
- Dust class L/M/H: PASS
- HEPA vs whole-vacuum class: PASS
- Airflow / vacuum / watts: PASS
- Tank capacity semantics: PASS
- Tool socket / compatibility: PASS
- Filter cleaning terminology: PASS
- ACD / ATEX / Z22: N/A
- Hazardous dust safety: PASS
- Current model / market status: PASS

### Residual risk
Conserver explicitement le fait qu'un filtre HEPA sur le DCV584L ne transforme pas ce modèle classe L en aspirateur classe M.

---

## Parkside

URL: `/marques/parkside/`  
Page type: `BRAND_HUB`  
Status: **FAIL**

### Gate results
- Intent & relevance: PASS
- Original value: PASS
- Evidence & factuality: PASS
- Trust / E-E-A-T: PASS
- GEO / entities: PASS
- Tone & editorial relevance: FAIL
- Anti-AI-slop: FAIL
- SEO editorial: PASS
- Page-type fit: PASS

### Chantier-specific checks
- Dust class L/M/H: PASS
- HEPA vs whole-vacuum class: PASS
- Airflow / vacuum / watts: PASS
- Tank capacity semantics: PASS
- Tool socket / compatibility: PASS
- Filter cleaning terminology: PASS
- ACD / ATEX / Z22: N/A
- Hazardous dust safety: PASS
- Current model / market status: PASS, sous réserve de stock au moment de publication

### Residual risk
La disponibilité Lidl est volatile. Toute future indexation doit relancer la vérification des références et stocks avant validation humaine.

---

## Nilfisk

URL: `/marques/nilfisk/`  
Page type: `BRAND_HUB`  
Status: **FAIL**

### Gate results
- Intent & relevance: PASS
- Original value: PASS
- Evidence & factuality: PASS
- Trust / E-E-A-T: PASS
- GEO / entities: PASS
- Tone & editorial relevance: FAIL
- Anti-AI-slop: FAIL
- SEO editorial: PASS
- Page-type fit: PASS

### Chantier-specific checks
- Dust class L/M/H: PASS
- HEPA vs whole-vacuum class: PASS
- Airflow / vacuum / watts: PASS
- Tank capacity semantics: PASS
- Tool socket / compatibility: PASS
- Filter cleaning terminology: PASS
- ACD / ATEX / Z22: N/A
- Hazardous dust safety: PASS
- Current model / market status: PASS

### Residual risk
Conserver la séparation Buddy/Multi vs ATTIX et ne pas généraliser InfiniClean ou FlowSensor à toute la gamme.

---

## Mirka

URL: `/marques/mirka/`  
Page type: `BRAND_HUB`  
Status: **FAIL**

### Gate results
- Intent & relevance: PASS
- Original value: PASS
- Evidence & factuality: PASS
- Trust / E-E-A-T: PASS
- GEO / entities: PASS
- Tone & editorial relevance: FAIL
- Anti-AI-slop: FAIL
- SEO editorial: PASS
- Page-type fit: PASS

### Chantier-specific checks
- Dust class L/M/H: PASS
- HEPA vs whole-vacuum class: PASS
- Airflow / vacuum / watts: PASS
- Tank capacity semantics: PASS
- Tool socket / compatibility: PASS
- Filter cleaning terminology: PASS
- ACD / ATEX / Z22: N/A
- Hazardous dust safety: PASS
- Current model / market status: PASS

### Residual risk
Conserver le positionnement ponçage/extraction et l'avertissement explicite selon lequel classe M n'équivaut pas à classe H.

---

# Corrections requises avant un nouveau run

1. Remplacer les statuts internes visibles par du français naturel dans le tableau gamme.
2. Supprimer le paragraphe générique expliquant `CURRENT` / `PREVIOUS_GENERATION` au lecteur.
3. Réduire le métadiscours éditorial ; garder uniquement une disclosure méthodologique courte et utile.
4. Supprimer ou réécrire le paragraphe générique sur la méthodologie des comparatifs.
5. Différencier davantage les transitions et paragraphes de décision par marque.
6. Remplacer « workflow » par une formulation métier française lorsqu'il n'apporte rien.
7. Corriger `Verifié` en `Vérifié` dans le générateur.
8. Régénérer les 8 hubs puis relancer le publish gate.

## Publication decision

**KEEP NOINDEX**

Aucune page ne doit devenir indexable sur la base de cet audit. Le `noindex, follow` actuel reste le bon état jusqu'à correction, nouveau `PASS` et validation humaine explicite.
