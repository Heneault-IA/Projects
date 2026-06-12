# 📊 Dashboard Scoring Crédit & Veille RandAugment

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-dashboard-red?style=flat&logo=streamlit&logoColor=white)
![SHAP](https://img.shields.io/badge/SHAP-explicabilit%C3%A9-brightgreen?style=flat)
![VGG16](https://img.shields.io/badge/VGG16-Transfer%20Learning-orange?style=flat)
![RandAugment](https://img.shields.io/badge/RandAugment-State%20of%20Art-purple?style=flat)

Projet de Data Science réalisé dans le cadre de la formation OpenClassrooms — suite du [Projet 7](https://github.com/Heneault-IA/Projects/tree/main/Project%207).

Ce projet se compose de deux parties indépendantes : un **dashboard interactif** de scoring crédit et une **veille technologique** sur RandAugment.

---

## Partie 1 — Dashboard Streamlit : Scoring Crédit

### 🎯 Objectif

Rendre le modèle de scoring crédit du Projet 7 **accessible et explicable** à des utilisateurs non techniques (conseillers bancaires, chargés de clientèle) via une interface web interactive.

### 🖥️ Fonctionnalités

- **Interrogation de l'API REST** (Projet 7) en temps réel
- **Décision claire** : crédit accordé ✅ ou refusé ❌ avec le score de probabilité
- **Explicabilité locale** : affichage des principales variables ayant influencé la décision pour ce client spécifique (SHAP values)
- Interface pensée pour un usage métier, sans nécessiter de connaissances en ML

### 🛠️ Stack

- **Streamlit** — interface web interactive
- **Requests** — appels à l'API Flask (Projet 7)
- **SHAP** — visualisation des features importantes par client
- **Matplotlib / Plotly** — graphiques d'explicabilité

---

## Partie 2 — Veille Technologique : RandAugment

### 🎯 Objectif

Évaluer l'apport de **RandAugment** (technique d'augmentation de données automatisée, Google Brain 2019) par rapport aux approches classiques, sur une tâche de classification d'images avec VGG16.

### 📖 État de l'art

RandAugment simplifie la recherche d'hyperparamètres d'augmentation en réduisant l'espace de recherche à deux paramètres globaux (N et M), là où AutoAugment nécessitait des milliers d'heures de calcul. L'article original démontre des gains significatifs sur ImageNet et CIFAR.

### 📊 Résultats expérimentaux

| Configuration                | Époques | Train Acc. | Val Acc.  | Test Acc. | Temps       |
| ---------------------------- | ------- | ---------- | --------- | --------- | ----------- |
| **Base (sans augmentation)** | 27      | 0.931      | **0.794** | **0.791** | 21m 29s     |
| Data Augmentation classique  | 30      | 0.889      | 0.745     | 0.762     | 23m 11s     |
| RandAugment                  | 23      | 0.869      | 0.739     | 0.768     | **17m 30s** |

> **Conclusion** : sur ce dataset, le modèle de base surpasse les deux variantes d'augmentation. Les images étant déjà suffisamment variées, l'augmentation artificielle introduit du bruit plutôt que de la régularisation. RandAugment présente néanmoins un avantage en **temps d'entraînement** (-19% vs base), ce qui peut justifier son usage dans des contextes contraints en ressources.

> Ce résultat illustre un principe fondamental : les techniques state-of-the-art ne sont pas universellement supérieures — leur bénéfice dépend des caractéristiques du dataset.

### 🛠️ Stack

- **TensorFlow / Keras** — VGG16, fine-tuning, callbacks (EarlyStopping)
- **RandAugment** — implémentation via `tf.keras.layers` ou `imgaug`
- **Matplotlib** — courbes Loss / Accuracy

---

## 📂 Structure du projet

```
Project 8/
├── dashboard/
    ├── pages/
    │   └── 1_Analyse_Critères.py
    ├── Dashboard.py
    └── requirements.txt
├── Technology_Watch_Notebook.ipynb
├── pyproject.toml
├── Project_presentation.pptx
├── Methodological_Note.pdf
├── Original_Article_RandAugment.pdf
└── README.md
```

---

## 🔗 Liens

- [Projet 7 — Scoring Crédit + API REST](https://github.com/Heneault-IA/Projects/tree/main/Project%207)
- [Retour au portfolio](https://github.com/Heneault-IA/Projects)
