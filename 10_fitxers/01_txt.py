###
# 10 - Fitxers TXT
# Objectius d'aprenentatge
# - Construir rutes portables amb pathlib.Path.
# - Obrir, llegir i escriure text UTF-8 amb with i open.
# - Distingir els modes r, w i a i recuperar mesures d'un fitxer.
###

from pathlib import Path
from tempfile import TemporaryDirectory

# 1. Una ruta representa una ubicació. Crear un Path no crea el fitxer.
# L'operador / uneix carpetes i noms amb el separador de cada sistema.
# Les rutes relatives parteixen del directori de treball del programa.
# exists() permet consultar si una ruta existeix.


def desar_temperatures(ruta, temperatures):
    """Desa una temperatura per línia en un fitxer de text."""
    # w crea el fitxer o en substitueix TOT el contingut anterior.
    # with tanca el recurs també si es produeix una excepció.
    with open(ruta, "w", encoding="utf-8") as fitxer:
        for temperatura in temperatures:
            fitxer.write(f"{temperatura}\n")


def llegir_temperatures(ruta):
    """Recupera temperatures numèriques i ignora les línies buides."""
    temperatures = []
    # r llegeix un fitxer existent. Si falta, genera FileNotFoundError.
    with open(ruta, "r", encoding="utf-8") as fitxer:
        for linia in fitxer:
            text = linia.strip()  # Elimina espais i el salt de línia final.
            if text:
                temperatures.append(float(text))
    # Un text no numèric genera ValueError. El bloc 09 explica com capturar-lo.
    return temperatures


def main():
    """Executa exemples en una carpeta temporal que es neteja en acabar."""
    # TemporaryDirectory només prepara l'espai de la demostració.
    # En un projecte real la ruta seria un paràmetre de configuració.
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "lectures.txt"
        print(ruta.name, ruta.exists())  # lectures.txt False
        desar_temperatures(ruta, [20.0, 21.5])
        print(ruta.exists())  # True

        # 2. read() retorna tot el text. Iterar és útil per processar línies.
        with open(ruta, "r", encoding="utf-8") as fitxer:
            print(fitxer.read(), end="")  # Dues línies, 20.0 i 21.5.

        # 3. a afegeix text al final i conserva el contingut anterior.
        with open(ruta, "a", encoding="utf-8") as fitxer:
            fitxer.write("22.0\n")
        print(llegir_temperatures(ruta))  # [20.0, 21.5, 22.0]

        # 4. L'absència de dades és diferent de l'absència del fitxer.
        desar_temperatures(ruta, [])
        print(llegir_temperatures(ruta))  # []


# Enginyeria del programari. Separar lectura, càlcul i presentació facilita
# reutilitzar funcions i provar-les amb fitxers petits i controlats.
# Essencial en 60 min. Rutes, modes, with, codificació i lectura per línies.
# Pràctica a 01_txt_exercicis.py. El repte és opcional.
if __name__ == "__main__":
    main()
