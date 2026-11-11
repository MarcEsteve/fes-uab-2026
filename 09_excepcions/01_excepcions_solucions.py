###
# SOLUCIONS (excepcions)
###

import math
from pathlib import Path
from tempfile import TemporaryDirectory


# Exercici 1 - Bàsic. Conversió segura de tensions
def mostrar_tensions(tensions):
    """Mostra les tensions convertides o un missatge d'error."""
    for text in tensions:
        try:
            tensio = float(text)
        except ValueError:
            print("Tensió incorrecta")
        else:
            print(tensio)


# Exercici 2 - Bàsic. Humitat amb contracte
def validar_humitat(text):
    """Retorna una humitat finita de 0 a 100 o genera ValueError."""
    humitat = float(text)
    if not math.isfinite(humitat):
        raise ValueError("La humitat ha de ser finita.")
    if humitat < 0 or humitat > 100:
        raise ValueError("La humitat ha d'estar entre 0 i 100.")
    return humitat


# Exercici 3 - Intermedi. Fitxer absent i finalització
def mostrar_fitxer(ruta):
    """Intenta llegir un fitxer i informa sempre de la finalització."""
    try:
        with open(ruta, encoding="utf-8") as fitxer:
            contingut = fitxer.read()
    except FileNotFoundError:
        print("Fitxer absent")
    else:
        print(contingut)
    finally:
        print("Intent acabat")


# Exercici 4 - Repte opcional. Filtrar lectures de temperatura
def validar_temperatura(text):
    """Retorna una temperatura finita dins del rang simulat [-40, 85]."""
    temperatura = float(text)
    if not math.isfinite(temperatura):
        raise ValueError("La temperatura ha de ser finita.")
    if temperatura < -40 or temperatura > 85:
        raise ValueError("Temperatura fora del rang simulat.")
    return temperatura


def filtrar_temperatures(textos):
    """Retorna les temperatures vàlides i el nombre de rebutjades."""
    valides = []
    rebutjades = 0
    for text in textos:
        try:
            temperatura = validar_temperatura(text)
        except ValueError:
            rebutjades += 1
        else:
            valides.append(temperatura)
    return valides, rebutjades


def main():
    """Executa els quatre exercicis amb dades i casos límit."""
    print("Exercici 1")
    mostrar_tensions(["3.3", "avaria", "0"])

    print("Exercici 2")
    entrades = ["0", "100", "45.5", "-1", "101", "nan", "inf", "error"]
    for text in entrades:
        try:
            humitat = validar_humitat(text)
        except ValueError as error:
            print(f"Rebutjada {text!r}: {error}")
        else:
            print(humitat)

    print("Exercici 3")
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "absent.txt"
        mostrar_fitxer(ruta)
        with open(ruta, "w", encoding="utf-8") as fitxer:
            fitxer.write("T1=21.5")
        mostrar_fitxer(ruta)

    print("Exercici 4")
    print(filtrar_temperatures(["-40", "21.5", "85", "86", "avaria", "nan"]))
    print(filtrar_temperatures([]))  # ([], 0)
    print(filtrar_temperatures(["nan", "inf"]))  # ([], 2)


if __name__ == "__main__":
    main()
