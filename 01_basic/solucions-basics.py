###
# soluciones.py
# Solucions als exercicis del fitxer exercicis-basics.py
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

# Solució:
nom = "Pere"  # Substitueix-lo pel teu nom
ciutat = "Barcelona"  # Substitueix-la per la teva ciutat

print(nom)
print(ciutat)

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Fes servir la funció 'type()' per determinar el tipus de dada de cada variable.")

# Variables de l'enunciat
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

# Solució:
print("Tipus de a:", type(a))
print("Tipus de b:", type(b))
print("Tipus de c:", type(c))
print("Tipus de d:", type(d))
print("Tipus de e:", type(e))

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena '12345' a un enter i després a un nombre decimal.")
print("Converteix el nombre decimal 3.99 a un enter. Què passa?")

# Solució:
cadena = "12345"
nombre_enter = int(cadena)  # Converteix la cadena a enter
nombre_decimal = float(nombre_enter)  # Converteix l'enter a nombre decimal

print("Nombre enter:", nombre_enter)
print("Nombre decimal:", nombre_decimal)

decimal_original = 3.99
enter_convertit = int(decimal_original)  # Se n'elimina la part decimal

print("Nombre decimal original:", decimal_original)
print("Nombre decimal convertit a enter (se n'elimina la part decimal):", enter_convertit)

print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Fes servir f-strings per mostrar una presentació.")

# Solució:
nom = "Marc"
edad = 18
alcada = 1.90

# Mostra la presentació amb una f-string
print(f"Hola! Em dic {nom}, tinc {edad} anys i faig {alcada} metres")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Utilitza el valor aproximat de PI (3.1416) sense desar-lo en una variable")
print("2. Arrodoneix el nombre amb round()")
print("3. Divideix entre 2 el nombre obtingut")
print("4. El resultat hauria de ser 1")

# Solució:
# Arrodonim directament el valor de pi sense desar-lo en una variable
resultat = int(round(3.1416) / 2)
print("Valor aproximat de PI:", 3.1416)
print("PI arrodonit:", round(3.1416))
print("Divisió de PI arrodonit entre 2:", resultat)

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix-la a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra tots dos valors amb un missatge clar.")

# Solució:
celsius = float(input("Introdueix la temperatura en °C: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")

print("--------------")

print("\nExercici 7: Calculadora de propines")
print("Demana l'import total d'un compte i el percentatge de propina.")
print("Calcula l'import de la propina i el total que cal pagar.")
print("Mostra els resultats amb 2 decimals.")

# Solució:
total_compte = float(input("Introdueix l'import total del compte: "))
percentatge_propina = float(input("Introdueix el percentatge de propina: "))

propina = total_compte * (percentatge_propina / 100)
total_final = total_compte + propina

print(f"Propina: {propina:.2f} €")
print(f"Total a pagar: {total_final:.2f} €")

print("--------------")

print("\nExercici 8: Comprovador senzill de contrasenya")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

# Solució:
contrasenya = input("Introdueix una contrasenya: ")

if len(contrasenya) >= 8:
	print("Contrasenya vàlida")
else:
	print("Contrasenya no vàlida")