###
# EXERCICIS
###

# Exercici 1: Afegir i modificar elements
# Crea una llista amb els nombres de l'1 al 5.
# Afegeix-hi el nombre 6 al final fent servir append().
# Insereix-hi el nombre 10 a la posició 2 fent servir insert().
# Modifica el primer element de la llista perquè sigui 0.
print("\nExercici 1:")
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.insert(2, 10)
lista[0] = 0
print(lista)  # Sortida: [0, 2, 10, 3, 4, 5, 6]

# Exercici 2: Combinar i buidar llistes
# Crea dues llistes:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Amplia lista_a amb lista_b fent servir extend().
# Elimina la primera aparició del nombre 1 de lista_a fent servir remove().
# Elimina l'element de l'índex 3 de lista_a fent servir pop(). Imprimeix l'element eliminat.
# Buida completament lista_b fent servir clear().
print("\nExercici 2:")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
lista_a.remove(1)
elemento_eliminado = lista_a.pop(3)
print(f"Element eliminat: {elemento_eliminado}") # Sortida: Element eliminat: 5
lista_b.clear()
print("Llista a:", lista_a) # Sortida: Llista a: [2, 3, 4, 6, 1, 2]
print("Llista b:", lista_b) # Sortida: Llista b: []

# Exercici 3: Slicing i eliminació amb del
# Crea una llista amb els nombres de l'1 al 10.
# Fes servir slicing i del per eliminar els elements des de l'índex 2 fins al 5
# (sense incloure el 5).
# Imprimeix la llista resultant.
print("\nExercici 3:")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista[2:5]
print(lista)  # Sortida: [1, 2, 6, 7, 8, 9, 10]

# Exercici 4: Ordenar i comptar
# Crea una llista amb els nombres següents: [5, 2, 8, 1, 9, 4, 2].
# Ordena la llista de manera ascendent fent servir sort().
# Compta quantes vegades apareix el nombre 2 a la llista fent servir count().
# Comprova si el nombre 7 és a la llista fent servir in.
print("\nExercici 4:")
lista = [5, 2, 8, 1, 9, 4, 2]
lista.sort()
cantidad_dos = lista.count(2)
esta_el_siete = 7 in lista
print(f"Llista ordenada: {lista}") # Sortida: Llista ordenada: [1, 2, 2, 4, 5, 8, 9]
print(f"Quantitat de 2: {cantidad_dos}") # Sortida: Quantitat de 2: 2
print(f"Hi ha el 7?: {esta_el_siete}") # Sortida: Hi ha el 7?: False

# Exercici 5: Còpia i referència
# Crea una llista anomenada original amb els nombres [1, 2, 3].
# Crea'n una còpia anomenada copia_1 fent servir slicing.
# Crea'n una altra còpia anomenada copia_2 fent servir copy().
# Crea una referència a la llista original anomenada referencia.
# Modifica a 10 el primer element de la llista referencia.
# Imprimeix les quatre llistes (original, copia_1, copia_2 i referencia) i observa'n els canvis.
print("\nExercici 5:")
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print(f"Original: {original}")       # Sortida: Original: [10, 2, 3]
print(f"Còpia 1 (slicing): {copia_1}") # Sortida: Còpia 1 (slicing): [1, 2, 3]
print(f"Còpia 2 (copy()): {copia_2}") # Sortida: Còpia 2 (copy()): [1, 2, 3]
print(f"Referència: {referencia}")     # Sortida: Referència: [10, 2, 3]

# Exercici 6: Ordenar cadenes sense distingir entre majúscules i minúscules
# Crea una llista amb les cadenes següents: ["Poma", "pera", "PLÀTAN", "taronja"].
# Ordena la llista sense distingir entre majúscules i minúscules.
print("\nExercici 6:")
strings = ["Poma", "pera", "PLÀTAN", "taronja"]
strings.sort(key=str.lower)
print(strings) # Sortida: ['pera', 'PLÀTAN', 'Poma', 'taronja']