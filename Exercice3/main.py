from csv_reader import *

try:
    articles = charger_csv("Exercice3/articles.csv")

    print("Importation réussie :")

    for article in articles:
        print(article)

except FichierIntrouvableException as e:
    print("Erreur :", e)

except LigneInvalideException as e:
    print("Erreur :", e)

except PrixNegatifException as e:
    print("Erreur :", e)

except CsvException as e:
    print("Erreur CSV :", e)

except OSError as e:
    print("Erreur de lecture :", e)