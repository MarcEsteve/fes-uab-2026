###
# 05 - Diccionaris
# Els diccionaris són col·leccions de parelles clau-valor.
# Serveixen per emmagatzemar dades relacionades.
###

import os
os.system("cls")

# exemple típic de diccionari
persona = {
  "nom": "marc",
  "edat": 25,
  "es_estudiant": True,
  "qualificacions": [7, 8, 9],
  "socials": {
    "twitterx": "@marcesteveg",
    "github": "@MarcEsteve",
    "linkedin": "Marc Esteve Garcia"
  }
}

# per accedir als valors
# print(persona["nom"]) # "marc"
# print(persona["edat"]) # 25
# print(persona["qualificacions"][2])
# print(persona["socials"]["twitterx"])

# canviar valors en accedir-hi
# persona["nom"] = "esteve"
# persona["qualificacions"][2] = 10

# eliminar completament una propietat
# del persona["edat"]
# print(persona)

# es_estudiant = persona.pop("es_estudiant")
# print(f"es_estudiant: {es_estudiant}")
# print(persona)

# sobreescriure un diccionari amb un altre diccionari
# a = { "nom": "marc", "edat": 25 }
# b = { "nom": "daniel", "es_estudiant": False }
# print(a)
# a.update(b)
# print(a)

# comprovar si existeix una propietat
print("name" in persona) # False
print("nom" in persona) # True

# obtenir totes les claus
print("\nkeys:")
print(persona.keys())
print(persona["socials"].keys())

# obtenir tots els valors
print("\nvalues:")
print(persona.values())

# obtenir tant la clau com el valor
print("\nitems:")
print(persona.items())

for clau, valor in persona.items():
  print(f"{clau}: {valor}")

###
# EXERCICIS (diccionaris)
###

# Consulta els exercicis a 05_dictionaries_exercicis.py
