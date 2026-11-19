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


# Exercici 5 - Intermedi - Filtrar temperatures
def filtrar_temperatures(ruta_origen, ruta_desti, llindar):
    """Desa les temperatures iguals o superiors al llindar."""
    temperatures = llegir_valides(ruta_origen)
    temperatures_filtrades = [
        temperatura
        for temperatura in temperatures
        if temperatura >= llindar
    ]
    with open(ruta_desti, "w", encoding="utf-8") as fitxer:
        for temperatura in temperatures_filtrades:
            fitxer.write(f"{temperatura:.1f}\n")
    return temperatures_filtrades


# Exercici 6 - Intermedi - Crear un resum d'un fitxer
def crear_resum(ruta_origen, ruta_resum):
    """Analitza un fitxer de temperatures i desa'n un resum."""
    temperatures = llegir_valides(ruta_origen)
    with open(ruta_resum, "w", encoding="utf-8") as fitxer:
        fitxer.write(f"Nombre de lectures: {len(temperatures)}\n")
        if not temperatures:
            fitxer.write("No hi ha dades per resumir.\n")
            return

        mitjana = sum(temperatures) / len(temperatures)
        fitxer.write(f"Mínima: {min(temperatures):.1f} °C\n")
        fitxer.write(f"Màxima: {max(temperatures):.1f} °C\n")
        fitxer.write(f"Mitjana: {mitjana:.1f} °C\n")


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

        temperatures = Path(carpeta) / "temperatures.txt"
        desar_missatge(temperatures, "18.5\n25.7\n27.3\n20.5\n")
        temperatures_altes = Path(carpeta) / "temperatures_altes.txt"
        print(filtrar_temperatures(
            temperatures, temperatures_altes, 25.0
        ))  # [25.7, 27.3]
        print(llegir_valides(temperatures_altes))  # [25.7, 27.3]

        resum = Path(carpeta) / "resum.txt"
        crear_resum(temperatures, resum)
        print(repr(llegir_missatge(resum)))
        # 'Nombre de lectures: 4\nMínima: 18.5 °C\n'
        # 'Màxima: 27.3 °C\nMitjana: 23.0 °C\n'

        desar_missatge(temperatures, "")
        filtrar_temperatures(temperatures, temperatures_altes, 25.0)
        print(llegir_missatge(temperatures_altes))  # ''
        crear_resum(temperatures, resum)
        print(repr(llegir_missatge(resum)))
        # 'Nombre de lectures: 0\nNo hi ha dades per resumir.\n'


if __name__ == "__main__":
    main()
