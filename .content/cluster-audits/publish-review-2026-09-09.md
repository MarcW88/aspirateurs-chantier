# CLUSTER_PUBLISH_REVIEW — 09/09/2026

## Status

**PASS — READY_FOR_HUMAN_VALIDATION — KEEP_NOINDEX**

Le PASS signifie que la séquence éditoriale et les garde-fous du cluster sont cohérents. Il ne retire pas le `noindex, follow`.

## Ordre réellement exécuté

1. **MODEL_CLEANUP**
   - 13 fiches modèles existantes sont rendues depuis `.content/models/model-evidence.json`.
   - Les placeholders `MM/AAAA`, `Contenu test à rédiger` et les champs factuels non maîtrisés sont supprimés des fiches ciblées.
   - Les appareils grand public WD / AdvancedVac / Multi ne reçoivent plus une classe L par défaut.
   - Festool CTL MIDI I est corrigé en classe L et n'est plus présenté comme AUTOCLEAN sur la référence standard.
   - Makita VC4210MX est corrigé en classe M avec InfiniClean.
   - Les métriques Bosch sont explicitées avec le contexte turbine lorsqu'il est disponible.

2. **USAGE_COMPLETION**
   - 7 pages d'usage sont complétées : plâtre, ponceuse, atelier, bois/sciure/copeaux, gravats, scie, bricolage/rénovation.
   - Leur rôle est désormais non-brand : tâche → poussière → risque → captage → classe documentée → critères de machine.
   - `/usages/aspirateur-ponceuse/` devient l'URL principale de l'intention ponceuse ; Festool et Mirka n'en gardent que la couche écosystème.

3. **NEIGHBORING_COMPARISON_BOUNDARY**
   - `/comparatifs/aspirateur-professionnel/` n'impose plus la classe M comme hard gate universel.
   - La page compare quatre profils professionnels et transfère explicitement l'intention « classe M » vers `/comparatifs/aspirateur-classe-m/`.
   - Cela réduit le chevauchement entre les deux comparatifs qui utilisaient auparavant presque le même trio de produits et des critères proches.

4. **BRAND_REVIEW**
   - Bosch reste `KEEP` sur le snapshot audité.
   - Kärcher, Festool, Makita, Nilfisk et Mirka conservent les architectures bespoke issues du `DEEP_REWRITE` parce qu'elles servent désormais une frontière de page plus nette.
   - DeWalt et Parkside sont enregistrés comme `LIGHT_UPDATE` sur le snapshot pré-rollout. Leur contenu actuel est conservé après review, mais aucune règle ne doit les faire passer automatiquement en deep rewrite lors d'un prochain recovery.
   - `/marques/` ne repose plus sur une hiérarchie Tier 1 / Tier 2 dans son contenu principal et utilise les familles actuelles (DCV, PWD, DEXOS, ATTIX, etc.).

5. **CLUSTER_PUBLISH_REVIEW**
   - pile 80/20 : PASS ;
   - 13 fiches modèles ciblées : PASS ;
   - 7 pages usages : PASS ;
   - frontière professionnel / classe M : PASS ;
   - 8 hubs marques : machine integrity PASS ;
   - génération canonique : idempotente ;
   - `noindex, follow` : conservé.

## Frontières d'intention retenues

- **Marque** : comprendre une gamme, un écosystème et les technologies qui changent la décision.
- **Modèle** : vérifier une référence précise et ses caractéristiques documentées.
- **Comparatif** : arbitrer entre plusieurs solutions pour une intention commerciale définie.
- **Usage** : résoudre un job-to-be-done non-brand.

## Garde-fous permanents

La commande canonique est `python _generate_cluster_content.py`.

Elle exécute les couches dans l'ordre imposé puis lance `_validate_cluster_rollout.py`. Le CI `.github/workflows/validate-cluster-content.yml` régénère ensuite le cluster sur PR / main et échoue si les artefacts committés divergent.

## Non-blocking follow-up

Le shell de navigation global historique contient encore les libellés visuels `Tier 1` / `Tier 2` dans le menu Marques de certaines pages. Ils ne sont plus utilisés dans le contenu du hub `/marques/` et ne pilotent plus la logique éditoriale. Leur suppression globale doit être traitée séparément dans la source de navigation afin d'éviter un rebuild massif non lié au contenu.

## Indexation

Toutes les URLs concernées restent `noindex, follow`. Une décision d'indexation doit faire l'objet d'une validation humaine séparée après revue visuelle et vérification des pages prioritaires.
