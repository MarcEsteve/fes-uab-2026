###
# 01 - Bucles (while)
# Permeten executar un bloc de codi repetidament mentre es compleixi una condició
###

import os
os.system("cls") # neteja la pantalla

# print("\n Bucle while:")

# Bucle amb una condició simple
# comptador = 0

# {claus} [claudàtors] (parèntesis)
# indentació "tabulació o sagnat"

# while comptador <= 5:
#     print(comptador)
#     comptador += 1 # és molt important per evitar un bucle infinit

# utilitzant la paraula break, per trencar el bucle
# print("\n Bucle while amb break:")
# comptador = 0

# while True:
#   print(comptador)
#   comptador += 1
#   if comptador == 5:
#     break # surt del bucle

# continue, el que fa és saltar aquesta iteració en concret
# i continuar amb el bucle
# print("\n Bucle amb continue")
# comptador = 0
# while comptador < 10:
#   comptador += 1

#   if comptador % 2 == 0:
#     continue

#   print(comptador)

# else, quan s'executa aquesta condició?
# print("\n Bucle while amb else:")
# comptador = 0
# while comptador < 5:
#   print(comptador)
#   comptador += 1

# else:
#   print("El bucle ha acabat, i ha recorregut tots els números")

# else, quan s'executa aquesta condició?
# print("\n Bucle while amb else:")
# comptador = 0
# while comptador < 5:
#   print(comptador)
#   comptador += 1
# else:
#   print("El bucle ha acabat")

# comptador = 0
# while comptador < 5:
#     print(f"El comptador és {comptador}")
#     comptador += 1
# else:
#     print("El bucle while ha acabat de forma natural.")
#     print(f"El valor final del comptador és {comptador}.")

# numero = 0
# while numero < 10:
#     print(f"El número és {numero}")
#     if numero == 3:
#         print("Hem arribat al 3! Trencant el bucle.")
#         break  # Interromp el bucle
#     numero += 1
# else:
#     print("Aquest missatge no s'imprimirà perquè el bucle ha estat interromput per 'break'.")

# print("El programa ha continuat després del bucle.")

# Sortida esperada:
# El número és 0
# El número és 1
# El número és 2
# El número és 3
# Hem arribat al 3! Trencant el bucle.
# El programa ha continuat després del bucle.

# Sortida esperada:
# El comptador és 0
# El comptador és 1
# El comptador és 2
# El comptador és 3
# El comptador és 4
# El bucle while ha acabat de forma natural.
# El valor final del comptador és 5.

# demanar a l'usuari un número que ha
# de ser positiu, si no, no el deixem en pau
# numero = -1
# while numero < 0:
#   numero = int(input("Escriu un número positiu: "))
#   if numero < 0:
#     print("El número ha de ser positiu. Torna-ho a provar.")

# print(f"El número que has introduït és {numero}")

# numero = -1
# while numero < 0:
#   try:
#     numero = int(input("Escriu un número positiu: "))
#     if numero < 0:
#       print("El número ha de ser positiu. Torna-ho a provar.")
#   except:
#     print("El que introdueixes ha de ser un número, que si no peta!")

# print(f"El número que has introduït és {numero}")

###
# EXERCICIS (while)
###

# # Exercici 1: Compte enrere
# # Imprimeix els números del 10 a l'1 fent servir un bucle while.
# print("\nExercici 1:")

# # Exercici 2: Suma de números parells (while)
# # Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
# print("\nExercici 2:")

# # Exercici 3: Factorial d'un número
# # Demana a l'usuari que introdueixi un número enter positiu.
# # Calcula el seu factorial fent servir un bucle while.
# # El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# # 5! = 5 x 4 x 3 x 2 x 1 = 120.
# print("\nExercici 3:")

# # Exercici 4: Validació de contrasenya
# # Demana a l'usuari que introdueixi una contrasenya.
# # La contrasenya ha de tenir almenys 8 caràcters.
# # Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# # Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
# print("\nExercici 4:")

# # Exercici 5: Taula de multiplicar
# # Demana a l'usuari que introdueixi un número.
# # Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
# print("\nExercici 5:")

# # Exercici 6: Números primers fins a N
# # Demana a l'usuari que introdueixi un número enter positiu N.
# # Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# print("\nExercici 6:")
