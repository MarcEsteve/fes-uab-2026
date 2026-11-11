###
# SOLUCIONS - Disseny i composició
# Exemple autònom. Sensor valida una lectura i el sistema coordina sensors.
###

from math import isfinite


class Sensor:
    """Representa un sensor amb un històric de nombres finits."""

    def __init__(self, nom, unitat):
        """Crea un sensor amb un històric independent."""
        self.nom = nom
        self.unitat = unitat
        self.lectures = []

    def registrar(self, valor):
        """Valida abans de modificar l'històric."""
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("La lectura ha de ser un nombre.")
        if isinstance(valor, float) and not isfinite(valor):
            raise ValueError("La lectura ha de ser finita.")
        self.lectures.append(valor)

    def ultima_lectura(self):
        """Retorna l'última lectura o None."""
        if not self.lectures:
            return None
        return self.lectures[-1]


class SistemaMonitoratge:
    """Agrupa sensors i en consulta l'estat actual."""

    # Exercici 1 - Bàsic - Organitzar sensors
    def __init__(self):
        """Crea el registre de sensors buit."""
        self.sensors = {}

    def afegir_sensor(self, sensor):
        """Rebutja noms duplicats abans de canviar el registre."""
        if sensor.nom in self.sensors:
            raise ValueError("Ja existeix un sensor amb aquest nom.")
        self.sensors[sensor.nom] = sensor

    # Exercici 2 - Bàsic - Delegar el registre
    def registrar(self, nom, valor):
        """Localitza el sensor i li delega la validació i el registre."""
        if nom not in self.sensors:
            raise ValueError("El sensor no existeix.")
        self.sensors[nom].registrar(valor)

    # Exercici 3 - Intermedi - Produir un resum
    def resum(self):
        """Retorna l'última lectura i la unitat de cada sensor."""
        files = []
        for sensor in self.sensors.values():
            files.append({
                "sensor": sensor.nom,
                "unitat": sensor.unitat,
                "valor": sensor.ultima_lectura(),
            })
        return files

    # Exercici 4 - Repte opcional - Seleccionar alarmes
    def alarmes(self, unitat, llindar):
        """Selecciona sensors d'una unitat que superen el llindar."""
        noms = []
        for sensor in self.sensors.values():
            lectura = sensor.ultima_lectura()
            if sensor.unitat == unitat and lectura is not None:
                if lectura > llindar:
                    noms.append(sensor.nom)
        return noms


def main():
    """Executa els exercicis i mostra els casos límit."""
    print("Exercici 1")
    sistema = SistemaMonitoratge()
    print(len(sistema.sensors))  # 0
    sistema.afegir_sensor(Sensor("T1", "°C"))
    sistema.afegir_sensor(Sensor("H1", "%"))
    print(list(sistema.sensors))  # ['T1', 'H1']
    try:
        sistema.afegir_sensor(Sensor("T1", "°C"))
    except ValueError:
        print("Nom duplicat")

    print("Exercici 2")
    sistema.registrar("T1", 20.0)
    sistema.registrar("T1", 24.0)
    sistema.registrar("H1", 50.0)
    print(sistema.sensors["T1"].ultima_lectura())  # 24.0
    print(sistema.sensors["H1"].ultima_lectura())  # 50.0
    for nom, valor in [("V1", 3.3), ("T1", "error")]:
        try:
            sistema.registrar(nom, valor)
        except ValueError:
            print("Registre rebutjat")
    print(sistema.sensors["T1"].ultima_lectura())  # 24.0

    print("Exercici 3")
    resum_sistema = SistemaMonitoratge()
    print(resum_sistema.resum())  # []
    resum_sistema.afegir_sensor(Sensor("T1", "°C"))
    resum_sistema.afegir_sensor(Sensor("H1", "%"))
    resum_sistema.registrar("T1", 22.5)
    print(resum_sistema.resum())
    # UML. SistemaMonitoratge -- 0..* Sensor.
    # El sistema conté zero o diversos sensors. Sensor pot existir per si sol.

    print("Exercici 4")
    alarmes_sistema = SistemaMonitoratge()
    for nom, unitat in [("T1", "°C"), ("T2", "°C"), ("H1", "%"),
                        ("T3", "°C")]:
        alarmes_sistema.afegir_sensor(Sensor(nom, unitat))
    alarmes_sistema.registrar("T1", 28.0)
    alarmes_sistema.registrar("T2", 25.0)
    alarmes_sistema.registrar("H1", 70.0)
    print(alarmes_sistema.alarmes("°C", 25.0))  # ['T1']
    print(alarmes_sistema.alarmes("V", 3.0))  # []
    print(SistemaMonitoratge().alarmes("°C", 25.0))  # []
    # La unitat dona sentit físic al llindar i evita barrejar % amb °C.


if __name__ == "__main__":
    main()
