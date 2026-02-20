# 📊 Projet 8 : Dashboard Interactif et Veille Technologique

## 🎯 Objectif du Projet

Ce projet fait suite au Projet 7 (Home Credit Default Risk). L'objectif est de :

1. Concevoir un **Dashboard interactif** destiné aux chargés de relation client, interrogeant l'API de scoring développée précédemment.
2. Garantir la transparence des décisions du modèle via des graphiques d'interprétabilité locale et globale.
3. Rédiger une note détaillée de veille technologique MLOps.

## 🗂️ Données Nécessaires (Veille Technologique)

🔗 [Ressources pour la veille](https://drive.google.com/drive/folders/1RJQPqPf-XqB-nLYNcNyLLqdxZe58dHc4?usp=sharing)
⚠️ **Instruction** : À télécharger dans le dossier `Data/Images` si la section concernant la veille doit être générée/illustrée.

## 🛠️ Outils et Environnement

Environnement préconisé : `python ^3.11`

### Librairies principales :

Identiques au Projet 7, avec une forte composante front-end via **Streamlit** :

- `streamlit` (^1.29.0)
- `lightgbm` (^4.2.0), `shap` (^0.44.0), `evidently` (^0.4.13), `mlflow` (^2.9.2)
