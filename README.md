## ventesSimplon

Projet d'analyse et de visualisation des ventes (Simplon) avec Python, Pandas et Plotly. Le script `app.py` génère des pages HTML interactives à partir d'une source de données Google Sheets.

### Aperçu rapide
- **Entrée**: une feuille Google Sheets (CSV public)
- **Sortie**: fichiers HTML interactifs
  - `ventes-par-region.html`
  - `ventes-par-produit.html`
  - `chiffre-affaires-par-produit.html`

## Prérequis
- Windows avec PowerShell
- Python 3.8+ installé (`py -3 --version` pour vérifier)
- Accès Internet (le CSV est téléchargé depuis Google Sheets)

## Installation
Exécutez ces commandes dans le dossier du projet:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
```

## Générer les visualisations
Lancez le script pour produire les fichiers HTML:

```powershell
python app.py
```

Les fichiers générés apparaîtront à la racine du projet.

## Prévisualisation locale
Option 1 — serveur local (recommandé):

```powershell
python -m http.server 8000
```

Ensuite ouvrez dans votre navigateur:
- `http://localhost:8000/ventes-par-region.html`
- `http://localhost:8000/ventes-par-produit.html`
- `http://localhost:8000/chiffre-affaires-par-produit.html`

Option 2 — ouverture directe: double-cliquez sur les fichiers `.html` (peut limiter certaines fonctionnalités selon le navigateur).

## Structure du projet
```
app.py                          # Génère les 3 pages HTML (Plotly)
requirements.txt                # Dépendances Python
ventes-par-region.html          # Sortie 1 (générée)
ventes-par-produit.html         # Sortie 2 (générée)
chiffre-affaires-par-produit.html # Sortie 3 (générée)
requete.sql                     # Exemples de requêtes SQL (référence)
synthese_analyse.md             # Notes d'analyse
```

## Commandes utiles
Recréer l'environnement rapidement:
```powershell
py -3 -m venv .venv; .\.venv\Scripts\Activate.ps1; python -m pip install -U pip; pip install -r requirements.txt
```

Regénérer les pages et lancer le serveur enchaîné:
```powershell
python app.py; python -m http.server 8000
```


## Licence
Projet pédagogique. Utilisation libre à des fins d'apprentissage.
