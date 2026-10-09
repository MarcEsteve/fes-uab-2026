###
# 01 - Sentències condicionals (if, elif, else)
# Permeten executar blocs de codi només si es compleixen certes condicions.
###

# print("\n Sentència condicional simple")

# Podem fer servir la paraula clau "if" per executar un bloc de codi
# només si es compleix una condició.
# edat = 18
# if edat >= 18:
#   print("Ets major d'edat")
#   print("Felicitats!")

# Si no es compleix la condició, no s'executa el bloc de codi.
# edat = 15
# if edat >= 18:
#   print("Ets major d'edat")
# print("Felicitats!")

# Podem fer servir la paraula clau "else" per executar un bloc de codi
# si no es compleix la condició anterior de l'if.
# print("\n Sentència condicional amb else")
# edat = 15
# if edat >= 18:
#   print("Ets major d'edat")
# else:
#   print("Ets menor d'edat")
  
# if edat >= 18:
#   print("Ets major d'edat")
# if edat < 18:
#   print("Ets menor d'edat")

# print("\n Sentència condicional amb elif")
# nota = 7

# A més de fer servir "if" i "else", podem fer servir "elif" per comprovar
# diverses condicions. Tingues en compte que només s'executarà el primer bloc
# de codi que compleixi la condició (o el de l'else, si n'hi ha).
# if nota >= 9:
#   print("Excel·lent!")
# elif nota >= 7:
#   print("Notable!")
# elif nota >= 5:
#   print("Aprovat!")
# else:
#   print("No ha aprovat!")

print("\n Condicions múltiples")
edat = 16
te_carnet = True

# Els operadors lògics de Python són:
# and: True si tots dos operands són certs.
# or: True si almenys un dels operands és cert.
# En JavaScript:
# && equival a and
# || equival a or

# edat = 16
# te_carnet = True

# Si ets major d'edat i tens carnet...
# podràs conduir.
if edat >= 18 and te_carnet:
  print("Pots conduir 🚗")
else:
  print("POLICIA 🚔!!!1!!!")

# En un poble de l'illa Margarita són més permissius i
# et deixen conduir si ets major d'edat O tens carnet.
# if edat >= 18 or te_carnet:
#   print("Pots conduir a l'illa Margarita 🚗")
# else:
#   print("Paga al policia i et deixarà conduir!!!")

# També tenim l'operador lògic "not",
# que ens permet negar una condició.
es_cap_de_setmana = False
# JavaScript -> !
# if not es_cap_de_setmana:
  # print("Marc, va, que hem de fer classe!")

# Podem anidar condicionals, l'un dins de l'altre,
# per comprovar diverses condicions, tot i que
# intentarem evitar-ho per simplificar el codi.
# print("\n Condicionals imbricats")
# edat = 20
# te_diners = False

# if edat >= 18:
#   if te_diners:
#     print("Pots anar a la discoteca")
#   else:
#     print("Pots entrar a la discoteca, però no comprar res")
# else:
#   print("No pots entrar a la discoteca")

# edat = 20
# te_diners = False
# Una manera més senzilla seria:
# if edat < 18:
#   print("No pots entrar a la discoteca")
# elif te_diners:
#   print("Pots anar a la discoteca")
# else:
#   print("Queda't a casa")

# Tingues en compte que, quan s'utilitzen com a condicions,
# alguns valors de Python s'avaluen com a certs o falsos.
# Per exemple, el nombre 5 és True.
# numero = 5
# if numero: # True
#   print("El nombre no és zero")

# En canvi, el nombre 0 s'avalua com a False.
numero = 0
if numero: # False
  print("Aquí no s'entrarà mai")
print("Aquí sí que s'executa i continua fins al final del codi")

# El valor buit "" també s'avalua com a False.
nombre = ""
if nombre:
  print("El nom no és buit")

# Ves amb compte de no confondre l'assignació = amb la comparació ==!
# numero = 3 # assignació
# es_el_tres = numero == 3 # comparació: True

# if es_el_tres:
#   print("El nombre és 3")

# De vegades podem escriure condicionals en una sola línia amb
# expressions condicionals, una forma concisa d'escriure un if-else.
# print("\nL'expressió condicional:")
# [codi si es compleix la condició] if [condició] else [codi si no es compleix]
# En JavaScript seria: [condició] ? [codi si es compleix] : [codi si no es compleix]
edat = 197
missatge = "És major d'edat" if edat >= 18 else "És menor d'edat"
print(missatge)

###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.


# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)