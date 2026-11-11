###
# SOLUCIONS - Herència, polimorfisme i encapsulació bàsica
# Ampliació opcional. La classe base reuneix el comportament compartit.
###

from math import isfinite


class Sensor:
    """Sensor general amb validació i consultes comunes."""

    def __init__(self, nom, unitat):
        """Inicialitza identificació i un històric independent."""
        self.nom = nom
        self.unitat = unitat
        self._lectures = []

    def _validar(self, valor):
        """Rebutja valors de tipus incorrecte i floats no finits."""
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("La lectura ha de ser un nombre.")
        if isinstance(valor, float) and not isfinite(valor):
            raise ValueError("La lectura ha de ser finita.")

    def registrar(self, valor):
        """Valida amb el mètode de la instància abans de desar."""
        self._validar(valor)
        self._lectures.append(valor)

    def ultima_lectura(self):
        """Retorna l'última lectura o None."""
        if not self._lectures:
            return None
        return self._lectures[-1]

    def mitjana(self):
        """Retorna la mitjana o None si l'històric és buit."""
        if not self._lectures:
            return None
        return sum(self._lectures) / len(self._lectures)

    def obtenir_lectures(self):
        """Retorna una còpia per conservar el control de l'històric."""
        return self._lectures.copy()


class SensorTemperatura(Sensor):
    """Especialitza el sensor per al rang simulat [-40, 85] °C."""

    def __init__(self, nom):
        """Fixa la unitat i reutilitza la construcció de la base."""
        super().__init__(nom, "°C")

    def _validar(self, valor):
        """Aplica les condicions comunes i el rang de temperatura."""
        super()._validar(valor)
        if not -40 <= valor <= 85:
            raise ValueError("La temperatura ha d'estar entre -40 i 85 °C.")


class SensorHumitat(Sensor):
    """Especialitza el sensor per al rang simulat [0, 100] %."""

    def __init__(self, nom):
        """Fixa la unitat i reutilitza la construcció de la base."""
        super().__init__(nom, "%")

    def _validar(self, valor):
        """Aplica les condicions comunes i el rang d'humitat."""
        super()._validar(valor)
        if not 0 <= valor <= 100:
            raise ValueError("La humitat ha d'estar entre 0 i 100 %.")


class SensorTensio(Sensor):
    """Especialitza el sensor per al rang simulat [0, 5] V."""

    def __init__(self, nom):
        """Fixa la unitat de tensió."""
        super().__init__(nom, "V")

    def _validar(self, valor):
        """Reutilitza la comprovació numèrica i valida el rang."""
        super()._validar(valor)
        if not 0 <= valor <= 5:
            raise ValueError("La tensió ha d'estar entre 0 i 5 V.")


def mostrar_resums(sensors):
    """Consulta tots els sensors mitjançant la mateixa interfície."""
    for sensor in sensors:
        print(sensor.nom, sensor.ultima_lectura(), sensor.mitjana(),
              sensor.unitat)


def main():
    """Executa les dades i els casos límit dels quatre exercicis."""
    # Exercici 1 - Bàsic - Especialitzar la construcció
    print("Exercici 1")
    temperatura = SensorTemperatura("T1")
    humitat = SensorHumitat("H1")
    print(temperatura.nom, temperatura.unitat, temperatura.obtenir_lectures())
    print(humitat.nom, humitat.unitat, humitat.obtenir_lectures())

    # Exercici 2 - Bàsic - Adaptar la validació
    print("Exercici 2")
    for valor in [-40, 85]:
        temperatura.registrar(valor)
    for valor in [0, 100]:
        humitat.registrar(valor)
    print(temperatura.obtenir_lectures())
    print(humitat.obtenir_lectures())
    for sensor, valor in [(temperatura, -41), (temperatura, 86),
                          (humitat, -1), (humitat, 101)]:
        try:
            sensor.registrar(valor)
        except ValueError:
            print("Lectura rebutjada")
    print(temperatura.obtenir_lectures())  # [-40, 85]
    print(humitat.obtenir_lectures())  # [0, 100]
    buit = SensorTemperatura("T0")
    for valor in [True, "25", float("nan"), float("inf")]:
        try:
            buit.registrar(valor)
        except ValueError:
            print("Lectura rebutjada")
    print(buit.obtenir_lectures())  # []

    # Exercici 3 - Intermedi - Polimorfisme i còpies
    print("Exercici 3")
    temperatura = SensorTemperatura("T1")
    humitat = SensorHumitat("H1")
    for valor in [20.0, 24.0]:
        temperatura.registrar(valor)
    for valor in [40.0, 60.0]:
        humitat.registrar(valor)
    sensors = [temperatura, humitat]
    mostrar_resums(sensors)
    copia = temperatura.obtenir_lectures()
    copia.append(999.0)
    print(temperatura.obtenir_lectures())  # [20.0, 24.0]
    print(buit.ultima_lectura())  # None
    print(buit.mitjana())  # None
    # _lectures és d'ús intern per convenció. La còpia protegeix la llista
    # original quan el codi client modifica l'històric que ha consultat.

    # Exercici 4 - Repte opcional - Afegir un tipus de sensor
    print("Exercici 4")
    tensio = SensorTensio("V1")
    tensio.registrar(0.0)
    tensio.registrar(5.0)
    try:
        tensio.registrar(6.0)
    except ValueError:
        print("Lectura rebutjada")
    sensors.append(tensio)
    mostrar_resums(sensors)
    print(tensio.obtenir_lectures())  # [0.0, 5.0]
    # Un sistema pot contenir aquests objectes i cridar registrar sense
    # repetir les validacions de rang. La composició coordina les instàncies
    # i l'herència especialitza el comportament de cada tipus.


if __name__ == "__main__":
    main()
