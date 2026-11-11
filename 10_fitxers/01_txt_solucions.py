###
# SOLUCIONS - Fitxers TXT
###

from pathlib import Path
from tempfile import TemporaryDirectory


# Exercici 1 - Bàsic - Desar un missatge
def desar_missatge(ruta, missatge):
    """Substitueix el contingut pel missatge rebut."""
    with open(ruta, "w", encoding="utf-8") as fitxer:
        fitxer.write(missatge)


def llegir_missatge(ruta):
    """Retorna tot el text, incloent-hi els salts de línia."""
    with open(ruta, "r", encoding="utf-8") as fitxer:
        return fitxer.read()


# Exercici 2 - Bàsic - Comptar lectures
def comptar_lectures(ruta):
    """Compta les línies amb contingut."""
    comptador = 0
    with open(ruta, "r", encoding="utf-8") as fitxer:
        for linia in fitxer:
            if linia.strip():
                comptador += 1
    return comptador


# Exercici 3 - Intermedi - Recuperar valors vàlids
def llegir_valides(ruta):
    """Recupera decimals i descarta les línies no convertibles."""
    lectures = []
    with open(ruta, "r", encoding="utf-8") as fitxer:
        for linia in fitxer:
            text = linia.strip()
            if text:
                try:
                    lectures.append(float(text))
                except ValueError:
                    continue
    return lectures


# Exercici 4 - Repte opcional - Registre acumulatiu
def afegir_esdeveniment(ruta, missatge):
    """Afegeix un missatge sense salts interns i un salt final."""
    with open(ruta, "a", encoding="utf-8") as fitxer:
        fitxer.write(missatge + "\n")


def main():
    """Mostra les quatre solucions amb dades temporals."""
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "prova.txt"
        desar_missatge(ruta, "Sensor de tensió actiu\n")
        print(repr(llegir_missatge(ruta)))
        desar_missatge(ruta, "")
        print(repr(llegir_missatge(ruta)))  # ''

        desar_missatge(ruta, "20.0\n\n21.5\n   \n")
        print(comptar_lectures(ruta))  # 2
        desar_missatge(ruta, "")
        print(comptar_lectures(ruta))  # 0
        try:
            comptar_lectures(Path(carpeta) / "absent.txt")
        except FileNotFoundError:
            print("S'ha propagat FileNotFoundError")

        desar_missatge(ruta, "20.0\nerror\n\n22.0\n")
        print(llegir_valides(ruta))  # [20.0, 22.0]
        desar_missatge(ruta, "error\n\n")
        print(llegir_valides(ruta))  # []

        registre = Path(carpeta) / "esdeveniments.txt"
        afegir_esdeveniment(registre, "Inici")
        afegir_esdeveniment(registre, "Aturada")
        print(repr(llegir_missatge(registre)))  # 'Inici\nAturada\n'
        afegir_esdeveniment(registre, "Inici")
        print(repr(llegir_missatge(registre)))


if __name__ == "__main__":
    main()
