# 📌 Solucions als exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
ciutats = ("Madrid", "Barcelona", "València", "Sevilla", "Bilbao")
print("Segona ciutat:", ciutats[1])
print("Penúltima ciutat:", ciutats[-2])

# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
numeros = (1, 3, 5, 3, 7, 3, 9)
recompte = numeros.count(3)
print("El número 3 apareix", recompte, "vegades a la tupla.")

# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def ordenar_tupla(tupla_numeros):
    return tuple(sorted(tupla_numeros))

numeros_desordenats = (9, 3, 7, 1, 5)
numeros_ordenats = ordenar_tupla(numeros_desordenats)
print("Tupla ordenada:", numeros_ordenats)
