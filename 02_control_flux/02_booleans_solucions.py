###
# SOLUCIONS
###

# Exercici 1: Comparar nombres
# Donats els nombres:
# nombre_a = 8
# nombre_b = 5
# Mostra el resultat de comparar si nombre_a és més gran, més petit o igual
# que nombre_b.
print("\nExercici 1:")
nombre_a = 8
nombre_b = 5
print(f"{nombre_a} > {nombre_b}: {nombre_a > nombre_b}")
print(f"{nombre_a} < {nombre_b}: {nombre_a < nombre_b}")
print(f"{nombre_a} == {nombre_b}: {nombre_a == nombre_b}")

# Exercici 2: Comparar cadenes de text
# Donades les cadenes:
# paraula_a = "Hola"
# paraula_b = "hola"
# Mostra si són iguals i si paraula_a és igual a "Hola".
# Observa si Python distingeix entre majúscules i minúscules.
print("\nExercici 2:")
paraula_a = "Hola"
paraula_b = "hola"
print(f"Les paraules són iguals: {paraula_a == paraula_b}")
print(f"paraula_a és igual a 'Hola': {paraula_a == 'Hola'}")

# Exercici 3: Connexió de xarxa
# Donats els valors booleans:
# router_encès = True
# connexio_activa = False
# Crea una variable anomenada xarxa_disponible que sigui True només si el
# router està encès i la connexió està activa. Mostra'n el resultat.
print("\nExercici 3:")
router_encès = True
connexio_activa = False
xarxa_disponible = router_encès and connexio_activa
print(f"Xarxa disponible: {xarxa_disponible}")

# Exercici 4: Avisos pendents
# Donats els valors booleans:
# actualitzacio_disponible = False
# alerta_critica = True
# Crea una variable anomenada cal_avisar que sigui True si hi ha una
# actualització disponible o una alerta crítica. Mostra'n el resultat.
print("\nExercici 4:")
actualitzacio_disponible = False
alerta_critica = True
cal_avisar = actualitzacio_disponible or alerta_critica
print(f"Cal avisar: {cal_avisar}")

# Exercici 5: Accés a un compte
# Donats els valors booleans:
# compte_actiu = True
# contrasenya_correcta = True
# codi_correcte = False
# dispositiu_de_confiança = True
# compte_bloquejat = False
# Crea una variable anomenada accés_permes que sigui True si el compte està
# actiu, la contrasenya és correcta, el compte no està bloquejat i, a més,
# el codi és correcte o el dispositiu és de confiança. Fes servir and, or i not.
# Mostra'n el resultat.
print("\nExercici 5:")
compte_actiu = True
contrasenya_correcta = True
codi_correcte = False
dispositiu_de_confiança = True
compte_bloquejat = False
accés_permes = (
    compte_actiu
    and contrasenya_correcta
    and (codi_correcte or dispositiu_de_confiança)
    and not compte_bloquejat
)
print(f"Accés permès: {accés_permes}")
