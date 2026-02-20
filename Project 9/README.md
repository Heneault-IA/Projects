# ☁️ Projet 9 : Architecture Big Data sur le Cloud (AWS) - Traitement d'Images

## 🎯 Objectif du Projet

L'objectif est de mettre en place un environnement Big Data complet et scalable sur Amazon Web Services (AWS) pour accomplir une tâche de prétraitement et de "featurization" d'un très grand volume d'images de fruits. L'architecture repose sur des clusters **Amazon EMR** et l'utilisation du framework de calcul distribué **PySpark**.

## 🗂️ Données Nécessaires

🔗 [Kaggle : Fruits 360 Dataset](https://www.kaggle.com/datasets/moltean/fruits)

⚠️ **Instruction** : Télécharger les données et les placer dans le dossier local `Data/fruits-360_dataset/fruits-360/Training`. Lors du déploiement, ces données sont envoyées sur un bucket S3.

## 🛠️ Librairies Requises

- `tensorflow==2.11.0`
- `pandas==1.2.5`
- `pillow`
- `pyarrow` / `wheel` / `boto3` / `fsspec`

## 📜 Scripts et Déploiement

- `bootstrap-emr.sh` : Script d'initialisation pour le cluster EMR (installation des dépendances au démarrage).
- `notebook_persitence.json` : Fichier de paramètres pour le cluster EMR, utilisé pour conserver la persistance du notebook créé sur JupyterHub.

## 📓 Notebooks

- `Pyspark_Notebook.ipynb` : Notebook exécuté sur le JupyterHub du cluster EMR pour le traitement distribué des images.
- `Création_Training_set.ipynb` : Notebook de préparation d'un jeu de données de test en local.

## 📈 Résultats

Les données extraites (features images transformées via un réseau de neurones pré-entraîné) sont enregistrées sous format **Parquet** (`paquet's files`) à l'issue de l'exécution sur le cluster PySpark.
