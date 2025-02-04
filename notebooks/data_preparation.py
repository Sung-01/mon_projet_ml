import pandas as pd

df = pd.read_csv("/Users/germain.pierroz/Documents/apprentissage_python/mon_projet_ml/data/titanic.csv")
print(df)

print(df.isnull().sum())  # Affiche le nombre de valeurs manquantes par colonne

#Récapitulatif du nettoyage
#	1.	Supprimer les colonnes inutiles (PassengerId, Name, Ticket, Cabin).
#	2.	Remplacer les valeurs manquantes :
#		    Age → Médiane
#		    Embarked → Valeur la plus fréquente
#	3.	Convertir les variables catégorielles (Sex, Embarked) en numériques.
#	4.	Standardiser les variables continues (Age, Fare).
#	5.	Supprimer les doublons.
#	6.	Vérifier et traiter les valeurs aberrantes.