import os
os.system("cls")

# 📌 Exemples de tuples en Python
# Les tuples són col·leccions ordenades i immutables d'elements.
# A diferència de les llistes, no es poden modificar un cop creades.

# 1️⃣ Creació d'una tupla
la_meva_tupla = (1, 2, 3, 2, 4, 2)
print("Tupla original:", la_meva_tupla)
# la_meva_llista = [1, 2, 3, 2, 4, 2]

# 2️⃣ Intentar modificar un valor de la tupla (això donarà error)
# la_meva_tupla[0] = 5  # ❌ TypeError: 'tuple' object does not support item assignment

# 3️⃣ Solució: Convertir la tupla en llista, modificar-la i tornar a tupla
llista = list(la_meva_tupla)  # Convertir a llista
llista[0] = 5  # Modificar el primer element
la_meva_tupla = tuple(llista)  # Convertir de nou a tupla
print("Tupla modificada convertint-la en llista:", la_meva_tupla)

# 4️⃣ Crear una tupla nova amb valors modificats
la_meva_tupla = (5,) + la_meva_tupla[1:]
print("Tupla nova amb valors modificats:", la_meva_tupla)

# 5️⃣ Accedir als elements d'una tupla
print("Primer element:", la_meva_tupla[0])
print("Últim element:", la_meva_tupla[-1])

# 6️⃣ Longitud d'una tupla
print("Nombre d'elements de la tupla:", len(la_meva_tupla))

# 7️⃣ Mètodes disponibles en una tupla
print("Nombre de vegades que apareix el 2 a la tupla:", la_meva_tupla.count(2))  # Compta quantes vegades apareix un valor
print("Índex de la primera aparició del 4:", la_meva_tupla.index(4))  # Retorna l'índex de la primera aparició d'un valor

# 📝 Exercicis sobre tuples
# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
