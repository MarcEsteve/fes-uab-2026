###
# 10 - Fitxers CSV
# Objectius d'aprenentatge
# - Representar una taula de lectures amb capçalera.
# - Escriure amb DictWriter i llegir amb DictReader.
# - Convertir text a float i validar l'estructura recuperada.
###

import csv
import math
from pathlib import Path
from tempfile import TemporaryDirectory

# CSV és text tabular. Cada fila conté camps i la primera pot posar-los nom.
# csv gestiona separadors, cometes i salts de línia dins dels camps.
# Evitem split(","), perquè un nom com "Laboratori, nord" conté una coma.
# El nostre format estable és sensor,valor,unitat, amb coma com a separador.
CAMPS = ["sensor", "valor", "unitat"]


def desar_csv(ruta, lectures):
    """Desa diccionaris amb les claus sensor, valor i unitat."""
    # Precondició del productor. Valors numèrics finits i camps textuals.
    # newline="" deixa que csv gestioni els salts de línia a cada plataforma.
    with open(ruta, "w", encoding="utf-8", newline="") as fitxer:
        escriptor = csv.DictWriter(fitxer, fieldnames=CAMPS)
        escriptor.writeheader()
        escriptor.writerows(lectures)


def llegir_csv(ruta):
    """Recupera lectures i rebutja capçaleres o mesures invàlides."""
    lectures = []
    with open(ruta, "r", encoding="utf-8", newline="") as fitxer:
        lector = csv.DictReader(fitxer)
        if lector.fieldnames != CAMPS:
            raise ValueError("La capçalera ha de ser sensor,valor,unitat")
        for fila in lector:
            # DictReader retorna text. Una fila incompleta pot contenir None.
            if None in fila:
                raise ValueError("La fila ha de tenir tres camps")
            for camp in CAMPS:
                if fila[camp] is None:
                    raise ValueError("La fila ha de tenir tres camps")
            valor = float(fila["valor"])
            # isfinite exclou nan i inf, que float accepta com a nombres.
            if not math.isfinite(valor):
                raise ValueError("La mesura ha de ser finita")
            lectures.append({
                "sensor": fila["sensor"],
                "valor": valor,
                "unitat": fila["unitat"],
            })
    return lectures


def main():
    """Desa i recupera una taula petita de monitoratge."""
    lectures = [
        {"sensor": "T1", "valor": 21.5, "unitat": "°C"},
        {"sensor": "Laboratori, nord", "valor": 48.0, "unitat": "%"},
    ]
    with TemporaryDirectory() as carpeta:
        # Primer, files com a llistes. writer/reader treballen per posició.
        # writerow escriu una fila i reader recupera llistes de cadenes.
        ruta_tensions = Path(carpeta) / "tensions.csv"
        with open(
            ruta_tensions, "w", encoding="utf-8", newline=""
        ) as fitxer:
            escriptor = csv.writer(fitxer)
            escriptor.writerow(["sensor", "volts"])
            escriptor.writerow(["V1", 3.3])
        with open(ruta_tensions, encoding="utf-8", newline="") as fitxer:
            print(list(csv.reader(fitxer)))
            # [['sensor', 'volts'], ['V1', '3.3']]

        # Després, DictWriter/DictReader treballen per nom de camp.
        ruta = Path(carpeta) / "lectures.csv"
        desar_csv(ruta, lectures)
        recuperades = llegir_csv(ruta)
        print(recuperades)  # Mateixos sensors, valors i unitats.
        print(type(recuperades[0]["valor"]).__name__)  # float
        desar_csv(ruta, [])
        print(llegir_csv(ruta))  # [] amb capçalera present.


# Enginyeria del programari. Acordar noms i unitats és un contracte de dades.
# El lector valida les dades externes abans que el programa les utilitzi.
# Essencial en 30 min. Capçalera, newline, DictWriter/DictReader i conversions.
# Ampliació. Diagnòstic de files malformades i altres delimitadors.
if __name__ == "__main__":
    main()
