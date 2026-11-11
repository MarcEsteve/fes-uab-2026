###
# SOLUCIONS - Classes i objectes
# La classe final reuneix els mètodes dels quatre exercicis.
###

from math import isfinite


class Sensor:
    """Gestiona lectures independents per a cada instància."""

    # Exercici 1 - Bàsic - Construcció i instàncies
    def __init__(self, nom, unitat):
        """Crea un sensor amb un històric propi buit."""
        self.nom = nom
        self.unitat = unitat
        self.lectures = []

    # Exercici 2 - Bàsic - Registrar i validar
    def registrar(self, valor):
        """Valida una lectura abans d'afegir-la a l'històric."""
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("La lectura ha de ser un nombre.")
        if isinstance(valor, float) and not isfinite(valor):
            raise ValueError("La lectura ha de ser finita.")
        self.lectures.append(valor)

    # Exercici 3 - Intermedi - Consultar l'estat
    def ultima_lectura(self):
        """Retorna l'última lectura o None."""
        if not self.lectures:
            return None
        return self.lectures[-1]

    def mitjana(self):
        """Retorna la mitjana de les lectures o None."""
        if not self.lectures:
            return None
        return sum(self.lectures) / len(self.lectures)

    # Exercici 4 - Repte opcional - Comptar superacions
    def comptar_superiors(self, llindar):
        """Compta lectures estrictament superiors a un llindar finit."""
        recompte = 0
        for lectura in self.lectures:
            if lectura > llindar:
                recompte += 1
        return recompte


def main():
    """Executa les dades i els casos límit dels enunciats."""
    print("Exercici 1")
    temperatura = Sensor("T1", "°C")
    humitat = Sensor("H1", "%")
    print(temperatura.nom, temperatura.unitat, temperatura.lectures)
    print(humitat.nom, humitat.unitat, humitat.lectures)

    print("Exercici 2")
    temperatura.registrar(20.0)
    temperatura.registrar(24.0)
    humitat.registrar(55.0)
    print(temperatura.lectures)
    print(humitat.lectures)
    for valor_invalid in ["error", True, float("inf")]:
        try:
            temperatura.registrar(valor_invalid)
        except ValueError:
            print("Lectura rebutjada")
    print(temperatura.lectures)
    try:
        temperatura.registrar(float("nan"))
    except ValueError:
        print("Lectura rebutjada")

    print("Exercici 3")
    print(temperatura.ultima_lectura())  # 24.0
    print(temperatura.mitjana())  # 22.0
    tensio = Sensor("V1", "V")
    print(tensio.ultima_lectura())  # None
    print(tensio.mitjana())  # None
    tensio.registrar(0)
    print(tensio.ultima_lectura())  # 0
    print(tensio.mitjana())  # 0.0

    print("Exercici 4")
    sensor = Sensor("T2", "°C")
    for lectura in [20.0, 24.0, 24.0, 30.0]:
        sensor.registrar(lectura)
    print(sensor.comptar_superiors(24.0))  # 1
    print(sensor.comptar_superiors(19.0))  # 4
    print(Sensor("T3", "°C").comptar_superiors(24.0))  # 0
    print(sensor.lectures)  # L'històric es conserva.


if __name__ == "__main__":
    main()
