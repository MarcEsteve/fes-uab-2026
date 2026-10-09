###
# SOLUCIONS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
print("\nExercici 1:")
numero = 10
while numero >= 1:
  print(numero)
  numero -= 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
print("\nExercici 2:")
numero = 1
suma_parells = 0
while numero <= 20:
  if numero % 2 == 0:
    suma_parells += numero
  numero += 1

print(f"La suma dels números parells fins a 20 és: {suma_parells}")

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nExercici 3:")

numero = int(input("Introdueix un número enter positiu: "))
factorial = 1
comptador = 1

while comptador <= numero:
  factorial *= comptador
  comptador += 1

print(f"El factorial de {numero} és: {factorial}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
print("\nExercici 4:")

contrasenya = ""
while len(contrasenya) < 8:
  contrasenya = input("Introdueix una contrasenya (almenys 8 caràcters): ")
  if len(contrasenya) < 8:
    print("La contrasenya ha de tenir almenys 8 caràcters. Torna-ho a provar.")

print("Contrasenya vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
print("\nExercici 5:")

numero = int(input("Introdueix un número: "))
multiplicador = 1

while multiplicador <= 10:
  resultat = numero * multiplicador
  print(f"{numero} x {multiplicador} = {resultat}")
  multiplicador += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

print("\nExercici 6:")
n = int(input("Introdueix un número enter positiu N: "))

numero = 2
while numero <= n:
  es_primer = True  # Assumim que el número és primer fins que es demostri el contrari
  divisor = 2
  while divisor * divisor <= numero:  # Optimitzem: no cal provar divisors fins a numero
    if numero % divisor == 0:
      es_primer = False  # Si trobem un divisor, no és primer
      break  # Sortim del bucle interior
    divisor += 1
  if es_primer:
    print(numero)

  numero += 1
