###
# SOLUCIONS - CSV
###

import csv
from pathlib import Path
from tempfile import TemporaryDirectory

CAMPS = ["sensor", "valor", "unitat"]


# Exercici 1 - Bàsic - Taula de tensions
def desar_tensions(ruta, tensions):
    """Desa parelles de sensor i tensió amb capçalera."""
    with open(ruta, "w", encoding="utf-8", newline="") as fitxer:
        escriptor = csv.writer(fitxer)
        escriptor.writerow(["sensor", "volts"])
        escriptor.writerows(tensions)


# Exercici 2 - Bàsic - Selecció per llindar
def sensors_en_alerta(ruta, llindar):
    """Retorna els noms amb una mesura igual o superior al llindar."""
    noms = []
    with open(ruta, "r", encoding="utf-8", newline="") as fitxer:
        for fila in csv.DictReader(fitxer):
            if float(fila["valor"]) >= llindar:
                noms.append(fila["sensor"])
    return noms


# Exercici 3 - Intermedi - Anada i tornada
def desar_lectures(ruta, lectures):
    """Escriu registres vàlids i conserva els noms amb comes."""
    with open(ruta, "w", encoding="utf-8", newline="") as fitxer:
        escriptor = csv.DictWriter(fitxer, fieldnames=CAMPS)
        escriptor.writeheader()
        escriptor.writerows(lectures)


def recuperar_lectures(ruta):
    """Recupera les files d'un CSV vàlid convertint valor a float."""
    with open(ruta, "r", encoding="utf-8", newline="") as fitxer:
        lectures = list(csv.DictReader(fitxer))
    for lectura in lectures:
        lectura["valor"] = float(lectura["valor"])
    return lectures


# Exercici 4 - Repte opcional - Capçalera incorrecta
def llegir_amb_capcalera_validada(ruta):
    """Valida la capçalera abans de recuperar files completes."""
    with open(ruta, "r", encoding="utf-8", newline="") as fitxer:
        lector = csv.DictReader(fitxer)
        if lector.fieldnames != CAMPS:
            raise ValueError("Capçalera incorrecta")
        lectures = list(lector)
    for lectura in lectures:
        lectura["valor"] = float(lectura["valor"])
    return lectures


def main():
    """Executa els quatre exercicis i els casos buits."""
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "lectures.csv"
        desar_tensions(ruta, [("V1", 3.3), ("V2", 5.0)])
        with open(ruta, encoding="utf-8", newline="") as fitxer:
            print(list(csv.reader(fitxer)))
        desar_tensions(ruta, [])
        with open(ruta, encoding="utf-8", newline="") as fitxer:
            print(list(csv.reader(fitxer)))  # [['sensor', 'volts']]

        lectures = [
            {"sensor": "T1", "valor": 20.0, "unitat": "°C"},
            {"sensor": "T2", "valor": 25.0, "unitat": "°C"},
            {"sensor": "T3", "valor": 26.0, "unitat": "°C"},
        ]
        desar_lectures(ruta, lectures)
        print(sensors_en_alerta(ruta, 25.0))  # ['T2', 'T3']
        desar_lectures(ruta, [])
        print(sensors_en_alerta(ruta, 25.0))  # []
        print(recuperar_lectures(ruta))  # []

        amb_coma = [{"sensor": "Sala, nord", "valor": 19.5, "unitat": "°C"}]
        desar_lectures(ruta, amb_coma)
        print(recuperar_lectures(ruta))  # Mateixa llista.
        print(llegir_amb_capcalera_validada(ruta))
        desar_lectures(ruta, [])
        print(llegir_amb_capcalera_validada(ruta))  # []
        for contingut in ["nom,valor\nT1,20\n", ""]:
            with open(ruta, "w", encoding="utf-8") as fitxer:
                fitxer.write(contingut)
            try:
                llegir_amb_capcalera_validada(ruta)
            except ValueError as error:
                print(error)


if __name__ == "__main__":
    main()
