# Exception personnalisée
class SoldeInsuffisantException(Exception):
    def __init__(self, message):
        super().__init__(message)


# Classe CompteBancaire
class CompteBancaire:

    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde

    # Déposer de l'argent
    def deposer(self, montant):
        if montant > 0:
            self.solde += montant

    # Retirer de l'argent
    def retirer(self, montant):
        if montant > self.solde:
            raise SoldeInsuffisantException(
                "Solde insuffisant pour ce retrait."
            )

        self.solde -= montant

    # Afficher le compte
    def afficher(self):
        print(f"Compte: {self.nom}, Solde: {self.solde}€")



try:
    compte = CompteBancaire("Alice", 100)

    compte.afficher()

    compte.retirer(150)

except SoldeInsuffisantException as e:
    print("Erreur:", e)