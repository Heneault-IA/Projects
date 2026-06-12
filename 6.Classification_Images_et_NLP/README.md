# 🛍️ Classification Automatique de Produits — NLP & Computer Vision

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-BERT%20%7C%20USE%20%7C%20TF--IDF-blue?style=flat)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-VGG16%20%7C%20SIFT-orange?style=flat)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-red?style=flat&logo=tensorflow)
![Transfer Learning](https://img.shields.io/badge/Transfer%20Learning-VGG16-purple?style=flat)

Projet de Data Science réalisé dans le cadre de la formation OpenClassrooms.

## 🎯 Objectif

Évaluer la **faisabilité d'une classification automatique** de produits e-commerce dans leurs catégories, à partir de leurs **descriptions textuelles** et de leurs **photos**, sans intervention humaine.

---

## 📦 Données

- Catalogue de produits avec descriptions textuelles et photos associées
- Plusieurs catégories de produits à prédire automatiquement

---

## 🔍 Démarche

### 1. `Data_Analysis.ipynb` — Exploration textuelle

- Analyse des descriptions produits : tokenisation, suppression des stop words
- Visualisation des mots les plus fréquents (word clouds, distributions)
- Identification des patterns linguistiques par catégorie

### 2. `Texts_Faisability.ipynb` — Faisabilité par le texte

Comparaison de 6 approches NLP, du plus classique au plus avancé :

| Approche                         | Type               | ARI          |
| -------------------------------- | ------------------ | ------------ |
| **TF-IDF**                       | Statistique        | **0.490** ✅ |
| Bag-of-Words                     | Statistique        | 0.445        |
| USE (Universal Sentence Encoder) | Embedding neuronal | 0.401        |
| BERT                             | Transformer        | 0.281        |
| Word2Vec                         | Embedding          | 0.118        |
| Doc2Vec                          | Embedding          | 0.108        |

> **Observation clé** : TF-IDF surpasse BERT et USE sur ce dataset. Les descriptions produits étant très techniques et répétitives (vocabulaire de catalogue), les approches statistiques tirent mieux parti de ce signal que les modèles pré-entraînés sur du langage général.

### 3. `Images_Faisability.ipynb` — Faisabilité par les images

- **SIFT** (extraction de points clés locaux) : ARI = 0.063 — approche trop peu discriminante
- **VGG16** (transfer learning, features extraites) : ARI = 0.45 — résultats comparables au texte
- Validation de la séparabilité des clusters via **PCA** et **t-SNE**

### 4. `Images_Classification.ipynb` — Classification avec VGG16

- Fine-tuning de **VGG16** pour la classification multi-classes
- Optimisation du nombre d'époques avec **early stopping** → **26 époques retenues**
- Expérimentation de la **data augmentation** pour améliorer la généralisation
- Suivi des courbes **Loss** et **Accuracy** (train vs validation)

---

## 📊 Synthèse des résultats

| Approche  | Méthode         | ARI       |
| --------- | --------------- | --------- |
| 🥇 Texte  | TF-IDF          | **0.490** |
| 🥈 Images | VGG16 fine-tuné | 0.450     |
| 🥉 Texte  | Bag-of-Words    | 0.445     |
| Texte     | USE             | 0.401     |
| Texte     | BERT            | 0.281     |
| Images    | SIFT            | 0.063     |

**Conclusion** : la classification automatique est **faisable** avec les deux modalités. Le texte (TF-IDF) offre le meilleur rapport performance/complexité. Les images (VGG16) atteignent des performances comparables au prix d'une infrastructure plus lourde. Une approche **multimodale** (texte + image) constituerait la piste d'amélioration naturelle.

---

## 🛠️ Stack technique

- **Python** — Pandas, NumPy, Matplotlib, Seaborn
- **NLP** — NLTK (tokenisation, stop words), Scikit-learn (Bag-of-Words, TF-IDF), Gensim (Word2Vec, Doc2Vec), HuggingFace Transformers (BERT), TensorFlow Hub (USE)
- **Computer Vision** — OpenCV (SIFT), TensorFlow/Keras (VGG16, transfer learning, data augmentation)
- **Réduction de dimension** — PCA, t-SNE
- **Environnement** — Jupyter Notebook, GPU

---

## 📂 Structure du projet

```
Project 6/
├── Notebooks/
│   ├── Data_Analysis.ipynb
│   ├── Texts_Faisability.ipynb
│   ├── Images_Faisability.ipynb
│   └── Images_Classification.ipynb
├── Project_presentation.pptx
└── README.md
```

---

## 🔗 Liens

- [Retour au portfolio](https://github.com/Heneault-IA/Projects)
