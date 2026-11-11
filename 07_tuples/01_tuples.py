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
# Les tuples només tenen dos mètodes: count() i index().
print("Nombre de vegades que apareix el 2 a la tupla:", la_meva_tupla.count(2))  # Compta quantes vegades apareix un valor
print("Índex de la primera aparició del 4:", la_meva_tupla.index(4))  # Retorna l'índex de la primera aparició d'un valor
print("Índex del primer 2 a partir de la posició 2:", la_meva_tupla.index(2, 2))  # Cerca des de l'índex indicat (inclòs)

# També hi podem aplicar funcions integrades de Python (no són mètodes de la tupla).
print("Valor més petit:", min(la_meva_tupla))
print("Valor més gran:", max(la_meva_tupla))
print("Suma dels elements:", sum(la_meva_tupla))
# sorted() retorna una llista ordenada; tuple() la converteix en una tupla nova.
print("Tupla ordenada de menor a major:", tuple(sorted(la_meva_tupla)))
