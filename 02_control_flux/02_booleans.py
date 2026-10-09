###
# 02 - Valors booleans
# Valors lògics: True (cert) i False (fals).
# Són fonamentals per al control del flux i la lògica en programació.
###

import os
os.system("cls") # Windows

# Els booleans representen valors de veritat: True o False.
# print("\nValors booleans bàsics:")
# print(True)
# print(False)

# Els operadors de comparació retornen un valor booleà.
# print("\nOperadors de comparació:")
print("5 > 3:", 5 > 3)        # True
# print("5 < 3:", 5 < 3)        # False
# print("5 == 5:", 5 == 5)      # True (igualtat)
# print("5 != 3:", 5 != 3)      # True (desigualtat)
# print("5 >= 5:", 5 >= 5)      # True (major o igual que)
# print("5 <= 3:", 5 <= 3)      # False (menor o igual que)

# print("\nComparació de cadenes de text:")
print("'poma' < 'pera':", "poma" < "pera") # True
print("'Hola' == 'hola'", "Hola" == "hola") # False

# Operadors lògics: and, or, not
print("\nOperadors lògics:")
print("True and True:", True and True)   # True
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("False or False:", False or False)  # False
print("not True:", not True)             # False
print("not False:", not False)            # True

# Taules de veritat (com a referència):
print("\nTaules de veritat:")
print("\nand:")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\n not:") 
print("A     not A")
print("True ", not True)
print("False", not False)