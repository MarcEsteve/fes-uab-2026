###
# SOLUCIONS (mòduls)
###

# Exercici 1 - Bàsic. Magnitud d'una mesura
import math as matematiques

# Exercici 2 - Bàsic. Conversions reutilitzables
import conversions as conv

# Exercici 3 - Intermedi. Resum d'una xarxa de sensors
from sensors import mitjana


# Exercici 4 - Repte opcional. Un programa reutilitzable
def informe_sensor(nom, lectures):
    """Retorna un resum amb el nom, el nombre de lectures i la mitjana."""
    return {"nom": nom, "nombre": len(lectures), "mitjana": mitjana(lectures)}


def main():
    """Executa les demostracions dels quatre exercicis."""
    print("Exercici 1")
    x = 3.0
    y = 4.0
    print(matematiques.sqrt(x * x + y * y))  # 5.0
    print(matematiques.sqrt(0.0 * 0.0 + 0.0 * 0.0))  # 0.0

    print("Exercici 2")
    temperatures = [-10.0, 0.0, 25.0]
    tensions_mv = [0, 3300, 5000]
    temperatures_k = []
    for temperatura in temperatures:
        temperatures_k.append(conv.celsius_a_kelvin(temperatura))
    tensions_v = []
    for tensio in tensions_mv:
        tensions_v.append(conv.milivolts_a_volts(tensio))
    print(temperatures_k)  # [263.15, 273.15, 298.15]
    print(tensions_v)  # [0.0, 3.3, 5.0]
    # Si una entrada és buida, el bucle no afegeix elements a la llista.

    print("Exercici 3")
    dades = {"T1": [20.0, 22.0], "T2": [18.0], "T3": []}
    mitjanes = {}
    for identificador, lectures in dades.items():
        mitjanes[identificador] = mitjana(lectures)
    print(mitjanes)  # {'T1': 21.0, 'T2': 18.0, 'T3': None}

    print("Exercici 4")
    print(informe_sensor("T1", [20.0, 22.0]))
    print(informe_sensor("T0", []))


if __name__ == "__main__":
    main()
