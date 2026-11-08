import unittest
from csv_reader import *


class TestCSV(unittest.TestCase):

    def test_fichier_absent(self):
        with self.assertRaises(FichierIntrouvableException):
            charger_csv("absent.csv")

    def test_prix_texte(self):
        with open("test.csv", "w") as f:
            f.write("1;Clavier;abc")

        with self.assertRaises(LigneInvalideException):
            charger_csv("test.csv")

    def test_prix_negatif(self):
        with open("test.csv", "w") as f:
            f.write("1;Souris;-50")

        with self.assertRaises(PrixNegatifException):
            charger_csv("test.csv")

    def test_ligne_invalide(self):
        with open("test.csv", "w") as f:
            f.write("1;Clavier")

        with self.assertRaises(LigneInvalideException):
            charger_csv("test.csv")


if __name__ == "__main__":
    unittest.main()