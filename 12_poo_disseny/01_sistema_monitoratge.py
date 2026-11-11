###
# 12 - Disseny orientat a objectes i composició
# Una sessió de teoria d'1 hora. Projecte de monitoratge de sensors.
###

# OBJECTIUS D'APRENENTATGE
# - Assignar una responsabilitat concreta a cada classe.
# - Construir un sistema que contingui objectes Sensor.
# - Distingir relacions entre objectes i interpretar un UML introductori.
# - Validar identificadors i generar un resum coherent.

from math import isfinite


# 1. RESPONSABILITAT D'UN SENSOR
# Recuperem el model del bloc 11. Es defineix aquí perquè aquest exemple
# es pugui executar de manera independent. A un projecte més gran el
# situaríem en un mòdul compartit, aplicant el bloc 08.
class Sensor:
    """Conserva i valida l'històric d'un sol sensor."""

    def __init__(self, nom, unitat):
        """Construeix un sensor sense lectures."""
        self.nom = nom
        self.unitat = unitat
        self.lectures = []

    def registrar(self, valor):
        """Afegeix un nombre finit o llança ValueError."""
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("La lectura ha de ser un nombre.")
        if isinstance(valor, float) and not isfinite(valor):
            raise ValueError("La lectura ha de ser finita.")
        self.lectures.append(valor)

    def ultima_lectura(self):
        """Retorna l'última lectura o None si encara no n'hi ha."""
        if not self.lectures:
            return None
        return self.lectures[-1]

    def mitjana(self):
        """Retorna la mitjana de l'històric o None."""
        if not self.lectures:
            return None
        return sum(self.lectures) / len(self.lectures)


# 2. COMPOSICIÓ D'OBJECTES
# SistemaMonitoratge conté objectes Sensor en un diccionari.
# La clau és el nom únic i el valor és l'objecte complet.
# El sistema localitza el sensor. El sensor valida i desa la mesura.
# Aquesta delegació evita repetir la validació a cada classe.
class SistemaMonitoratge:
    """Organitza sensors per nom i coordina el registre de lectures."""

    def __init__(self):
        """Crea un sistema sense sensors."""
        self.sensors = {}

    def afegir_sensor(self, sensor):
        """Afegeix un sensor i rebutja un nom que ja existeixi."""
        if sensor.nom in self.sensors:
            raise ValueError("Ja existeix un sensor amb aquest nom.")
        self.sensors[sensor.nom] = sensor

    def registrar(self, nom, valor):
        """Envia una lectura al sensor indicat pel seu nom."""
        if nom not in self.sensors:
            raise ValueError("El sensor no existeix.")
        self.sensors[nom].registrar(valor)

    def resum(self):
        """Retorna una fila per sensor, en ordre d'incorporació."""
        files = []
        for sensor in self.sensors.values():
            files.append({
                "sensor": sensor.nom,
                "unitat": sensor.unitat,
                "valor": sensor.ultima_lectura(),
            })
        return files


# 3. UML INTRODUCTORI
# Un diagrama de classes descriu classes, atributs, mètodes i relacions.
# Cada caixa té tres parts. Nom de classe, atributs i mètodes.
# El notebook mostra les caixes i la relació amb multiplicitat 0..*.
# Un SistemaMonitoratge pot contenir zero, un o diversos sensors.
# Fem servir composició d'objectes en codi. En UML dibuixem una associació
# simple perquè el sensor es crea fora i pot existir sense el sistema.
# El diamant ple de composició UML implicaria propietat exclusiva i un
# cicle de vida dependent que aquest model senzill encara no imposa.


def main():
    """Construeix un sistema amb dos sensors i mostra el resum."""
    sistema = SistemaMonitoratge()
    print(sistema.resum())  # []
    sistema.afegir_sensor(Sensor("T1", "°C"))
    sistema.afegir_sensor(Sensor("H1", "%"))
    sistema.registrar("T1", 22.5)
    sistema.registrar("T1", 23.0)
    print(sistema.resum())
    # [{'sensor': 'T1', 'unitat': '°C', 'valor': 23.0},
    #  {'sensor': 'H1', 'unitat': '%', 'valor': None}]

    try:
        sistema.afegir_sensor(Sensor("T1", "°C"))
    except ValueError as error:
        print(error)
    try:
        sistema.registrar("V1", 3.3)
    except ValueError as error:
        print(error)

    # ACTIVITAT GUIADA
    # Localitza quin objecte ha de rebutjar cadascuna de les dues entrades.
    # Quina classe canviaries per afegir una comprovació de lectura?
    # Quina classe canviaries per impedir noms duplicats?
    # La responsabilitat única facilita localitzar cada canvi.


# IMPRESCINDIBLE
# Relacions entre objectes, responsabilitats, delegació i composició.
# AMPLIACIÓ
# L'herència es desenvolupa al bloc opcional 15.
# Exercicis a 01_sistema_monitoratge_exercicis.py i resolucions al fitxer
# 01_sistema_monitoratge_solucions.py. El bloc 13 provarà aquest model.

if __name__ == "__main__":
    main()
