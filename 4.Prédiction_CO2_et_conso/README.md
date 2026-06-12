# 🏢 Prédiction CO2 & Énergie — Bâtiments de Seattle

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-orange?style=flat&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-green?style=flat)
![LightGBM](https://img.shields.io/badge/LightGBM-yellow?style=flat)
![SHAP](https://img.shields.io/badge/SHAP-explicabilit%C3%A9-brightgreen?style=flat)

Projet de Data Science réalisé dans le cadre de la formation OpenClassrooms.

## 🎯 Objectif

Prédire les **émissions de CO2** et la **consommation énergétique** des bâtiments non résidentiels de la ville de Seattle, à partir de leurs caractéristiques structurelles — sans recourir aux relevés de consommation annuels, coûteux à collecter.

---

## 📦 Données

- **Source** : [Seattle Building Energy Benchmarking](https://www.seattle.gov/environment/climate-change/buildings-and-energy/energy-benchmarking) (données publiques, ville de Seattle)
- Caractéristiques des bâtiments : surface, type d'usage, année de construction, nombre d'étages, etc.
- **2 cibles** : émissions CO2 (`CO2_Prediction.ipynb`) et consommation énergétique (`Energy_Prediction.ipynb`)

---

## 🔍 Démarche

### 1. `Data_Analysis.ipynb` — Exploration & préparation

- Analyse exploratoire, détection et traitement des outliers
- Étude des corrélations (matrices, heatmaps)
- **ACP avec cercles de corrélation** pour visualiser les relations entre variables
- Construction de pipelines Scikit-learn pour le prétraitement

### 2. `CO2_Prediction.ipynb` — Prédiction des émissions CO2

- Comparaison de 10 modèles de régression via **pipelines Scikit-learn**
- 3 phases de modélisation :
  - Données brutes (baseline)
  - Avec **feature engineering** (+61% de R² sur le meilleur modèle)
  - Avec **transformation de la target** (normalisation des distributions asymétriques)
- Optimisation du modèle retenu par hyperparameter tuning

### 3. `Energy_Prediction.ipynb` — Prédiction de la consommation énergétique

- Modélisation avec **GradientBoostingRegressor**
- Analyse de la **feature importance** native du modèle
- Explicabilité approfondie avec **SHAP**
- **Analyse ANOVA** pour valider statistiquement les différences de performance entre modèles

---

## 📊 Résultats — Prédiction CO2

### Comparaison des modèles (données brutes vs features enrichies)

| Modèle          | R² brut | R² + features | Gain     |
| --------------- | ------- | ------------- | -------- |
| **Extra Trees** | 0.36    | **0.58**      | **+61%** |
| Gradient Boost  | 0.17    | 0.53          | +212%    |
| Random Forest   | 0.31    | 0.52          | +68%     |
| XGBoost         | 0.12    | 0.51          | +325%    |
| LightGBM        | 0.21    | 0.39          | +86%     |
| Lasso           | 0.27    | —             | —        |
| Ridge           | 0.26    | —             | —        |
| SVM             | -0.07   | -0.08         | —        |

### Modèle retenu après optimisation

| Modèle                 | R²       | NMAE   |
| ---------------------- | -------- | ------ |
| Extra Trees (optimisé) | **0.52** | -54.78 |

> **Conclusion clé** : le feature engineering est l'étape la plus déterminante du projet. Sans features enrichies, les meilleurs modèles plafonnent à R²~0.36. Avec features créées, Extra Trees atteint **R²=0.58**, soit +61% de performance.

---

## 💡 Impact du feature engineering

La transformation des features existantes (interactions, ratios, encodages adaptés) a permis des gains massifs sur tous les modèles ensemblistes :

- Extra Trees : **+61%**
- Gradient Boost : **+212%**
- XGBoost : **+325%**

Les modèles linéaires (Lasso, Ridge, ElasticNet) ont été écartés dès la phase initiale, leurs scores R² (~0.26-0.27) indiquant une relation non-linéaire entre les features et la cible.

---

## 🛠️ Stack technique

- **Python** — Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning** — Scikit-learn (pipelines, LinearRegression, ElasticNet, Lasso, Ridge, SVR, ExtraTreesRegressor, GradientBoostingRegressor, RandomForestRegressor), XGBoost, LightGBM
- **Explicabilité** — SHAP
- **Statistiques** — ANOVA (validation des performances inter-modèles)
- **Réduction de dimension** — ACP (analyse en composantes principales)
- **Environnement** — Jupyter Notebook

---

## 📂 Structure du projet

```
Project 4/
├── Notebooks/
│   ├── Data_Analysis.ipynb
│   ├── CO2_Prediction.ipynb
│   └── Energy_Prediction.ipynb
├── Project_presentation.pptx
├── pyproject.toml
└── README.md
```

---

## 🔗 Liens

- [Retour au portfolio](https://github.com/Heneault-IA/Projects)
