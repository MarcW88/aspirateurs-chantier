# Cluster audit — Marques — aspirateurs-chantier.fr

Date : 2026-09-10
Mode : `brand-analysis-workflow / CLUSTER_AUDIT`
Scope : `/marques/karcher/`, `/marques/bosch/`, `/marques/makita/`, `/marques/festool/`, `/marques/dewalt/`, `/marques/parkside/`, `/marques/nilfisk/`, `/marques/mirka/`

## Statut global

**CLUSTER NOT READY FOR HUMAN VALIDATION**

Les huit pages restent des drafts `noindex, follow`. Le nouveau contrat v2 de workflow est en place, mais aucun des huit slugs ne possède encore de run-evidence éditorial complet dans `.content/brands/runs/<slug>.json`. Le cluster doit donc être retravaillé avec le stack partagé avant toute nouvelle décision de publication.

## Méthode 80/20

L'audit utilise la gouvernance actuelle du repo : méthodologie partagée issue des skills vendored depuis `bloc-notes-numerique` et leurs upstreams lorsque documentés ; custom limité aux risques métier aspirateurs et à la distinctivité inter-marques.

Shared gates mobilisés pour le diagnostic :

- `search-intent`
- `content-audit`
- `content-refresh`
- `fact-check`
- `evidence-based-reviews`
- `affiliate-value`
- `content-brief-authoring`
- `internal-linking-audit`
- `anti-ai-slop`
- `seo-technical` / `seo-best-practices`
- `editorial-qa`

Custom :

- lecture des risques métier spécifiques aux aspirateurs de chantier ;
- comparaison des rôles et architectures des huit pages marque.

Cet audit ne prétend pas constituer le futur run-evidence de rédaction. Il décide quoi retravailler et dans quel ordre.

---

# 1. Findings cluster-wide

## 1.1 Le vieux template fixe a été largement cassé — à préserver

La situation actuelle est meilleure que l'ancien générateur `gamme → écosystème → forces → limites → choisir → éviter`. Les overrides actuels donnent déjà des axes propres :

- Kärcher : WD vs NT, puis Tact / ACD et niveau de besoin ;
- Bosch : Home & Garden vs GAS Professional, puis les deux écosystèmes 18 V ;
- Makita : lecture de référence, filaire VC, LXT/XGT, AWS/Makpac ;
- Festool : système de travail, CTL/CTM/CTH, AUTOCLEAN, CTC/CTMC, CLEANTEC/Systainer ;
- DeWalt : chantier sans fil, DCV586M/DCV584L, AIRLOCK, FLEXVOLT/TSTAK ;
- Parkside : rapport équipement/prix, révisions PWD, disponibilité, limites de sécurité ;
- Nilfisk : Buddy/Multi vs ATTIX, InfiniClean, spécialisation aspiration ;
- Mirka : ponçage d'abord, DEXOS 1217/1230, DEROS/DEOS, workflow Mirka.

**Conclusion : ne pas revenir à un template unique.** La direction structurelle est bonne.

## 1.2 La profondeur éditoriale reste insuffisante et trop uniforme

Le problème principal n'est plus l'identité des H2, mais la cadence : une answer-box, 5–6 sections courtes, souvent deux paragraphes par section, un tableau d'orientation, puis les sources. Cette régularité produit encore une sensation de page générée même lorsque les headings diffèrent.

Il ne faut pas ajouter des mots pour atteindre un quota. Il faut approfondir uniquement les questions où une vraie décision est aujourd'hui compressée :

- générations et statut des références ;
- compatibilités réelles outils / flexibles / raccords ;
- sacs, filtres et consommables ;
- coût de changement ou de maintien d'écosystème ;
- différences entre classes et variantes proches ;
- conséquences de poids, cuve et mobilité ;
- situations de chantier où l'avantage de marque disparaît ;
- contradictions ou limites entre documentation, disponibilité et usage réel.

