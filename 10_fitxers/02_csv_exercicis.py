###
# EXERCICIS - CSV
# Utilitza csv, UTF-8, newline="" i una carpeta temporal per a les proves.
###

# Exercici 1 - Bàsic - Taula de tensions
# Implementa desar_tensions(ruta, tensions) amb csv.writer.
# Escriu la capçalera ["sensor", "volts"] i les files rebudes.
# Amb les dades següents, csv.reader ha de recuperar
# [["sensor", "volts"], ["V1", "3.3"], ["V2", "5.0"]].
# Una llista buida ha de produir només la capçalera.
tensions = [("V1", 3.3), ("V2", 5.0)]

# Exercici 2 - Bàsic - Selecció per llindar
# Implementa sensors_en_alerta(ruta, llindar) amb csv.DictReader.
# El CSV d'entrada té la capçalera sensor,valor,unitat i valors finits vàlids.
# Retorna els noms amb valor >= llindar, conservant l'ordre del fitxer.
# Amb les lectures següents i llindar 25.0 s'espera ["T2", "T3"].
# Amb només capçalera s'espera []. El valor igual al llindar s'inclou.
lectures = [
    {"sensor": "T1", "valor": 20.0, "unitat": "°C"},
    {"sensor": "T2", "valor": 25.0, "unitat": "°C"},
    {"sensor": "T3", "valor": 26.0, "unitat": "°C"},
]

# Exercici 3 - Intermedi - Anada i tornada
# Implementa desar_lectures(ruta, lectures) i recuperar_lectures(ruta).
# Fes servir DictWriter/DictReader i la capçalera sensor,valor,unitat.
# Les entrades són diccionaris vàlids i els valors recuperats han de ser float.
# La llista següent s'ha de recuperar igual, incloent-hi la coma del nom.
# Una llista buida s'ha de recuperar com [], amb capçalera al fitxer.
lectures_amb_coma = [
    {"sensor": "Sala, nord", "valor": 19.5, "unitat": "°C"},
]

# Exercici 4 - Repte opcional - Capçalera incorrecta
# Implementa llegir_amb_capcalera_validada(ruta).
# Exigeix exactament sensor,valor,unitat en aquest ordre.
# Si falta la capçalera o és diferent, genera ValueError.
# Amb capçalera correcta, retorna una llista de diccionaris amb valor float.
# Per simplificar, les files posteriors a la capçalera són completes i vàlides.
# Entrada "nom,valor\nT1,20\n" genera ValueError.
# Entrada "sensor,valor,unitat\n" retorna []. Fitxer buit genera ValueError.
capcalera_incorrecta = "nom,valor\nT1,20\n"
