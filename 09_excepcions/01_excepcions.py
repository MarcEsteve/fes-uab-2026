###
# 09 - Excepcions i validació
###

# Objectius d'aprenentatge
# - Identificar ValueError i FileNotFoundError.
# - Utilitzar try, except, else i finally segons la seva responsabilitat.
# - Validar lectures i comunicar errors amb raise.
# Durada orientativa de teoria i demostracions: 60 minuts.

import math
from pathlib import Path
from tempfile import TemporaryDirectory


# 1. Una excepció interromp el flux normal quan una operació falla.
# float("error") provocaria ValueError. Capturar-la permet donar resposta.
# Limitem el try a l'operació que esperem que pugui fallar.
text = "error"
try:
    temperatura = float(text)
except ValueError:
    print("La temperatura ha de ser numèrica.")
else:
    # else s'executa quan el try acaba sense excepció.
    print(f"Temperatura convertida: {temperatura}")
finally:
    # finally s'executa tant en el camí correcte com en el camí d'error.
    # No equival a confirmar que l'operació ha anat bé.
    print("Intent de conversió acabat.")


# 2. Converteix primer i valida després. raise crea una excepció explícita.
# El rang -40..85 °C és una especificació del sensor SIMULAT del curs.
# math.isfinite rebutja inf, -inf i nan, que float sí que pot convertir.
def validar_temperatura(text):
    """Converteix text a una temperatura finita entre -40 i 85 °C."""
    valor = float(text)
    if not math.isfinite(valor):
        raise ValueError("La temperatura ha de ser finita.")
    if valor < -40 or valor > 85:
        raise ValueError("Temperatura fora del rang simulat [-40, 85].")
    return valor


for entrada in ["21.5", "-40", "85", "90", "nan", "avaria"]:
    try:
        lectura = validar_temperatura(entrada)
    except ValueError as error:
        print(f"Lectura {entrada!r} rebutjada: {error}")
    else:
        print(f"Lectura acceptada: {lectura} °C")


# 3. Una funció valida i qui la crida decideix com gestionar l'error.
# La humitat relativa del model admet els extrems 0 i 100 %.
def validar_humitat(text):
    """Converteix text a una humitat finita entre 0 i 100 %."""
    humitat = float(text)
    if not math.isfinite(humitat):
        raise ValueError("La humitat ha de ser finita.")
    if humitat < 0 or humitat > 100:
        raise ValueError("La humitat ha d'estar entre 0 i 100.")
    return humitat


try:
    print(validar_humitat("101"))
except ValueError as error:
    print(error)


# 4. FileNotFoundError indica que no s'ha trobat el fitxer demanat.
# Path construeix una ruta i TemporaryDirectory crea una carpeta temporal.
# with en gestiona la neteja. Al bloc 10 treballarem amb aquestes eines.
# Aquí no creem el fitxer: així l'error és determinista i no toca dades reals.
with TemporaryDirectory() as carpeta:
    ruta = Path(carpeta) / "lectures_absents.txt"
    try:
        with open(ruta, encoding="utf-8") as fitxer:
            contingut = fitxer.read()
    except FileNotFoundError:
        print("Encara no hi ha cap fitxer de lectures.")
    else:
        print(contingut)

# Imprescindible: excepcions concretes, validació i missatges comprensibles.
# Rebutgem una lectura errònia abans d'incorporar-la a l'estat del sistema.
# Ampliació: excepcions pròpies, fora de la sessió.
# Pràctica: 01_excepcions_exercicis.py.
