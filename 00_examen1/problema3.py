# Problema 3. Control del consum de dades d'una xarxa
# Una empresa de telecomunicacions vol controlar el consum de dades d'un dispositiu que té un límit de 100 GB mensuals.
# Desenvolupa un programa en Python que demani repetidament la quantitat de GB consumits en cada connexió.
# El programa ha de:
# 1.	Utilitzar un bucle while per continuar demanant consums mentre el total acumulat sigui inferior a 100 GB i no s'hagin registrat 10 connexions.
# 2.	Acumular els GB consumits i comptar el nombre de connexions registrades.
# 3.	Finalitzar automàticament quan s'arribi als 100 GB o s'hagin registrat 10 connexions.
# 4.	Mostrar el consum total acumulat i el nombre de connexions registrades.
# 5.	Mostrar el consum mitjà per connexió, si s'ha registrat almenys una connexió.
# Restriccions: Utilitza un bucle while, variables, operadors i, com a màxim, una estructura condicional if. No utilitzis llistes ni funcions pròpies.
# Considera que els consums introduïts són nombres positius.

total_consum = 0
connexions = 0

while total_consum < 100 and connexions < 10:
    consum = float(input("Introdueix el consum en GB: "))
    total_consum += consum
    connexions += 1

print("Consum total acumulat:", total_consum)
print("Connexions registrades:", connexions)
if connexions > 0:
    print("Consum mitjà per connexió:", total_consum / connexions)
