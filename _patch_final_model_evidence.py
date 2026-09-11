#!/usr/bin/env python3
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
path = BASE / '.content' / 'models' / 'model-evidence.json'
data = json.loads(path.read_text(encoding='utf-8'))
data['updated_at'] = '2026-09-11'

n = data['models']['nilfisk-multi-ii-30-t']
n['description'] = 'Aspirateur eau et poussière 30 L avec prise outil, auto on/off et Push&Clean manuel.'
n['summary'] = ('Le Multi II 30 T est un aspirateur eau/poussière grand public bien équipé pour l’atelier. '
                'La fiche fabricant ne documente pas de classe L/M/H et affiche deux champs de dépression distincts, '
                '292 mbar et 210 mbar / 21 kPa, qui ne doivent pas être fusionnés.')
n['specs'] = {
    'Puissance Pmax': '1 400 W',
    'Puissance': '1 260 W',
    'Cuve': '30 L',
    'Dépression (champ Vacuum)': '210 mbar (21 kPa)',
    'Max. suction power (champ distinct)': '292 mbar',
    'Nettoyage du filtre': 'Push&Clean manuel + indicateur',
    'Prise outil': 'Oui, 1 100 W + marche/arrêt automatique',
    'Flexible': '4 m',
    'Poids': '9,6 kg',
    'Classe de sécurité': 'Pas de classe L/M/H documentée'
}
n['best_for'] = [
    'Garage et atelier avec outil électroportatif',
    'Nettoyage eau/poussière avec cuve 30 L',
    'Utilisateur qui veut Push&Clean et auto on/off sans gamme de sécurité professionnelle'
]
n['limits'] = [
    'Pas de classe L/M/H documentée sur la fiche grand public',
    'Push&Clean est manuel',
    'La fiche affiche 292 mbar et 210 mbar / 21 kPa sous deux libellés distincts'
]
n['source'] = 'https://shop.nilfisk.com/fr-be/products/multi-ii-30-t-aspirateur-eau-et-poussiere'

path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('✓ final model evidence updated')
