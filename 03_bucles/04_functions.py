###
# 04 - Funcions
# Blocs de codi reutilitzables i parametritzables per fer tasques específiques
###

import os
os.system("cls")

""" Definició d'una funció

def nom_de_la_funcio(parametre1, parametre2, ...):
  # docstring
  # cos de la funció
  return valor_de_retorn # opcional

"""

# # Exemple d'una funció per imprimir alguna cosa a la consola
# def saludar():
#   print("Hola!")

# saludar() # crida a la funció

# # Exemple d'una funció amb paràmetre
# def saludar_a(nom):
#   print(f"Hola {nom}!")

# saludar_a("marc") # argument = "marc"
# saludar_a("cristina")
# saludar_a("fernando")

# El paràmetre és el que accepta la funció
# L'argument és el valor que se li passa a la funció

# # Funcions amb més paràmetres
# def sumar(a, b):
#   suma = a + b
#   return suma

# resultat = sumar(2, 3)
# print(resultat)

# # Documentar les funcions amb docstring
# def restar(a, b):
#   """Resta dos números i retorna el resultat"""
#   return a - b
# En Python pots accedir al docstring d'una funció amb l'atribut __doc__
# print(restar.__doc__)
# Fins i tot help(restar) et mostrarà el docstring de la funció
# help(restar)

# paràmetres per defecte
# def multiplicar(a, b = 5):
#   return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))

# Arguments per posició
# def descriure_persona(nom: str, edat: int, sexe: str):
#   print(f"Sóc {nom}, tinc {edat} anys i m'identifico com a {sexe}")

# els paràmetres són posicionals
# descriure_persona(1, 25, "gat")
# descriure_persona("marc", 25, "gat")
# descriure_persona("home", "marc", 39)

# Arguments per clau
# paràmetres anomenats
# descriure_persona(sexe="gat", nom="marc", edat=25)
# descriure_persona(sexe="home", nom="pere", edat=21)

# Arguments de longitud variable (*args):
# def sumar_numeros(*args):
#   suma = 0
#   for numero in args:
#     suma += numero
#   return suma

# print(sumar_numeros(1, 2, 3, 4, 5))
# print(sumar_numeros(1, 2))
# print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Arguments de clau-valor variable (**kwargs):
# def mostrar_informacio_de(**kwargs):
#   for clau, valor in kwargs.items():
#     print(f"{clau}: {valor}")

# mostrar_informacio_de(nom="marc", edat=25, sexe="gat")
# print("\n")
# mostrar_informacio_de(nom="pere", edat=21, pais="Madagascar")
# print("\n")
# mostrar_informacio_de(nick="charly", es_sub=True, es_ric=True)
# print("\n")
# mostrar_informacio_de(super_nom="joan", es_mode=True, gats=40)

# Exercicis
# Tornar als exercicis anteriors
# i convertir-los en funcions
# i intentar utilitzar tots els casos i conceptes
# que hem vist fins ara
# rangs, llistes, bucles, etc.
