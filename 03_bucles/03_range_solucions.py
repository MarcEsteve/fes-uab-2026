###
# SOLUCIONS (range)
###

# Exercici 1: Imprimir números de l'1 al 10
# Imprimeix els números de l'1 al 10 (inclosos) fent servir un bucle for i range().
print("\nExercici 1:")
for i in range(1, 11):  # Recorda que range no inclou el límit superior
  print(i)

# Exercici 2: Imprimir números senars de l'1 al 20
# Imprimeix tots els números senars entre 1 i 20 (inclosos) fent servir un bucle for i range().
print("\nExercici 2:")
for i in range(1, 21, 2):  # El pas 2 assegura que només es generin senars
  print(i)

# Exercici 3: Imprimir múltiples de 5
# Imprimeix els múltiples de 5 des del 5 fins al 50 (inclosos) fent servir un bucle for i range().
print("\nExercici 3:")
for i in range(5, 51, 5):  # El pas 5 genera els múltiples de 5
  print(i)

# Exercici 4: Imprimir números en ordre invers
# Imprimeix els números del 10 a l'1 (inclosos) en ordre invers fent servir un bucle for i range().
print("\nExercici 4:")
for i in range(10, 0, -1):  # Pas negatiu per a l'ordre invers
  print(i)

# Exercici 5: Suma de números en un rang
# Calcula la suma dels números de l'1 al 100 (inclosos) fent servir un bucle for i range().
print("\nExercici 5:")
suma = 0
for i in range(1, 101):
  suma += i
print(f"La suma dels números de l'1 al 100 és: {suma}")

# Exercici 6: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle for i range().
print("\nExercici 6:")
numero = int(input("Introdueix un número per a la taula de multiplicar: "))
for i in range(1, 11):
  print(f"{numero} x {i} = {numero * i}")
