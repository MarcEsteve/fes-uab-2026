# 1. Quin resultat retorna bool('False')?
# a) False
# b) None
# c) Es produeix un error
# d) True

print(bool('False')) #True
# 1 d)

# 2. Quina sortida genera el codi següent?
x = 10 
if x > 5: 
     print('A') 
elif x > 8: 
     print('B') 
else: 
     print('C') 
# a) B
# b) A i B
# c) C
# d) A

# 2 d) A

# 3. Quin resultat té l'expressió següent?
not (True and False) or False
# a) False
# b) True
# c) None
# d) TypeError

print(not (True and False) or False) #True
# 3 b) True

# 4. Quin resultat retorna el codi següent?
llista = [1, 2, 3, 4, 5, 6, 7, 8] 
print(llista[1:6:2])

# a) [1, 3, 5]
# b) [2, 3, 4, 5, 6]
# c) [2, 4, 6]
# d) [1, 3, 5, 7]

# 4 c) [2, 4, 6]

# 5. Què imprimeix aquest codi?
comptador = 0
while comptador < 10:
       comptador += 1
       if comptador % 2 == 0:
              continue
       print(comptador)  

# a) 2, 4, 6, 8, 10
# b) 0, 2, 4, 6, 8
# c) 1, 2, 3, 4, 5
# d) 1, 3, 5, 7, 9

# 5 d) 1, 3, 5, 7, 9

# 6. Quin és el resultat d'executar aquest codi?
numeros = [10, 20, 30, 40]
numeros.pop(1) # Elimina l'element a l'índex 1 (20) -> numeros = [10, 30, 40]
numeros.insert(2, 50) # Insereix 50 a l'índex 2 -> numeros = [10, 30, 50, 40]
print(numeros[-2]) # Mostra l'element a l'índex -2 (50)

# a) 20
# b) 30
# c) 50
# d) 40

# 6 c) 50

# 7. Quin missatge imprimirà el programa?
temperatura = 28
humitat = 75

if temperatura > 30 or humitat > 80:
     print('Alerta')
elif temperatura >= 25 and humitat >= 70:
     print('Precaució')
else:
     print('Normal')

# a) Alerta
# b) Precaució
# c) Normal
# d) Alerta i Precaució

# 7 b) Precaució

# 8. Quin resultat mostrarà aquest programa?
valors = [2, 4, 6, 8, 10]
i = 0
while i < len(valors):
     if valors[i] > 5:
          valors.pop(i)
     else:
          i += 1
print(valors)

# a) [2, 4, 6]
# b) [2, 4, 8, 10]
# c) [2, 4]
# d) Es produeix un IndexError

# 8 c) [2, 4]
