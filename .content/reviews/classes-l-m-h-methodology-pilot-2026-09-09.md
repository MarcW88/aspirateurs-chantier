# PUBLISH_REVIEW — /guides/classes-l-m-h/

Date : 2026-09-09
Method : shared 80/20 content stack + aspirateurs-chantier domain checks
Refresh decision : `LIGHT_UPDATE`
Result : **PASS — READY_FOR_HUMAN_VALIDATION**

## Gate 1 — Intent

PASS.

La page répond immédiatement à la confusion principale : L/M/H concernent l’aspirateur complet, et le nom d’un matériau ne suffit pas à sélectionner une classe. Le tableau de lecture rapide réduit le temps nécessaire pour comprendre les trois niveaux sans devenir une prescription automatique.

## Gate 2 — Recovery discipline

PASS.

Le contenu existant était déjà solide et n’a pas été remplacé par une réécriture complète. Les axes norme, matériaux, HEPA, choix, maintenance, sources et maillage ont été conservés puis clarifiés. La principale nouveauté structurelle est le tableau L/M/H et la mise à jour INRS 2026.

## Gate 3 — Factuality / evidence

PASS.

- EN/IEC 60335-2-69 correctement reliée aux classes L/M/H.
- Seuils >99 %, >99,9 % et >99,995 % corroborés par la documentation fabricant citant la norme.
- Classe H de l’aspirateur distinguée de H13/H14 du filtre.
- Exigences amiante formulées à partir de l’INRS.
- Captage à la source / aspiration haute dépression pour la silice formulé à partir de l’INRS.
- Étude INRS 2026 explicitement limitée aux appareils étudiés ; aucun comportement universel des H n’est déduit.

## Gate 4 — Vacuum-domain safety

PASS.

La page n’infère jamais une classe depuis :

- un filtre HEPA ;
- une puissance moteur ;
- un débit ;
- un simple nom de matériau.

La séquence de décision reste : risque et prescriptions → classe → captage → performances et maintien du débit → accessoires / maintenance.

## Gate 5 — Original value

PASS.

La page apporte plus qu’un tableau constructeur :

- distinction entre appareil et média filtrant ;
- garde-fou matériau ≠ classe universelle ;
- interprétation du rôle du captage à la source ;
- mise en contexte du compromis colmatage / filtration issu de l’étude INRS 2026 ;
- routage vers les guides performance et le comparatif M seulement après cadrage de la classe.

La page reste utile sans aucun lien affilié.

## Gate 6 — Writing / anti-AI-slop

PASS.

Le texte reste technique mais lisible, sans faux témoignage, superlatif marchand, conclusion générique ou structure artificiellement symétrique. Les limites de preuve sont visibles dans le corps du texte.

## Gate 7 — Internal linking

PASS.

Les liens servent des approfondissements distincts : plâtre, bois, classe M, HEPA, débit, décolmatage, prise asservie, entretien et sac/sans sac. Pas de quota éditorial utilisé pour décider des destinations.

## Gate 8 — SEO / technical

PASS pour le pilote.

- title/H1 cohérents avec l’intention ;
- canonical inchangé et correct ;
- `noindex, follow` conservé ;
- answer-box présente ;
- TOC alignée sur les H2 réels ;
- sources externes visibles ;
- aucun changement d’indexation autorisé par ce review.

## Machine QA

GitHub Actions pilot :

- génération complète des guides : PASS ;
- override LIGHT_UPDATE : PASS ;
- structural quality gate : PASS ;
- assertions spécifiques article : PASS ;
- idempotence de l’override : PASS ;
- `noindex, follow` : PASS.

## Conclusion

**PASS — READY_FOR_HUMAN_VALIDATION**

Ce test valide surtout un point méthodologique : le stack 80/20 n’a pas besoin de produire un `DEEP_REWRITE` pour montrer sa valeur. Ici, la bonne décision était de préserver un article déjà sérieux, d’augmenter sa valeur décisionnelle et d’ajouter uniquement les preuves nouvelles qui changent réellement la compréhension.
