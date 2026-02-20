# 🍏 Projet 3 : Analyse de Données - Open Food Facts

## 🎯 Objectif du Projet

L'objectif de ce projet est d'explorer et de nettoyer le jeu de données public **Open Food Facts**. L'idée principale est d'analyser ces données nutritives complexes afin de vérifier la faisabilité de développer un moteur d'autocomplétion ou de suggestion.

## 🗂️ Données Nécessaires

Les données brutes (très volumineuses) doivent être téléchargées depuis les serveurs d'Open Food Facts :
🔗 [Open Food Facts Dataset (CSV.gz)](https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv.gz)

⚠️ **Instruction** : Décompressez le fichier téléchargé dans un dossier nommé `Data` à la racine de ce projet.
_Note : Pour des raisons de taille de fichier, certaines sorties graphiques ont été supprimées des notebooks sauvegardés._

## 🛠️ Outils et Environnement

Environnement préconisé : `python >=3.7 <3.12`

### Librairies principales :

- `numpy` (^1.25.1)
- `pandas` (^2.0.3)
- `matplotlib` (^3.7.2) & `seaborn` (^0.12.2)
- `scikit-learn` (^1.3.0)
- `missingno` (^0.5.2) pour l'analyse des valeurs manquantes
- `googletrans` (4.0.0-rc1) & `langdetect` (^1.0.9) pour le NLP et la détection de langue
