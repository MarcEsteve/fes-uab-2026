# Problema 2. Gestió de dispositius d'una xarxa
# Una empresa de telecomunicacions disposa de la llista següent, que representa els identificadors dels dispositius connectats a una xarxa:
# dispositius = [105, 203, 101, 305, 203, 410]
# Desenvolupa un programa en Python que realitzi les operacions següents, en aquest ordre:
# 1.	Afegeix el dispositiu 500 al final de la llista.
# 2.	Insereix el dispositiu 150 a la segona posició.
# 3.	Elimina la primera aparició del dispositiu 203.
# 4.	Ordena els dispositius de menor a major identificador.
# 5.	Mostra la llista final de dispositius i quantes vegades apareix el dispositiu 203.
# Restriccions: Utilitza els mètodes de llistes de Python treballats a classe, sense fer servir bucles ni funcions pròpies.

dispositius = [105, 203, 101, 305, 203, 410]
dispositius.append(500)
dispositius.insert(1, 150)
dispositius.remove(203)
dispositius.sort()
print(dispositius)
print(dispositius.count(203))
