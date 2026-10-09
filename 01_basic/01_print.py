###
# 01 - print()
# El mòdul print() és el mòdul que ens permet imprimir a la consola
# Serveix per mostrar informació a la consola i t'acompanyarà
# TOTA LA VIDA. Des d'avui fins a la fi dels temps
###

# Aquest és un exemple bàsic de com imprimir un text a la consola
# print("Hola, món!")

# També pots utilitzar cometes simples per imprimir text
# print('Això també funciona amb una cometa')

# Pots imprimir diversos elements separats per un espai
# print("Python", "és", "genial")

# El paràmetre 'sep' permet definir com se separen els elements impresos
# print("Python", "és", "brutal", sep = "-")

# El paràmetre 'end' defineix què s'imprimeix al final de la línia
# print("Això s'imprimeix", end = "\n") # Aquí, 'end' té un salt de línia explícit
# print("en una línia") # Això s'imprimeix a la línia següent

# També es poden imprimir números directament
print(42)
# print(3+2)
# Exemple de com imprimir el símbol de polzada (")
# Si utilitzem cometes dobles dins d'una cadena amb cometes dobles, es produeix un error:
# print("Això és una "polzada"")  # ❌ Això generaria un error de sintaxi

# # ✅ Solució 1: Utilitzar cometes simples per delimitar la cadena
# print('Això és una "polzada" dins una cadena amb cometes simples')

# # ✅ Solució 2: Utilitzar el caràcter d'escapament \ per incloure cometes dobles dins d'una cadena amb cometes dobles
# print("Això és una \"polzada\" dins d'una cadena amb cometes dobles")

# # ✅ Solució 3: Utilitzar cometes triples per definir la cadena
# print("""Això és una "polzada" dins d'una cadena amb cometes triples""")
