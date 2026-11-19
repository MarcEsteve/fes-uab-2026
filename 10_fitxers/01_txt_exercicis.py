###
# EXERCICIS - Fitxers TXT
# Treballa amb rutes rebudes per paràmetre i encoding="utf-8".
# Fes les proves dins de TemporaryDirectory per conservar les dades existents.
###

# Exercici 1 - Bàsic - Desar un missatge
# Implementa desar_missatge(ruta, missatge) i llegir_missatge(ruta).
# Escriu tot el missatge amb mode w i recupera'l amb read().
# Entrada de prova, "Sensor de tensió actiu\n".
# llegir_missatge ha de retornar el mateix text amb el salt final.
# Cas límit, el missatge "" es recupera com "".
missatge_inicial = "Sensor de tensió actiu\n"

# Exercici 2 - Bàsic - Comptar lectures
# Implementa comptar_lectures(ruta). Compta les línies que no queden buides
# després d'aplicar strip(), sense convertir-les a nombres.
# Contingut inicial, "20.0\n\n21.5\n   \n". Resultat esperat, 2.
# Un fitxer buit ha de donar 0. Si falta, propaga FileNotFoundError.
contingut_registre = "20.0\n\n21.5\n   \n"

# Exercici 3 - Intermedi - Recuperar valors vàlids
# Implementa llegir_valides(ruta). Converteix cada línia no buida amb float.
# Si una línia genera ValueError, ignora-la i continua amb la següent.
# El contracte d'aquest exercici només inclou decimals finits o text invàlid.
# Entrada, "20.0\nerror\n\n22.0\n". Sortida, [20.0, 22.0].
# Cas límit, totes les línies invàlides o buides han de retornar [].
contingut_amb_error = "20.0\nerror\n\n22.0\n"

# Exercici 4 - Repte opcional - Registre acumulatiu
# Implementa afegir_esdeveniment(ruta, missatge) amb mode a.
# Cada crida afegeix el missatge i un salt de línia.
# Precondició, el missatge rebut no conté salts de línia.
# Amb un fitxer inicialment absent i les crides amb "Inici" i "Aturada",
# la lectura completa ha de donar "Inici\nAturada\n".
# Repetir "Inici" ha d'afegir una tercera línia, conservant les dues anteriors.
esdeveniments = ["Inici", "Aturada"]

# Exercici 5 - Intermedi - Filtrar temperatures
# Implementa filtrar_temperatures(ruta_origen, ruta_desti, llindar).
# Llegeix les temperatures de ruta_origen i desa a ruta_desti només les que
# siguin iguals o superiors al llindar, una per línia i amb un decimal.
# Entrada, "18.5\n25.7\n27.3\n20.5\n" i llindar 25.0.
# La lectura del fitxer de destí ha de donar [25.7, 27.3].
# Si cap temperatura supera el llindar, el fitxer de destí ha d'existir buit.
temperatures_per_filtrar = "18.5\n25.7\n27.3\n20.5\n"
llindar_temperatures = 25.0

# Exercici 6 - Intermedi - Crear un resum d'un fitxer
# Implementa crear_resum(ruta_origen, ruta_resum).
# Llegeix temperatures i escriu un resum amb aquest format exacte:
# "Nombre de lectures: 4\nMínima: 18.5 °C\nMàxima: 27.3 °C\nMitjana: 23.0 °C\n"
# Entrada, "18.5\n25.7\n27.3\n20.5\n". Arrodoneix la mitjana a un decimal.
# El fitxer buit ha de produir només:
# "Nombre de lectures: 0\nNo hi ha dades per resumir.\n"