## 1.3 Evidence layer trop centré fabricant

La couche factuelle actuelle est utile pour les classes, caractéristiques et compatibilités documentées, mais elle repose presque exclusivement sur des sources officielles fabricant ou retailer. Ce niveau est suffisant pour un claim de spécification ; il ne suffit pas pour transformer des formulations comme « workflow plus stable », « particulièrement intéressant », « plus pratique », « premium justifié » ou des jugements d'ergonomie/fiabilité en conclusions solides.

Pour les futures réécritures :

- Tier 1 fabricant/documentation pour specs, classes, compatibilité et statut ;
- Tier 2 utilisateurs seulement lorsqu'un corpus réel permet d'identifier un pattern ;
- Tier 3 tests indépendants nommés pour ergonomie, bruit, comportement avec poussière fine, mobilité, qualité des raccords, etc. ;
- Tier 4 interdit sauf vrai test du site.

Aucune page marque n'a besoin artificiellement de Tier 2/3 partout. En revanche, dès qu'un jugement dépasse la spec, il doit être étayé ou reformulé comme déduction.

## 1.4 La valeur affiliée originale existe, mais reste trop souvent au niveau de la bonne remarque

Les pages contiennent déjà des insights utiles : WD n'est pas NT, HEPA n'est pas classe M, LXT n'est pas XGT, POWER FOR ALL n'est pas AMPShare, DEXOS n'est pas un aspirateur de gravats généraliste. C'est une bonne base.

Ce qui manque est la transformation de ces insights en outils de décision plus riches : matrices de compatibilité lorsque nécessaire, lecture du coût total, arbre de décision, mapping gamme → usage → limite, risques de mauvais achat, différences de génération et routage vers la bonne fiche modèle.

Test à garder : la page doit rester nettement utile si tous les liens affiliés sont supprimés.

## 1.5 Frontière marque / modèle à mieux tenir

Bosch, Kärcher et Makita contiennent déjà beaucoup de détails modèle. Une page marque doit utiliser ces références pour expliquer une logique de gamme, puis router vers `/modeles/`. Elle ne doit pas devenir huit mini-reviews alignées.

À l'inverse, une page trop abstraite qui ne nomme jamais les modèles décisifs devient un simple discours de marque. L'objectif est donc : **modèles comme preuves et points de repère, pas comme catalogue.**

## 1.6 Similarité acceptable vs similarité problématique

Acceptable et à conserver :

- même shell HTML ;
- answer-box lorsque réellement utile ;
- sidebar / TOC ;
- composants tableau ;
- disclosure desk research ;
- bloc sources ;
- design commun.

À éviter dans la prochaine production :

- toujours exactement 6 sections ;
- toujours un tableau central ;
- même longueur de section ;
- même mécanique « avantage → contrepartie » à chaque H2 ;
- même conclusion « comparez le coût complet » ;
- même rappel L/M/H répété plusieurs fois si une seule occurrence suffit ;
- alternatives ajoutées par symétrie plutôt que parce qu'elles résolvent une limite précise.

---

# 2. Décisions par page

## Kärcher — `DEEP_REWRITE`

**À préserver** : angle WD vs NT ; hiérarchie sécurité avant performance ; Tact/ACD ; routage WD pour usage courant et NT pour besoins professionnels.

**Pourquoi deep** : la marque possède une profondeur de gamme très supérieure à ce que la page actuelle exploite. Le passage Home & Garden → Professional, les variantes NT, les consommables/accessoires, la logique de décolmatage, les usages de gros volume et la lecture ACD méritent une architecture plus riche. Le contenu actuel est juste mais trop condensé pour une des marques les plus larges du cluster.

**Research focus** : gamme actuelle France, architecture WD/NT, Tact, ACD, L/M/H, filtres/sacs/flexibles, raccordement outil, différences 30/50 L, maintien de débit, coûts/contraintes de consommables, alternatives par besoin.

## Bosch — `LIGHT_UPDATE`

