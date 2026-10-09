###
# SOLUCIONS (funcions)
###

# Exercici 1: Funció de salutació
print("\nExercici 1:")
def saludar_a(nom, salutacio="Hola"):
  print(f"{salutacio} {nom}!")

saludar_a("Marc")
saludar_a("Cristina", "Bon dia")

# Exercici 2: Parell o senar
print("\nExercici 2:")
def es_parell(numero):
  return numero % 2 == 0

print(es_parell(4))  # True
print(es_parell(7))  # False

# Exercici 3: Mitjana d'una llista
print("\nExercici 3:")
def mitjana(numeros):
  suma = 0
  for numero in numeros:
    suma += numero
  return suma / len(numeros)

print(mitjana([10, 20, 30, 40, 50]))  # 30.0

# Exercici 4: Suma amb *args
print("\nExercici 4:")
def sumar_tot(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print(sumar_tot(1, 2))
print(sumar_tot(1, 2, 3, 4, 5))
print(sumar_tot(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Exercici 5: Taula de multiplicar
print("\nExercici 5:")
def taula_multiplicar(numero, limit=10):
  for i in range(1, limit + 1):
    print(f"{numero} x {i} = {numero * i}")

taula_multiplicar(3)
taula_multiplicar(5, 3)

# Exercici 6: Informació amb **kwargs
print("\nExercici 6:")
def mostrar_perfil(**kwargs):
  for clau, valor in kwargs.items():
    print(f"{clau}: {valor}")

mostrar_perfil(nom="Anna", edat=19, grau="Enginyeria de Sistemes de Telecomunicació")

# Exercici 7: Reconvertir exercicis anteriors
print("\nExercici 7:")
def factorial(n):
  resultat = 1
  comptador = 1
  while comptador <= n:
    resultat *= comptador
    comptador += 1
  return resultat

def maxim(numeros):
  valor_maxim = numeros[0]
  for numero in numeros:
    if numero > valor_maxim:
      valor_maxim = numero
  return valor_maxim

print(f"El factorial de 5 és {factorial(5)}")  # 120
print(f"El màxim és {maxim([15, 5, 25, 10, 20])}")  # 25
