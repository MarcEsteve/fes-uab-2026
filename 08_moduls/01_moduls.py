###
# 08 - Mòduls
# Un mòdul és un fitxer .py que agrupa codi reutilitzable.
###

# Objectius d'aprenentatge
# - Utilitzar import, from i as amb mòduls de la biblioteca estàndard.
# - Importar funcions de mòduls propis amb responsabilitats concretes.
# - Distingir la importació de l'execució directa amb __name__.
# Durada orientativa de teoria i demostracions: 60 minuts.

# 1. import carrega un mòdul. Accedim als seus noms amb un punt.
# math forma part de Python i ofereix funcions matemàtiques.
import math

print(math.sqrt(25))  # 5.0

# 2. from permet importar noms concrets. as dona un àlies local.
# statistics també pertany a la biblioteca estàndard.
from statistics import mean
import math as matematiques

print(mean([20.0, 22.0, 24.0]))  # 22.0
print(matematiques.pi)  # 3.141592653589793

# Evitem import * perquè dificulta saber d'on prové cada nom.
# Tampoc anomenem un fitxer math.py perquè ocultaria el mòdul estàndard.

# 3. Mòduls propis. conversions.py i sensors.py són a la mateixa carpeta.
# Python cerca primer a la carpeta del script quan l'executem directament.
# Executa des de l'arrel: python 08_moduls/01_moduls.py
import conversions as conv
from sensors import mitjana

print(conv.celsius_a_kelvin(25.0))  # 298.15
print(conv.milivolts_a_volts(3300))  # 3.3
print(mitjana([21.0, 22.0, 23.0]))  # 22.0
print(mitjana([]))  # None, absència de lectures

# 4. Projecte evolutiu. El programa coordina funcions dels dos mòduls.
# conversions transforma unitats i sensors resumeix lectures.
# Separar responsabilitats afavoreix la reutilització i el manteniment.
def mostrar_resum():
    """Mostra la temperatura mitjana simulada en Celsius i kelvins."""
    lectures = [20.0, 21.0, 22.0]
    temperatura_mitjana = mitjana(lectures)
    if temperatura_mitjana is None:
        print("Encara no hi ha lectures.")
    else:
        print(f"Mitjana: {temperatura_mitjana:.1f} °C")
        print(f"Mitjana: {conv.celsius_a_kelvin(temperatura_mitjana):.2f} K")


# __name__ val "__main__" quan executem aquest fitxer directament.
# En importar-lo, val el nom del mòdul i aquest bloc no s'executa.
# Les instruccions fora del bloc sí que s'executen en la primera importació.
# Observa conversions.py i sensors.py: només tenen demostracions protegides.
if __name__ == "__main__":
    mostrar_resum()

# Imprescindible: importacions explícites, mòduls propis i guarda __main__.
# Ampliació: paquets i instal·lació de biblioteques, fora d'aquesta sessió.
# Pràctica: 01_moduls_exercicis.py. Resol-la abans d'obrir les solucions.
