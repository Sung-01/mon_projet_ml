# Projet ML - Prédiction de la Survie sur le Titanic

Ce projet analyse le dataset du Titanic pour prédire la survie des passagers à l'aide d'une régression logistique.

## Structure du projet

mon_projet_ml/
├── data/
│   ├── dataset.csv          # Données brutes
│   └── dataset_clean.csv    # Données nettoyées
├── notebooks/
│   └── exploration.ipynb    # Analyse et visualisation
├── scripts/
│   ├── data_preparation.py  # Nettoyage des données
│   └── train_model.py       # Entraînement et évaluation du modèle
├── results/
│   ├── model.pkl            # Modèle sauvegardé
│   └── predictions.csv      # Prédictions exportées
├── README.md                # Présentation du projet
└── requirements.txt         # Dépendances du projet

## Installation et exécution

1. Cloner le dépôt et se placer dans le dossier du projet :
   ```bash
   git clone <URL_DU_DEPOT>
   cd mon_projet_ml

	2.	Installer les dépendances :

pip install -r requirements.txt


	3.	Exécuter les scripts dans l’ordre :
	•	Nettoyage des données : python scripts/data_preparation.py
	•	Exploration des données : ouvrir notebooks/exploration.ipynb
	•	Entraînement et évaluation du modèle : python scripts/train_model.py

Auteur

Sung-01