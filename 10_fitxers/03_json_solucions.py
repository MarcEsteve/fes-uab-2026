###
# SOLUCIONS - JSON
###

import json
from pathlib import Path
from tempfile import TemporaryDirectory


# Exercici 1 - Bàsic - Configuració d'un dispositiu
def desar_configuracio(ruta, configuracio):
    """Desa dades natives de Python en JSON UTF-8."""
    with open(ruta, "w", encoding="utf-8") as fitxer:
        json.dump(configuracio, fitxer, ensure_ascii=False, indent=2)


def llegir_configuracio(ruta):
    """Recupera el valor JSON del fitxer."""
    with open(ruta, "r", encoding="utf-8") as fitxer:
        return json.load(fitxer)


# Exercici 2 - Bàsic - Mitjana d'un històric
def mitjana_historic(ruta):
    """Calcula la mitjana de registres vàlids o None quan no n'hi ha."""
    lectures = llegir_configuracio(ruta)
    if not lectures:
        return None
    suma = 0
    for lectura in lectures:
        suma += lectura["valor"]
    return suma / len(lectures)


# Exercici 3 - Intermedi - Detectar JSON malmès
def carregar_o_informar(ruta):
    """Informa dels errors de fitxer absent o de sintaxi JSON."""
    try:
        return llegir_configuracio(ruta)
    except FileNotFoundError:
        print("Fitxer absent")
    except json.JSONDecodeError:
        print("JSON invàlid")
    return None


# Exercici 4 - Repte opcional - Històric de sensors
def afegir_lectura(ruta, lectura):
    """Amplia l'històric d'un únic procés amb una lectura nova."""
    try:
        lectures = llegir_configuracio(ruta)
    except FileNotFoundError:
        lectures = []
    lectures.append(lectura)
    desar_configuracio(ruta, lectures)


def main():
    """Executa els exercicis amb exemples normals, buits i erronis."""
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "dades.json"
        configuracio = {
            "dispositiu": "Estació UAB", "actiu": True, "periode_s": 5,
        }
        desar_configuracio(ruta, configuracio)
        print(llegir_configuracio(ruta))
        desar_configuracio(ruta, {})
        print(llegir_configuracio(ruta))  # {}

        historic = [
            {"sensor": "T1", "valor": 20.0, "unitat": "°C"},
            {"sensor": "T1", "valor": 22.0, "unitat": "°C"},
        ]
        desar_configuracio(ruta, historic)
        print(mitjana_historic(ruta))  # 21.0
        desar_configuracio(ruta, [])
        print(mitjana_historic(ruta))  # None

        print(carregar_o_informar(Path(carpeta) / "absent.json"))
        with open(ruta, "w", encoding="utf-8") as fitxer:
            fitxer.write('{"actiu":')
        print(carregar_o_informar(ruta))  # JSON invàlid i None.
        desar_configuracio(ruta, {"actiu": True})
        print(carregar_o_informar(ruta))  # {'actiu': True}
        desar_configuracio(ruta, None)
        print(carregar_o_informar(ruta))  # None, sense avís.

        ruta_historic = Path(carpeta) / "historic.json"
        primera = {"sensor": "H1", "valor": 45.0, "unitat": "%"}
        segona = {"sensor": "H1", "valor": 46.0, "unitat": "%"}
        afegir_lectura(ruta_historic, primera)
        afegir_lectura(ruta_historic, segona)
        print(llegir_configuracio(ruta_historic))  # Dues lectures en ordre.
        afegir_lectura(ruta_historic, primera)
        print(len(llegir_configuracio(ruta_historic)))  # 3
        with open(ruta_historic, "w", encoding="utf-8") as fitxer:
            fitxer.write("[")
        try:
            afegir_lectura(ruta_historic, primera)
        except json.JSONDecodeError:
            print("S'ha propagat JSONDecodeError")


if __name__ == "__main__":
    main()
