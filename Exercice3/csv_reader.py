import os
import csv


# Exception principale
class CsvException(Exception):
    pass


# Exceptions personnalisées
class FichierIntrouvableException(CsvException):
    pass


class LigneInvalideException(CsvException):
    pass


class PrixNegatifException(CsvException):
    pass


# Fonction de lecture du fichier CSV
def charger_csv(chemin):

    if not os.path.exists(chemin):
        raise FichierIntrouvableException("Fichier CSV introuvable.")

    articles = []

    with open(chemin, "r", encoding="utf-8") as fichier:

        lecteur = csv.reader(fichier, delimiter=";")

        for numero, ligne in enumerate(lecteur, start=1):

            if not ligne:
                continue

            if len(ligne) != 3:
                raise LigneInvalideException(
                    f"Ligne {numero} : nombre de colonnes invalide."
                )

            identifiant, nom, prix = ligne

            try:
                prix = float(prix)
            except ValueError:
                raise LigneInvalideException(
                    f"Ligne {numero} : le prix doit être numérique."
                )

            if prix <= 0:
                raise PrixNegatifException(
                    f"Ligne {numero} : le prix doit être positif."
                )

            articles.append({
                "id": identifiant,
                "nom": nom,
                "prix": prix
            })

    return articles