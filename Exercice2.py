# Exception principale
class ReservationException(Exception):
    def __init__(self, message):
        super().__init__(message)


# Exceptions personnalisées
class CapaciteDepasseeException(ReservationException):
    pass


class NombreInvalideException(ReservationException):
    pass


class NomClientInvalideException(ReservationException):
    pass


# Classe Evenement
class Evenement:

    def __init__(self, nom, capacite):
        self.nom = nom
        self.capacite = capacite
        self.places_reservees = 0

    # Réserver des places
    def reserver(self, nom_client, nb_places):

        if not nom_client.strip():
            raise NomClientInvalideException("Nom du client requis.")

        if nb_places <= 0:
            raise NombreInvalideException("Nombre de places invalide.")

        if self.places_reservees + nb_places > self.capacite:
            raise CapaciteDepasseeException("Capacité dépassée.")

        self.places_reservees += nb_places

        print(f"Réservation confirmée pour {nom_client} ({nb_places} places).")

    # Afficher les réservations
    def afficher(self):
        print(f"Événement: {self.nom} — {self.places_reservees}/{self.capacite} places réservées")



try:
    event = Evenement("Concert", 5)

    event.reserver("", 2)

    event.afficher()

except ReservationException as e:
    print("Erreur:", e)