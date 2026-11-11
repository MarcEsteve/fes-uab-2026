###
# 10 - Fitxers JSON
# Objectius d'aprenentatge
# - Representar registres i configuracions amb JSON.
# - Desar amb json.dump i recuperar amb json.load.
# - Distingir sintaxi correcta i estructura adequada a l'aplicació.
###

import json
import math
from pathlib import Path
from tempfile import TemporaryDirectory

# JSON representa diccionaris amb claus textuals, llistes, nombres, text,
# booleans i null. Python converteix null a None i true/false a True/False.
# Una tupla s'escriu com un array i es recupera com una llista.
# Les classes pròpies necessiten una conversió explícita a dades natives.


def desar_json(ruta, lectures):
    """Desa una llista de lectures preparada pel sistema de monitoratge."""
    # Precondició del productor. Diccionaris sensor/valor/unitat vàlids.
    # dump escriu al fitxer. dumps retornaria una cadena.
    # allow_nan=False exigeix nombres finits, segons el JSON estàndard.
    # Preparem el text abans d'obrir el destí per detectar errors de conversió.
    text = json.dumps(lectures, ensure_ascii=False, indent=2, allow_nan=False)
    with open(ruta, "w", encoding="utf-8") as fitxer:
        fitxer.write(text)


def llegir_json(ruta):
    """Recupera una llista de lectures amb camps i valors vàlids."""
    with open(ruta, "r", encoding="utf-8") as fitxer:
        lectures = json.load(fitxer)
    # Un JSON pot ser sintàcticament correcte i tenir un format inadequat.
    if not isinstance(lectures, list):
        raise ValueError("Cal una llista de lectures")
    for lectura in lectures:
        if not isinstance(lectura, dict):
            raise ValueError("Cada lectura ha de ser un diccionari")
        if len(lectura) != 3:
            raise ValueError("Cada lectura ha de tenir sensor, valor i unitat")
        for camp in ("sensor", "valor", "unitat"):
            if camp not in lectura:
                raise ValueError("Falta un camp de la lectura")
        if not isinstance(lectura["sensor"], str):
            raise ValueError("El nom del sensor ha de ser text")
        if not isinstance(lectura["unitat"], str):
            raise ValueError("La unitat ha de ser text")
        valor = lectura["valor"]
        # bool és un subtipus d'int en Python. Aquí True no és una mesura.
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("La mesura ha de ser numèrica")
        try:
            valor = float(valor)
        except OverflowError:
            raise ValueError("La mesura supera el rang numèric admès")
        if not math.isfinite(valor):
            raise ValueError("La mesura ha de ser finita")
        lectura["valor"] = valor
    return lectures


def main():
    """Desa un registre, el recupera i mostra un error de sintaxi JSON."""
    lectures = [{"sensor": "T1", "valor": 21.5, "unitat": "°C"}]
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "lectures.json"
        desar_json(ruta, lectures)
        print(llegir_json(ruta))  # Mateixa llista de registres.
        desar_json(ruta, [])
        print(llegir_json(ruta))  # []

        # Un exemple directe de dump per a una configuració petita.
        configuracio = Path(carpeta) / "configuracio.json"
        with open(configuracio, "w", encoding="utf-8") as fitxer:
            json.dump({"actiu": True, "llindar": 25.0}, fitxer, indent=2)
        with open(configuracio, encoding="utf-8") as fitxer:
            print(json.load(fitxer))  # {'actiu': True, 'llindar': 25.0}

        with open(ruta, "w", encoding="utf-8") as fitxer:
            fitxer.write('{"sensor":')
        try:
            llegir_json(ruta)
        except json.JSONDecodeError:
            print("El fitxer conté JSON incomplet")


# Enginyeria del programari. Validar dades recuperades defineix el límit
# entre persistència i lògica del sistema. CSV i JSON comparteixen contracte.
# Essencial en 30 min. dump/load, tipus compatibles i errors de sintaxi.
# Ampliació. Validació detallada de l'esquema que aplica llegir_json.
if __name__ == "__main__":
    main()
