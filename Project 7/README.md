# 🏦 Projet 7 : Moteur de Scoring et Création d'API (Home Credit Default Risk)

## 🎯 Objectif du Projet

Dans le cadre de l'évaluation du risque de crédit pour l'entreprise "Prêt à dépenser", ce projet consiste à :

1. Construire un modèle de Machine Learning de scoring de crédit (prédiction de probabilité de défaut de paiement).
2. Développer une API REST pour interroger le modèle.
3. Déployer l'API sur le cloud (avec intégration continue via Github & Heroku).

## 🗂️ Données Nécessaires

Les données proviennent de la compétition Kaggle "Home Credit Default Risk" :
🔗 [Dataset Kaggle Home Credit](https://www.kaggle.com/c/home-credit-default-risk/data)

⚠️ **Instruction** : Télécharger et extraire dans le dossier `Data`.

## 🛠️ Outils et Environnement

Environnement préconisé : `python ^3.11`

### Librairies principales :

- **Data & ML** : `pandas` (^2.1.4), `numpy` (^1.26.2), `scikit-learn` (^1.3.2), `lightgbm` (^4.2.0), `imbalanced-learn` (^0.11.0)
- **MLOps & API** : `mlflow` (^2.9.2), `streamlit` (^1.29.0), `evidently` (^0.4.13), `pytest` (^7.4.4)
- **Interprétabilité** : `shap` (^0.44.0)
