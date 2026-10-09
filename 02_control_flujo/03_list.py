###
# 03 - Llistes
# Seqüències mutables d'elements.
# Poden contenir elements de tipus diferents.
###

# Creació de llistes
# print("\nCrear llistes")
lista1 = [1, 2, 3, 4, 5] # llista d'enters
lista2 = ["pomes", "peres", "plàtans"] # llista de cadenes
lista3 = [1, "hola", 3.14, True] # llista de tipus diferents

lista_vacia = []
# lista_de_listas = [[1, 2], ['mitjó', 4]]
#       1   [0][0]    2 [0][1]
# 'mitjó'[1][0]       4 [1][1]
# print(lista_de_listas[1][0]) # mitjó
matrix = [[1, 2], [2, 3], [4, 5]]

# print(lista1)
# print(lista2)
# print(lista3)
# print(lista_vacia)
# print(lista_de_listas)
# print(matrix)

# Accés als elements mitjançant l'índex
# print("\nAccés als elements mitjançant l'índex")
fruites = ["pomes", "peres", "plàtans", "maduixes", "kiwi"]
print(fruites[0])  # pomes
print(fruites[1])  # peres
print(fruites[2])  # plàtans
print(fruites[3])  # maduixes
print(fruites[-1]) # kiwi, és la forma a Python de mostra l'últim valor de la llista
print(fruites[-2]) # maduixes

lista_de_listas = [[1, 2], ['mitjó', 4]]
print(lista_de_listas[1][0]) #mitjó
print(lista_de_listas[0][1]) #2
print(lista_de_listas[1][1]) #4

# Selecció de fragments d'una llista (slicing)
numeros_tallats = [1, 2, 3, 4, 5]
print(numeros_tallats[1:4]) # [2, 3, 4]
print(numeros_tallats[:3]) # [1, 2, 3]
print(numeros_tallats[3:]) # [4, 5]
print(numeros_tallats[:]) # [1, 2, 3, 4, 5] Còpia de la llista


# ENCARA HI HA MÉS POSSIBILITATS
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[1:6:2]) # [2, 4, 6] # [inici:final:pas]
print(lista1[::2]) # retorna els elements dels índexs parells, posicions senars
print(lista1[::-1]) # retorna els elements en ordre invers

# Modificar una llista
lista1[0] = 20
print(lista1)
# Compte: si l'índex no existeix, per exemple:
lista1[10] = 100 # Error
# Python no permet afegir elements a una llista mitjançant un índex.

# Afegir elements a una llista
lista1 = [1, 2, 3]

# Forma llarga i menys eficient
lista1 = lista1 + [4, 5, 6]
print(lista1)

# Forma curta i més eficient
lista1 += [7, 8, 9]
print(lista1)

# Consultar la longitud d'una llista
print("Longitud de la llista", len(lista1))

# En JavaScript, la longitud d'un array s'obté amb .length.