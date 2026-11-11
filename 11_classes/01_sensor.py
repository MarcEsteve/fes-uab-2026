###
# 11 - Classes i objectes
# Dues sessions de teoria d'1 hora. Projecte de monitoratge de sensors.
###

# OBJECTIUS D'APRENENTATGE
# - Distingir una classe de les seves instàncies.
# - Construir objectes amb __init__ i entendre el paper de self.
# - Agrupar atributs i mètodes que gestionen el mateix estat.
# - Mantenir les lectures de cada sensor independents i validades.

from math import isfinite


# 1. DE LES DADES A UN OBJECTE
# Fins ara podíem representar un sensor amb un diccionari.
# Una classe defineix les dades i les operacions dels seus objectes.
# Sensor és la classe. Sensor("T1", "°C") crea una instància concreta.
# Els atributs emmagatzemen estat. Els mètodes són funcions de la classe.

class Sensor:
    """Agrupa la identificació i l'històric d'un sensor simulat."""

    def __init__(self, nom, unitat):
        """Inicialitza una instància amb un històric buit propi."""
        # Python crida __init__ quan construïm l'objecte.
        # self identifica la instància que està executant el mètode.
        self.nom = nom
        self.unitat = unitat
        # Aquesta llista es crea per a cada objecte, dins d'__init__.
        self.lectures = []

    # 2. MÈTODES I CANVIS D'ESTAT
    # En sensor.registrar(22.5), Python passa sensor com a self.
    # La validació es fa abans de modificar l'històric.
    def registrar(self, valor):
        """Afegeix un int o float finit, o llança ValueError."""
        # bool és un subtipus d'int, però True no és una mesura.
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("La lectura ha de ser un nombre.")
        # Els enters són finits. Els floats també poden ser inf o nan.
        if isinstance(valor, float) and not isfinite(valor):
            raise ValueError("La lectura ha de ser finita.")
        self.lectures.append(valor)

    # 3. MÈTODES QUE CONSULTEN L'ESTAT
    # None representa l'absència de lectura. 0 és una mesura vàlida.
    def ultima_lectura(self):
        """Retorna l'última lectura, o None si l'històric és buit."""
        if not self.lectures:
            return None
        return self.lectures[-1]

    def mitjana(self):
        """Retorna la mitjana aritmètica, o None si no hi ha lectures."""
        if not self.lectures:
            return None
        return sum(self.lectures) / len(self.lectures)


def main():
    """Mostra construcció, estat independent i consultes."""
    # Primera sessió. Constructor, atributs, mètodes i dues instàncies.
    temperatura = Sensor("T1", "°C")
    humitat = Sensor("H1", "%")
    print(temperatura.nom, temperatura.unitat)  # T1 °C
    print(temperatura.ultima_lectura())  # None

    temperatura.registrar(20.0)
    temperatura.registrar(24.0)
    humitat.registrar(55.0)
    print(temperatura.lectures)  # [20.0, 24.0]
    print(humitat.lectures)  # [55.0]

    # Segona sessió. Consultes, validació i evolució de l'estat.
    print(temperatura.ultima_lectura())  # 24.0
    print(temperatura.mitjana())  # 22.0
    try:
        temperatura.registrar("error")
    except ValueError as error:
        print(error)
    print(temperatura.lectures)  # [20.0, 24.0]
    # L'històric conserva les lectures acceptades.

    # ACTIVITAT GUIADA
    # Abans d'executar les línies següents, prediu els dos historials.
    # Dibuixa dues caixes, una per instància, amb nom, unitat i lectures.
    temperatura.registrar(0)
    print(temperatura.ultima_lectura())  # 0
    print(humitat.ultima_lectura())  # 55.0
    # Canviar temperatura no modifica humitat. Comprova també un sensor buit.
    tensio = Sensor("V1", "V")
    print(tensio.mitjana())  # None

# ENGINYERIA DEL PROGRAMARI
# Sensor té la responsabilitat de gestionar les seves lectures.
# Centralitzar la validació a registrar facilita la mantenibilitat.
# En aquest primer model lectures és públic. Utilitza registrar per afegir
# mesures i conservar la validació. El bloc opcional 15 amplia l'encapsulació.
# La composició de diversos sensors arriba al bloc 12.
# Exercicis a 01_sensor_exercicis.py i solucions a 01_sensor_solucions.py.

if __name__ == "__main__":
    main()
