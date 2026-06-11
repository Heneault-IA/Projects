# 🛒 Segmentation Client e-commerce — Clustering & Simulation Temporelle

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-orange?style=flat&logo=scikit-learn&logoColor=white)
![KMeans](https://img.shields.io/badge/KMeans-clustering-blue?style=flat)
![DBSCAN](https://img.shields.io/badge/DBSCAN-clustering-blue?style=flat)
![RFM](https://img.shields.io/badge/RFM-analyse-brightgreen?style=flat)

Projet de Data Science réalisé dans le cadre de la formation OpenClassrooms.

## 🎯 Objectif

Segmenter les clients d'un site e-commerce brésilien (**Olist**) afin de permettre aux équipes marketing de personnaliser leurs actions par profil de clientèle.

Au-delà du clustering statique, le projet répond à une question opérationnelle clé : **à quelle fréquence faut-il réentraîner le modèle pour que la segmentation reste pertinente ?**

---

## 📦 Données

- **Source** : dataset public [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (e-commerce brésilien)
- Historique de commandes, clients, produits et évaluations

---

## 🔍 Démarche

### 1. `Data_Analysis.ipynb` — Exploration & nettoyage

- Analyse exploratoire du dataset Olist
- Nettoyage des données, gestion des valeurs manquantes et des doublons
- Préparation des features pour la modélisation

### 2. `Customers_Segmentation.ipynb` — Modélisation

- Construction des features **RFM** (Récence, Fréquence, Montant)
- Optimisation du nombre de clusters avec **KElbowVisualizer**
- Comparaison d'approches :
  - KMeans standard
  - KMeans avec transformation logarithmique (normalisation des distributions)
  - DBSCAN (clustering par densité, sans nombre de clusters prédéfini)
- **Modèle retenu** : KMeans avec **5 clusters**

### 3. `Simulation_Over_Time.ipynb` — Stabilité temporelle

- Simulation semaine par semaine de l'évolution des segments clients
- Mesure de la dérive des clusters dans le temps via des métriques de similarité
- **Conclusion** : réentraînement recommandé toutes les **2 semaines** pour maintenir la cohérence de la segmentation

---

## 👥 Résultats — Les 5 segments clients

| Segment               | Profil type                                                   |
| --------------------- | ------------------------------------------------------------- |
| 0 Clients à réactiver | commande il y a très longtemps mais avec bonne expérience     |
| 1 Clients à récupérer | commande assez récente mais avec une mauvaise expérience      |
| 2 Très bons clients   | commande assez récente à gros montant avec bonne satisfaction |
| 3 Clients à fidéliser | commande récente, et avec une bonne expérience                |
| 4 Clients réguliers   | plusieurs commandes et bons retours => sponsors               |

---

## 💡 Valeur métier

La segmentation RFM permet aux équipes marketing de :

- Cibler les **clients à risque** avec des offres de rétention avant qu'ils ne partent
- Récompenser les **champions** avec des programmes de fidélité
- Adapter les communications selon le cycle de vie client

La simulation temporelle apporte une **recommandation opérationnelle concrète** : sans réentraînement régulier (toutes les 2-4 semaines), les segments dérivent et les actions marketing perdent en pertinence.

---

## 🛠️ Stack technique

- **Python** — Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning** — Scikit-learn (KMeans, DBSCAN)
- **Visualisation clustering** — Yellowbrick (KElbowVisualizer)
- **Analyse RFM** — feature engineering manuel
- **Environnement** — Jupyter Notebook

---

## 📂 Structure du projet

```
Project 5/
├── Notebooks/
│   ├── Data_Analysis.ipynb
│   ├── Customers_Segmentation.ipynb
│   └── Simulation_Over_Time.ipynb
├── Project_presentation.pptx
└── README.md
```

---

## 🔗 Liens

- [Retour au portfolio](https://github.com/Heneault-IA/Projects)