**À préserver** : structure actuelle DIY vs Professional vs 18 V ; distinction POWER FOR ALL / AMPShare ; tableau GAS ; contextualisation des chiffres mesurés à la turbine.

**Pourquoi light** : c'est actuellement la page la plus aboutie du cluster. Elle couvre plusieurs références actuelles et transforme correctement la nomenclature Bosch en décision. Le besoin principal est de compléter le run-evidence, de renforcer/qualifier les jugements non purement factuels et de vérifier que les détails modèle ne cannibalisent pas les fiches dédiées.

**Research focus** : actualité des gammes PAS/AdvancedVac/GAS, accessoires Click & Clean, L-BOXX, AMPShare, disponibilité des consommables, sources indépendantes uniquement pour les claims d'usage qui le nécessitent.

## Makita — `DEEP_REWRITE`

**À préserver** : angle « décoder la référence avant de choisir » ; distinction LXT / 18Vx2 / XGT ; AWS / Makpac ; classe avant plateforme.

**Pourquoi deep** : la complexité Makita est précisément sa valeur éditoriale potentielle, mais elle est encore trop résumée. Les suffixes, variantes L/M/H, kits, plateformes, AWS, diamètres/raccords et statut de nombreuses références rendent une simple série de paragraphes insuffisante.

**Research focus** : nomenclature exacte, statut France des références, classes par référence, différences LXT/XGT, compatibilité AWS, kits batterie, raccords, Makpac, consommables, coût total d'un passage de plateforme.

## Festool — `LIGHT_UPDATE`

**À préserver** : logique système ; CTL/CTM/CTH ; AUTOCLEAN ; CLEANTEC ; MIDI ; CTC/CTMC ; coût de l'écosystème comme angle.

**Pourquoi light** : l'architecture est déjà nettement spécifique et le rôle de marque est clair. L'amélioration doit surtout porter sur la profondeur de preuve et sur les conséquences concrètes de l'écosystème, sans transformer la page en revue de chaque CT.

**Research focus** : générations actuelles, compatibilités de flexibles/raccords, Systainer, Bluetooth, AUTOCLEAN, consommables, différences MIDI/grands volumes et éléments indépendants lorsque l'on parle réellement d'ergonomie ou de workflow.

## DeWalt — `LIGHT_UPDATE`

**À préserver** : positionnement autour du chantier sans fil ; DCV586M comme pivot ; distinction DCV584L classe L ; AIRLOCK ; FLEXVOLT/TSTAK.

**Pourquoi light** : la gamme plus resserrée justifie une page plus courte que Kärcher ou Makita. Le problème n'est pas d'ajouter beaucoup de sections, mais de mieux démontrer quand l'écosystème DeWalt est rationnel, ses contraintes de batterie et les limites réelles face aux grandes gammes filaires.

**Research focus** : statut DCV586/DCV584 et successeurs éventuels, AIRLOCK, Perform & Protect, autonomie/kit uniquement si source solide, coût batterie, accessoires de captage et frontière L/M.

## Parkside — `DEEP_REWRITE`

**À préserver** : angle disponibilité/révisions ; PWD 12/20/25/30 ; valeur équipement/prix ; distinction nettoyage manuel du filtre vs AFC/Tact/InfiniClean ; absence de déduction M/H.

**Pourquoi deep** : c'est la page la plus exposée à l'obsolescence commerciale. Les références Lidl tournent, les suffixes changent et la disponibilité est discontinue. Une page utile doit aller plus loin sur la logique de génération, disponibilité, compatibilité consommables et coût d'un achat « bon marché » dans la durée. Une photographie de quatre fiches produit ne suffit pas.

**Research focus** : offre réellement visible aujourd'hui, historique récent des générations, filtres/sacs compatibles, disponibilité des pièces, fonctions selon suffixe, limites d'usage intensif. Les expériences utilisateurs ne doivent être intégrées que si un corpus suffisant est étudié.

