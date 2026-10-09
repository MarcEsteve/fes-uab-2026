###
# SOLUCIONS (diccionaris)
###

# Exercici 1: Crear un diccionari
print("\nExercici 1:")
estudiant = {
  "nom": "Anna",
  "edat": 19,
  "assignatures": ["FES", "Matemàtiques", "Física"]
}
print(estudiant)

# Exercici 2: Accedir i modificar
print("\nExercici 2:")
print(estudiant["assignatures"][1])  # Matemàtiques
estudiant["edat"] = 20
print(estudiant["edat"])

# Exercici 3: Afegir i eliminar
print("\nExercici 3:")
estudiant["grau"] = "Enginyeria de Sistemes de Telecomunicació"
del estudiant["edat"]
print(estudiant)

# Exercici 4: Comprovar claus
print("\nExercici 4:")
print("nom" in estudiant)    # True
print("email" in estudiant)  # False

# Exercici 5: Recórrer un diccionari
print("\nExercici 5:")
for clau, valor in estudiant.items():
  print(f"{clau}: {valor}")

# Exercici 6: Comptar paraules
print("\nExercici 6:")
paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
recompte = {}
for paraula in paraules:
  if paraula in recompte:
    recompte[paraula] += 1
  else:
    recompte[paraula] = 1
print(recompte)  # {'sol': 3, 'lluna': 2, 'estrella': 1}
