# 🍎 Pipeline Big Data — Featurisation d'Images sur AWS

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-Big%20Data-orange?style=flat&logo=apachespark&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20S3-yellow?style=flat&logo=amazonaws&logoColor=white)
![MobileNetV2](https://img.shields.io/badge/MobileNetV2-Transfer%20Learning-red?style=flat)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-red?style=flat&logo=tensorflow)

Projet de Data Science réalisé dans le cadre de la formation OpenClassrooms.

## 🎯 Objectif

Concevoir et déployer un **pipeline de featurisation d'images à grande échelle** sur infrastructure cloud AWS, en combinant **Transfer Learning** (MobileNetV2) et **traitement distribué** (PySpark).

L'objectif n'est pas la classification finale, mais de démontrer la **faisabilité et la scalabilité** d'un tel pipeline dans un contexte Big Data réel.

---

## 📦 Données

- **Source** : [Fruits 360](https://www.kaggle.com/datasets/moltean/fruits) (Kaggle)
- Dataset de photos de fruits classées par catégorie
- Échantillonnage aléatoire de **10 images par catégorie** pour constituer le jeu d'entraînement

---

## 🏗️ Architecture

```
Kaggle (Fruits 360)
        ↓
  Échantillonnage
  (10 img/catégorie)
        ↓
   AWS S3 (stockage
  images + features)
        ↓
   AWS EC2 (instance)
        ↓
  PySpark + MobileNetV2
  (extraction features)
        ↓
  Vecteurs de features
     → PCA → S3
```

---

## 🔍 Démarche

### 1. `Creation_Training_set.ipynb` — Préparation du dataset

- Parcours récursif de l'arborescence du dataset Fruits 360
- **Échantillonnage aléatoire** de 10 images par catégorie
- Constitution d'un jeu d'entraînement équilibré et reproductible
- Upload vers **AWS S3**

### 2. `Pyspark_Notebook.ipynb` — Pipeline distribué sur AWS EC2

- **Extraction de features** avec **MobileNetV2** (pré-entraîné sur ImageNet)
  - Utilisation de la couche avant la tête de classification (`layers[-2].output`)
  - Chaque image → vecteur de features dense
- **Conversion en vecteurs Spark** via UDF et `VectorUDT` pour intégration native dans le DataFrame PySpark
- **Réduction de dimension** avec **PCA** (Spark MLlib)
- Persistance des features réduites sur **AWS S3**

---

## 💡 Choix techniques

**Pourquoi MobileNetV2 ?**
Architecture légère et efficace, idéale pour de l'extraction de features en environnement contraint (instance EC2 sans GPU dédié). Les poids ImageNet fournissent des représentations visuelles riches sans nécessiter de réentraînement.

**Pourquoi PySpark ?**
Le pipeline est conçu pour scaler : en remplaçant l'instance EC2 par un cluster EMR, le même code traiterait des millions d'images sans modification. C'est la démonstration d'une **architecture production-ready**.

**Pourquoi la PCA en sortie ?**
Réduire la dimensionnalité des vecteurs MobileNetV2 avant stockage réduit les coûts S3 et accélère les étapes de modélisation en aval.

---

## 🛠️ Stack technique

- **Cloud** — AWS EC2 (exécution), AWS S3 (stockage)
- **Big Data** — PySpark, Spark MLlib (PCA)
- **Deep Learning** — TensorFlow/Keras, MobileNetV2 (transfer learning)
- **Python** — Pandas, NumPy
- **Environnement** — Jupyter Notebook sur EC2

---

## 📂 Structure du projet

```
Project 9/
├── Notebooks/
│   ├── Creation_Training_set.ipynb
│   └── Pyspark_Notebook.ipynb
├── scripts/
│   ├── bootstrap-emr.sh
│   └── notebook_persitence.json
├── Project_presentation.pptx
└── README.md
```

---

## 🔗 Liens

- [Retour au portfolio](https://github.com/Heneault-IA/Projects)
