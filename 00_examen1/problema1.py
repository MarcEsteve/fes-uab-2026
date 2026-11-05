# Problema 1. Prioritat d'una incidència de xarxa
# Una empresa de telecomunicacions necessita un programa en Python que determini la prioritat d'una incidència segons el nombre d'usuaris afectats.
# El programa ha de demanar el nombre d'usuaris afectats i mostrar la prioritat segons aquests criteris:
# •	Prioritat crítica: 50 usuaris o més.
# •	Prioritat alta: entre 10 i 49 usuaris.
# •	Prioritat baixa: menys de 10 usuaris.

# Si el nombre d'usuaris és negatiu, el programa ha de mostrar Dades incorrectes.
# Restriccions: Utilitza variables, operadors i estructures condicionals (if, elif, else).

num_usuaris = int(input("Introdueix el nombre d'usuaris afectats: "))
if num_usuaris < 0:
    print("Dades incorrectes")
elif num_usuaris >= 50:
    print("Prioritat crítica")
elif num_usuaris >= 10:
    print("Prioritat alta")
else:
    print("Prioritat baixa")
