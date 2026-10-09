###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
print("\nExercici 1:")
num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))

if num1 > num2:
    print(f"{num1} és més gran que {num2}")
elif num2 > num1:
    print(f"{num2} és més gran que {num1}")
else:
    print("Els nombres són iguals")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
print("\nExercici 2:")
num1 = float(input("Introdueix el primer nombre: "))
num2 = float(input("Introdueix el segon nombre: "))
operacio = input("Introdueix l'operació (+, -, *, /): ")

if operacio == "+":
    resultat = num1 + num2
elif operacio == "-":
    resultat = num1 - num2
elif operacio == "*":
    resultat = num1 * num2
elif operacio == "/":
    if num2 == 0:
        print("Error: no es pot dividir per zero.")
    else:
        resultat = num1 / num2
else:
    print("Operació no vàlida.")

if 'resultat' in locals(): # Comprova si existeix la variable resultat.
    print(f"El resultat és: {resultat}")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.
print("\nExercici 3:")
any = int(input("Introdueix un any: "))

if (any % 4 == 0 and any % 100 != 0) or any % 400 == 0:
    print(f"{any} és un any de traspàs.")
else:
    print(f"{any} no és un any de traspàs.")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)
print("\nExercici 4:")
edat = int(input("Introdueix una edat: "))

if 0 <= edat <= 2:
    print("Nadó")
elif 3 <= edat <= 12:
    print("Infant")
elif 13 <= edat <= 17:
    print("Adolescent")
elif 18 <= edat <= 64:
    print("Adult")
elif edat >= 65:
    print("Persona gran")
else:
    print("Edat no vàlida.")

# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència i el percentatge de paquets perduts i classifica la connexió.
print("\nExercici 6:")
latencia = float(input("Introdueix la latència en ms: "))
perdua = float(input("Introdueix el percentatge de paquets perduts: "))

if latencia < 0:
    print("La latència no pot ser negativa.")
elif perdua < 0 or perdua > 100:
    print("La pèrdua de paquets ha d'estar entre el 0 % i el 100 %.")
elif latencia <= 30 and perdua <= 1:
    print("La connexió és excel·lent.")
elif latencia <= 80 and perdua <= 3:
    print("La connexió és bona.")
elif latencia <= 150 and perdua <= 5:
    print("La connexió és acceptable.")
else:
    print("La connexió és deficient.")

# Exercici 7: Cost mensual d'un pla de dades
# Calcula el preu del pla i, si escau, el cost dels GB addicionals.
print("\nExercici 7:")
pla = input("Introdueix el tipus de pla (bàsic o plus): ").strip().lower()
consum = float(input("Introdueix el consum mensual en GB: "))

if consum < 0:
    print("El consum no pot ser negatiu.")
elif pla == "bàsic":
    cost = 10
    if consum > 10:
        cost += (consum - 10) * 1.50
    print(f"El cost total és: {cost:.2f} €")
elif pla == "plus":
    cost = 20
    if consum > 30:
        cost += (consum - 30) * 0.75
    print(f"El cost total és: {cost:.2f} €")
else:
    print("Tipus de pla no vàlid.")

# Exercici 8: Accés a un compte de client
# Comprova l'estat del compte, la contrasenya i, si cal, el codi de doble verificació.
print("\nExercici 8:")
compte_actiu = input("El compte està actiu? (s/n): ").strip().lower()
contrasenya_correcta = input("La contrasenya és correcta? (s/n): ").strip().lower()

if compte_actiu != "s":
    print("Accés denegat: el compte està desactivat.")
elif contrasenya_correcta != "s":
    print("Accés denegat: la contrasenya és incorrecta.")
else:
    codi_correcte = input("El codi de doble verificació és correcte? (s/n): ").strip().lower()
    if codi_correcte == "s":
        print("Accés permès.")
    else:
        print("Accés denegat: el codi de doble verificació és incorrecte.")

# Exercici 9: Diagnòstic d'un router
# Comprova el router i els indicadors en l'ordre indicat.
print("\nExercici 9:")
router_encès = input("El router està encès? (s/n): ").strip().lower()

if router_encès != "s":
    print("Cal encendre el router.")
else:
    los_encès = input("L'indicador LOS està encès? (s/n): ").strip().lower()
    internet_encès = input("L'indicador d'Internet està encès? (s/n): ").strip().lower()

    if los_encès == "s":
        print("Cal revisar el cable de fibra.")
    elif internet_encès != "s":
        print("Cal contactar amb el proveïdor.")
    else:
        print("La connexió funciona correctament.")

# Exercici 10: Prioritat d'una incidència de xarxa
# Assigna la prioritat segons la criticitat, els usuaris afectats i l'alternativa.
print("\nExercici 10:")
servei_critic = input("La incidència afecta un servei crític? (s/n): ").strip().lower()
usuaris = int(input("Quants usuaris estan afectats? "))

if usuaris < 0:
    print("El nombre d'usuaris no pot ser negatiu.")
else:
    alternativa = input("Hi ha una alternativa de connexió? (s/n): ").strip().lower()

    if (servei_critic == "s" and alternativa != "s") or (usuaris >= 50 and alternativa != "s"):
        print("Prioritat crítica.")
    elif usuaris >= 10 or servei_critic == "s":
        print("Prioritat alta.")
    else:
        print("Prioritat baixa.")