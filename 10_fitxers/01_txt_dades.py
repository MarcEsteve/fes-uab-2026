###
# EXEMPLE - Treballar amb fitxers TXT reals
# Executa aquest fitxer i obre la carpeta dades_txt per veure els resultats.
###

from pathlib import Path

# Rutes dels fitxers de dades
CARPETA_DADES = Path(__file__).resolve().parent / "dades_txt"
FITXER_TEMPERATURES = CARPETA_DADES / "temperatures.txt"
FITXER_FILTRE = CARPETA_DADES / "temperatures_altes.txt"

# Funcions per desar i llegir temperatures en fitxers de text
def desar_temperatures(ruta, temperatures):
    """Crea o substitueix un fitxer amb una temperatura per línia."""
    with open(ruta, "w", encoding="utf-8") as fitxer:
        for temperatura in temperatures:
            fitxer.write(f"{temperatura:.1f}\n")

# Funció per llegir temperatures des d'un fitxer existent
def llegir_temperatures(ruta):
    """Llegeix les temperatures d'un fitxer de text existent."""
    temperatures = []
    with open(ruta, "r", encoding="utf-8") as fitxer:
        for linia in fitxer:
            text = linia.strip()
            if text:
                temperatures.append(float(text))
    return temperatures


# Funció principal de l'exemple
def main():
    """Crea, llegeix i filtra dades persistents en fitxers visibles."""
    CARPETA_DADES.mkdir(exist_ok=True)

    # Això permet repetir l'exemple des de la mateixa situació inicial.
    # Els fitxers es creen de nou, però queden a la carpeta quan acaba.
    FITXER_TEMPERATURES.unlink(missing_ok=True)
    FITXER_FILTRE.unlink(missing_ok=True)

    print(f"Carpeta de l'exemple: {CARPETA_DADES}")
    print(f"Abans de crear-lo, {FITXER_TEMPERATURES.name} existeix: "
          f"{FITXER_TEMPERATURES.exists()}")

    # Temperatures fictícies registrades durant un dia d'estiu a Bellaterra.
    temperatures_dia = [
        18.5, 19.2, 20.1, 21.8, 23.4, 25.7,
        27.3, 28.1, 26.9, 24.6, 22.8, 20.5,
    ]
    desar_temperatures(FITXER_TEMPERATURES, temperatures_dia)
    print(f"Després de crear-lo, {FITXER_TEMPERATURES.name} existeix: "
          f"{FITXER_TEMPERATURES.exists()}")

    temperatures_llegides = llegir_temperatures(FITXER_TEMPERATURES)
    print(f"S'han llegit {len(temperatures_llegides)} temperatures.")

    llindar = 25.0
    temperatures_altes = [
        temperatura
        for temperatura in temperatures_llegides
        if temperatura >= llindar
    ]
    desar_temperatures(FITXER_FILTRE, temperatures_altes)

    print(f"Temperatures de {llindar:.1f} °C o superiors:")
    for temperatura in temperatures_altes:
        print(f"- {temperatura:.1f} °C")

    print("\nObre aquests dos fitxers des de l'explorador de VS Code:")
    print(f"- {FITXER_TEMPERATURES}")
    print(f"- {FITXER_FILTRE}")


# Fi del fitxer de l'exemple
if __name__ == "__main__":
    main()
