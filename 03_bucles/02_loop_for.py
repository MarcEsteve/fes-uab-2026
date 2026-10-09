###
# 02 - Bucles (for)
# Permeten executar un bloc de codi repetidament mentre ITERA un iterable o una llista
###

import os
os.system("cls")  # Neteja la pantalla del terminal

print("\nBucle for:")

# Iterar una llista
# fruites = ["poma", "pera", "mandarina"]
# for fruita in fruites:
#   print(fruita)

# Iterar sobre qualsevol cosa que sigui iterable
# cadena = "marc"
# for caracter in cadena:
#   print(caracter)

# enumerate()
# fruites = ["poma", "pera", "mandarina"]
# for idx, valor in enumerate(fruites):
#   print(f"L'índex és {idx} i la fruita és {valor}")

# bucles imbricats
# lletres = ["A", "B", "C"]
# numeros = [1, 2, 3]

# for lletra in lletres:
#   for numero in numeros:
#     print(f"{lletra}{numero}")

# Revisar Python Tutor: http://pythontutor.com/visualize.html#mode=edit


# break
# print("\nbreak:")
# animals = ["gos", "gat", "ratolí", "lloro", "peix", "canari"]
# for idx, animal in enumerate(animals):
#   print(animal)
#   if animal == "lloro":
#     print(f"El lloro està amagat a l'índex {idx}")
#     break

# continue
# print("\ncontinue:")
# animals = ["gos", "gat", "ratolí", "lloro", "peix", "canari"]
# for idx, animal in enumerate(animals):
#   if animal == "lloro": continue
#   print(animal)

# Comprensió de llistes (list comprehension)
# animals = ["gos", "gat", "ratolí", "lloro", "peix", "canari"]
# animals_majus = [animal.upper() for animal in animals]
# print(animals_majus)

# Mostra els números parells d'una llista
# parells = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
# print(parells)

###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
# print("\nExercici 1:")

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
# numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
# print("\nExercici 2:")

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
# numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
# print("\nExercici 3:")

# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
# print("\nExercici 4:")

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
# print("\nExercici 5:")
