###
# 03 - Llistes
# Seqüències mutables d'elements.
# Poden contenir elements de tipus diferents.
###

# Creació de llistes
# print("\nCrear llistes")
llista1 = [1, 2, 3, 4, 5] # llista d'enters
llista2 = ["pomes", "peres", "plàtans"] # llista de cadenes
llista3 = [1, "hola", 3.14, True] # llista de tipus diferents

llista_buida = []
# llista_de_llistes = [[1, 2], ['mitjó', 4]]
#       1   [0][0]    2 [0][1]
# 'mitjó'[1][0]       4 [1][1]
# print(llista_de_llistes[1][0]) # mitjó
matriu = [[1, 2], [2, 3], [4, 5]]

# print(llista1)
# print(llista2)
# print(llista3)
# print(llista_buida)
# print(llista_de_llistes)
# print(matriu)

# Accés als elements mitjançant l'índex
# print("\nAccés als elements mitjançant l'índex")
fruites = ["pomes", "peres", "plàtans", "maduixes", "kiwi"]
print(fruites[0])  # pomes
print(fruites[1])  # peres
print(fruites[2])  # plàtans
print(fruites[3])  # maduixes
print(fruites[-1]) # kiwi, és la manera de mostrar l'últim valor de la llista a Python
print(fruites[-2]) # maduixes

llista_de_llistes = [[1, 2], ['mitjó', 4]]
print(llista_de_llistes[1][0]) # mitjó
print(llista_de_llistes[0][1]) # 2
print(llista_de_llistes[1][1]) # 4

# Selecció de fragments d'una llista (slicing)
nombres_tallats = [1, 2, 3, 4, 5]
print(nombres_tallats[1:4]) # [2, 3, 4]
print(nombres_tallats[:3]) # [1, 2, 3]
print(nombres_tallats[3:]) # [4, 5]
print(nombres_tallats[:]) # [1, 2, 3, 4, 5] Còpia de la llista


# ENCARA HI HA MÉS POSSIBILITATS
llista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(llista1[1:6:2]) # [2, 4, 6] # [inici:final:pas]
print(llista1[::2]) # retorna els elements dels índexs parells, posicions senars
print(llista1[::-1]) # retorna els elements en ordre invers

# Modificar una llista
llista1[0] = 20
print(llista1)
# Compte: si l'índex no existeix, per exemple:
llista1[10] = 100 # Error
# Python no permet afegir elements a una llista mitjançant un índex.

# Afegir elements a una llista
llista1 = [1, 2, 3]

# Forma llarga i menys eficient
llista1 = llista1 + [4, 5, 6]
print(llista1)

# Forma curta i més eficient
llista1 += [7, 8, 9]
print(llista1)

# Consultar la longitud d'una llista
print("Llargada de la llista", len(llista1))

# En JavaScript, la longitud d'un array s'obté amb .length.