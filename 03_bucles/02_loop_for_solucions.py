###
# SOLUCIONS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
print("\nExercici 1:")
for numero in range(2, 21, 2):  # range(inici, final, pas)
  print(numero)

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
# numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
print("\nExercici 2:")
numeros = [10, 20, 30, 40, 50]
suma = 0
for numero in numeros:
  suma += numero
mitjana = suma / len(numeros)
print(f"La mitjana és: {mitjana}")

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
# numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
print("\nExercici 3:")
numeros = [15, 5, 25, 10, 20]
maxim = numeros[0]  # Inicialitzem amb el primer element
for numero in numeros:
  if numero > maxim:
    maxim = numero
print(f"El número màxim és: {maxim}")

# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
print("\nExercici 4:")
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
paraules_llargues = [paraula for paraula in paraules if len(paraula) > 5]
print(paraules_llargues)

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
print("\nExercici 5:")
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
lletra = input("Introdueix una lletra: ").lower()  # Convertim la lletra a minúscula
comptador = 0
for paraula in paraules:
  if paraula.lower().startswith(lletra):  # Comparem en minúscules
    comptador += 1
print(f"Hi ha {comptador} paraules que comencen per la lletra {lletra}")
