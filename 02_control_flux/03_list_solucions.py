###
# SOLUCIONS
###

# Exercici 1: El missatge secret
# Donada la llista següent:
# missatge = ["C", "o", "d", "i", " ", "s", "e", "c", "r", "e", "t"]
# Fent servir slicing i concatenació, crea una llista nova que contingui només
# el missatge "secret".
print("\nExercici 1:")
missatge = ["C", "o", "d", "i", " ", "s", "e", "c", "r", "e", "t"]
secret = missatge[5:]
print(secret)

# Exercici 2: Intercanvi de posicions
# Donada la llista següent:
# nombres = [10, 20, 30, 40, 50]
# Intercanvia la primera i l'última posició fent servir només l'assignació per índex.
print("\nExercici 2:")
nombres = [10, 20, 30, 40, 50]
nombres[0], nombres[-1] = nombres[-1], nombres[0] # Intercanvi en una sola línia.
print(nombres)

# Exercici 3: L'entrepà de llistes
# Donades les llistes següents:
# pa_de_dalt = ["pa de dalt"]
# ingredients = ["pernil", "formatge", "tomàquet"]
# pa_de_sota = ["pa de sota"]
# Crea una llista anomenada entrepà que contingui, en aquest ordre, el pa de dalt,
# els ingredients i el pa de sota.
print("\nExercici 3:")
pa_de_dalt = ["pa de dalt"]
ingredients = ["pernil", "formatge", "tomàquet"]
pa_de_sota = ["pa de sota"]
entrepà = pa_de_dalt + ingredients + pa_de_sota
print(entrepà)

# Exercici 4: Duplicar una llista
# Donada una llista:
# llista = [1, 2, 3]
# Crea una llista nova que contingui duplicats els elements de la llista original.
# Exemple: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print("\nExercici 4:")
llista = [1, 2, 3]
llista_duplicada = llista + llista
print(llista_duplicada)

# Exercici 5: Extreure l'element central
# Donada una llista amb un nombre senar d'elements, extreu-ne l'element central
# fent servir slicing.
# Exemple: llista = [10, 20, 30, 40, 50] -> L'element central és 30
print("\nExercici 5:")
llista = [10, 20, 30, 40, 50]
centre = len(llista) // 2
print(llista[centre])

# Exercici 6: Inversió parcial
# Donada una llista, inverteix-ne només la primera meitat (fent servir slicing
# i concatenació).
# Exemple: llista = [1, 2, 3, 4, 5, 6] -> Resultat: [3, 2, 1, 4, 5, 6]
print("\nExercici 6:")
llista = [1, 2, 3, 4, 5, 6]
meitat = len(llista) // 2
llista_invertida = llista[:meitat][::-1] + llista[meitat:]
print(llista_invertida)