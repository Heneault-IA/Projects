# 🚀 Projet OpenClassrooms - Home Credit Default Risk (API)

## 🎯 Objectif du Projet

Ce projet, réalisé dans le cadre du parcours OpenClassrooms, porte sur l'analyse du jeu de données _Home Credit Default Risk_ et inclut la création d'un modèle de prédiction (Scoring de Crédit) déployé via une API REST.

## 📂 Contenu du Projet

- **Tests** : Ce dossier contient les tests (unitaires) réalisés à chaque push sur la branche main (Intégration Continue).
- **model** : Héberge les fichiers nécessaires au déploiement du modèle de Machine Learning. Il s'agit d'un `LGBMClassifier` déjà entraîné sur les données d'entraînement.
- **templates** : Contient les fichiers HTML pour le rendu de l'application (si besoin de vues web).
- **Fichiers principaux** :
  - `app.py` : L'application principale (API) déployée sur Heroku.
  - `fonction.py` : Contient les fonctions ou la logique métier (testées).
  - `noteboo.ipynb` : Le notebook contenant l'exploration des données et la recherche du meilleur modèle (modélisation).
  - `Procfile` : Fichier de configuration indispensable pour le déploiement de l'application sur Heroku.

## 🚀 Utilisation

### Notebooks

Pour explorer les analyses, le nettoyage, et les résultats de la modélisation en profondeur, veuillez ouvrir le fichier `.ipynb` dans Jupyter Notebook ou JupyterLab.

### API (Déploiement)

L'API est déployée de manière automatisée sur Heroku et accessible à l'adresse suivante :
🔗 [Lien de l'API Heroku](https://home-credi-default-risk-2d75b983d33b.herokuapp.com/)

> **Note** : Le format de la requête attendu par l'API correspond au format de données généré et documenté à la fin du notebook.

Une application complémentaire (Streamlit) permet également de simuler les appels à cette API à l'aide de données pré-enregistrées (voir le projet de Dashboard).

---

_Auteur : Heneault Thomas_
