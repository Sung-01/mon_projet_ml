import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Lecture du dataset
df = pd.read_csv("/Users/germain.pierroz/Documents/apprentissage_python/mon_projet_ml/data/titanic.csv")
print("Aperçu du dataset initial :")
print(df.head())

# 2. Suppression des colonnes inutiles
colonnes_a_supprimer = ['PassengerId', 'Name', 'Ticket', 'Cabin']
df.drop(columns=colonnes_a_supprimer, inplace=True, errors='ignore')

# 3. Traitement des valeurs manquantes
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])


# 4. Transformation des variables catégorielles
df['Sex'] = df['Sex'].map({'female': 0, 'male': 1})

# Transformation de 'Embarked' en variables dummy (on peut choisir de supprimer une des colonnes pour éviter la redondance)
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# 5. Standardisation des variables continues
scaler = StandardScaler()
colonnes_continues = ['Age', 'Fare']
df[colonnes_continues] = scaler.fit_transform(df[colonnes_continues])

# 6. Suppression des doublons
df.drop_duplicates(inplace=True)

# Affichage des informations de vérification
print("\nNombre de valeurs manquantes par colonne après nettoyage :")
print(df.isnull().sum())

print("\nAperçu du dataset nettoyé :")
print(df.head())

# Optionnel : sauvegarde du dataset nettoyé pour une utilisation ultérieure
df.to_csv("/Users/germain.pierroz/Documents/apprentissage_python/mon_projet_ml/data/dataset_clean.csv", index=False)