## Nilfisk — `DEEP_REWRITE`

**À préserver** : lecture Buddy/Multi vs ATTIX ; spécialisation aspiration ; InfiniClean ; classe et référence complète avant volume.

**Pourquoi deep** : Nilfisk a un univers professionnel suffisamment large pour que le raccourci « Multi grand public / ATTIX pro » reste trop grossier. La page actuelle a un bon angle mais ne tire pas assez parti de la profondeur de gamme, des systèmes de filtration, des accessoires et de la neutralité vis-à-vis des plateformes d'outillage.

**Research focus** : architecture actuelle ATTIX, variantes M/H, InfiniClean, FlowSensor, antistatique, filtres/sacs, raccordements, gammes Multi/Buddy, usages où l'absence d'écosystème outil est un avantage ou une limite.

## Mirka — `LIGHT_UPDATE`

**À préserver** : ponçage d'abord ; DEXOS 1217/1230 ; DEROS/DEOS ; AFC ; workstation / myMirka ; limites hors ponçage.

**Pourquoi light** : le positionnement est déjà le plus spécifique du cluster et la gamme est assez étroite pour qu'une page concise reste légitime. Il faut surtout renforcer les preuves derrière les affirmations de workflow, vérifier la transition des anciennes générations DE vers DEXOS et documenter plus précisément les compatibilités utiles.

**Research focus** : DEXOS actuels, compatibilité DEROS/DEOS, AFC, workstation, Bluetooth/myMirka, flexibles/abrasifs, sources indépendantes uniquement pour les bénéfices d'usage non démontrés par la documentation.

---

# 3. Priorisation recommandée

Ordre de travail recommandé, non pas selon volume de recherche mais selon valeur du test méthodologique :

1. **Kärcher — DEEP_REWRITE** : meilleur test d'un brand hub large avec séparation grand public/pro/sécurité.
2. **Makita — DEEP_REWRITE** : meilleur test de complexité nomenclature + écosystèmes batterie.
3. **Parkside — DEEP_REWRITE** : meilleur test de fraîcheur, disponibilité et valeur sans surpromesse.
4. **Nilfisk — DEEP_REWRITE** : meilleur test d'une marque spécialiste aspiration.
5. **Bosch — LIGHT_UPDATE** : benchmark interne à préserver et enrichir.
6. **Festool — LIGHT_UPDATE**.
7. **Mirka — LIGHT_UPDATE**.
8. **DeWalt — LIGHT_UPDATE**.

L'ordre peut changer si les données de performance organique montrent une priorité commerciale ou SEO différente, mais cette séquence est la plus utile pour valider le nouveau workflow.

---

# 4. Gate pour la prochaine étape

Pour chaque page retravaillée :

1. créer un vrai `.content/brands/runs/<slug>.json` ;
2. exécuter le stack shared et persister des outputs concrets ;
3. construire le plan seulement après intention + evidence brief + affiliate-value ;
4. laisser le custom aspirateurs intervenir sur les risques métier ;
5. rédiger via `content-and-copy`, puis fact-check post-draft et stack de finition ;
6. passer l'anti-template inter-pages ;
7. exécuter `PUBLISH_REVIEW` ;
8. conserver `noindex, follow` tant qu'il n'y a pas de validation humaine et instruction d'indexation.

## Résultat du CLUSTER_AUDIT

- `DEEP_REWRITE` : Kärcher, Makita, Parkside, Nilfisk.
- `LIGHT_UPDATE` : Bosch, Festool, DeWalt, Mirka.
- `KEEP` : aucun à ce stade, car aucun run v2 n'est suffisamment documenté pour considérer le travail comme définitivement terminé.
- `MERGE` : aucun.
- `NOINDEX` structurel : aucun ; les huit pages ont une intention autonome légitime, mais restent temporairement `noindex, follow` pendant la récupération.

**Décision cluster : retravailler, ne pas publier/indexer maintenant.**
