###
# 04 - Mètodes de les llistes
# Els mètodes més importants per treballar amb llistes
###

lista1 = ['a', 'b', 'c', 'd']
print(lista1)
# Afegir o inserir elements a la llista
# lista1[4]='e'
lista1.append('e') # Afegeix un element al final.
print(lista1)

lista1.insert(1, '@') # Insereix un element a la posició indicada pel primer argument.
print(lista1)

lista1.extend(['😃', '😍']) # Afegeix elements al final de la llista.
print(lista1)

# Eliminar elements de la llista
lista1.remove('@') # Elimina la primera aparició del caràcter @.
print(lista1)

ultimo = lista1.pop() # Elimina l'últim element de la llista i també el retorna.
# lista1.pop(-1) # També es pot fer així.
print(ultimo)
print(lista1)

letrab = lista1.pop(1) # Elimina el segon element de la llista (índex 1).
print(letrab)
print(lista1)

# Eliminar directament amb del
del lista1[-1]
print(lista1)

lista1.clear() # Elimina tots els elements de la llista.
print(lista1)

# Eliminar un interval d'elements
lista1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del lista1[1:3]
print(lista1)

# Més mètodes útils
print("Ordenar llistes modificant l'original")
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Ordenar llistes creant-ne una de nova')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

print("Ordenar una llista de cadenes de text (tot en minúscula)")
frutas = ['poma', 'pera', 'llimona', 'poma', 'pera', 'llimona']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una llista de cadenes de text (majúscules i minúscules barrejades)")
frutas = ['poma', 'Pera', 'Llimona', 'poma', 'pera', 'llimona']
frutas.sort(key=str.lower)
# Distingeix entre majúscules i minúscules.
print(frutas)

# Més coses útils
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Mida de la llista -> 4
print(animals.count('🐶')) # Quantes vegades apareix '🐶' -> 2
print('🐼' in animals) # Comprova si hi ha un '🐼' a la llista -> True
print('🐹' in animals) # -> False

###
# EXERCICIS
# Fes servir, sempre que puguis, els mètodes que has après.
###

# Exercici 1: Afegir i modificar elements
# Crea una llista amb els nombres de l'1 al 5.
# Afegeix-hi el nombre 6 al final fent servir append().
# Insereix-hi el nombre 10 a la posició 2 fent servir insert().
# Modifica el primer element de la llista perquè sigui 0.

# Exercici 2: Combinar i buidar llistes
# Crea dues llistes:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Amplia lista_a amb lista_b fent servir extend().
# Elimina la primera aparició del nombre 1 de lista_a fent servir remove().
# Elimina l'element de l'índex 3 de lista_a fent servir pop(). Imprimeix l'element eliminat.
# Buida completament lista_b fent servir clear().

# Exercici 3: Slicing i eliminació amb del
# Crea una llista amb els nombres de l'1 al 10.
# Fes servir slicing i del per eliminar els elements des de l'índex 2 fins al 5
# (sense incloure el 5).
# Imprimeix la llista resultant.

# Exercici 4: Ordenar i comptar
# Crea una llista amb els nombres següents: [5, 2, 8, 1, 9, 4, 2].
# Ordena la llista de manera ascendent fent servir sort().
# Compta quantes vegades apareix el nombre 2 a la llista fent servir count().
# Comprova si el nombre 7 és a la llista fent servir in.

# Exercici 5: Còpia i referència
# Crea una llista anomenada original amb els nombres [1, 2, 3].
# Crea'n una còpia anomenada copia_1 fent servir slicing.
# Crea'n una altra còpia anomenada copia_2 fent servir copy().
# Crea una referència a la llista original anomenada referencia.
# Modifica a 10 el primer element de la llista referencia.
# Imprimeix les quatre llistes (original, copia_1, copia_2 i referencia) i observa'n els canvis.

# Exercici 6: Ordenar cadenes sense distingir entre majúscules i minúscules
# Crea una llista amb les cadenes següents: ["Poma", "pera", "PLÀTAN", "taronja"].
# Ordena la llista sense distingir entre majúscules i minúscules.