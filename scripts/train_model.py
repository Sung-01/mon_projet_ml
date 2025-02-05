import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

# 1. Charger le dataset nettoyé
df = pd.read_csv("/Users/germain.pierroz/Documents/apprentissage_python/mon_projet_ml/data/dataset_clean.csv")  # Assure-toi que le chemin est correct

# 2. Sélection des features (variables explicatives) et de la target (variable à prédire)
# Dans cet exemple, nous allons prédire 'Survived'
# Nous allons utiliser les colonnes: Pclass, Sex, Age, SibSp, Parch, Fare (et éventuellement les variables dummy pour Embarked si présentes)
# Assure-toi d'adapter cette sélection selon ton DataFrame.
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_Q', 'Embarked_S']
X = df[features]
y = df['Survived']

# 3. Division des données en train et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialiser et entraîner le modèle (ici, une régression logistique)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 5. Faire des prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# 6. Évaluer le modèle
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 7. Sauvegarder le modèle dans le dossier results (par exemple, model.pkl)
with open("/Users/germain.pierroz/Documents/apprentissage_python/mon_projet_ml/results/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Exemple sans identifiant, on crée un index:
results_df = pd.DataFrame({
    "Index": X_test.index,
    "Predicted_Survived": y_pred
})

# Chemin du dossier results
results_dir = "/Users/germain.pierroz/Documents/apprentissage_python/mon_projet_ml/results"

# Si le dossier n'existe pas, le créer
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# Ensuite, sauvegarder le fichier CSV
results_df.to_csv(os.path.join(results_dir, "predictions.csv"), index=False)