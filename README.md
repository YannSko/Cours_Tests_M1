# Calculatrice Scientifique

Un projet de calculatrice scientifique avec des fonctionnalités avancées comprenant des opérations mathématiques, statistiques et de visualisation.
L'objectif est d'implementer tout type de test via pytest & Unitest pour chaque methode/fonction

## Fonctionnalités

- Opérations mathématiques de base: addition, soustraction, multiplication, division
- Fonctions mathématiques avancées: puissance, racine carrée, logarithme, modulo
- Fonctions trigonométriques: sinus, cosinus, tangente
- Fonctions statistiques: moyenne, médiane, mode, écart-type, variance
- Statistiques avancées: percentile, corrélation, régression linéaire
- Visualisation de données: graphiques, nuages de points, histogrammes, diagrammes polaires, graphiques 3D, boîtes à moustaches, diagrammes Q-Q, cartes de chaleur, diagrammes circulaires, diagrammes à barres

## Installation

1. Cloner le dépôt
```bash
git clone <url_du_dépôt>
cd Cours_Tests_M1
```

2. Créer un environnement virtuel
```bash
python -m venv venv
```

3. Activer l'environnement virtuel
```bash
# Sur Windows
.\venv\Scripts\activate
# Sur Linux/Mac
source venv/bin/activate
```

4. Installer les dépendances
```bash
pip install -r requirements.txt
```

## Utilisation

Pour lancer l'application:
```bash
python main.py
```

## Tests

Pour exécuter les tests avec pytest:
```bash
pytest tests/
```

Pour exécuter les tests avec couverture de code:
```bash
coverage run -m pytest tests/
coverage report
coverage html  # Génère un rapport HTML dans le dossier htmlcov/
```

## Structure du projet

- `calculate/`: Contient les modules principaux de l'application
  - `controller.py`: Gère les interactions entre la vue et les opérateurs
  - `operators.py`: Implémente toutes les opérations mathématiques et statistiques
  - `view.py`: Gère l'interface utilisateur
- `tests/`: Contient les tests unitaires pour chaque module
- `main.py`: Point d'entrée de l'application

