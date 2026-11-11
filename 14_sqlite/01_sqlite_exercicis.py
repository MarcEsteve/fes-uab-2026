###
# EXERCICIS - SQLite
# Bloc d'ampliació opcional. Dedicació de pràctica orientativa d'1 hora.
# Utilitza sqlite3, contextlib.closing i una ruta dins de TemporaryDirectory.
# Les funcions han de rebre la ruta de la base de dades com a paràmetre.
# Parametritza les dades amb ?. Confirma els canvis i tanca cada connexió.
###

# Exercici 1 - Bàsic - Crear i omplir l'històric
# Implementa crear_historic(ruta) amb CREATE TABLE IF NOT EXISTS.
# La taula lectures ha de tenir id INTEGER PRIMARY KEY, sensor TEXT NOT NULL,
# valor REAL NOT NULL i unitat TEXT NOT NULL.
# Implementa afegir_lectura(ruta, sensor, valor, unitat).
# Utilitza INSERT parametritzat.
# Retorna cursor.lastrowid, l'identificador assignat a la nova fila.
# En una base nova, les dues insercions següents retornen 1 i 2.
# Crear la taula dues vegades ha de conservar les dades existents.
# Si només es crea la taula, SELECT ha de recuperar una llista buida.
lectures_inicials = [("Sensor d'entrada", 3.3, "V"), ("T1", 21.5, "°C")]

# Exercici 2 - Bàsic - Consultar un sensor
# Implementa lectures_sensor(ruta, nom). Retorna tuples (valor, unitat)
# per al sensor indicat, ordenades per id. Utilitza SELECT, WHERE i ORDER BY.
# Amb les dues lectures de l'exercici 1 i una tercera lectura
# ("Sensor d'entrada", 3.4, "V"), la consulta del nom següent ha de retornar
# [(3.3, 'V'), (3.4, 'V')]. Un nom desconegut ha de retornar [].
# Ha de funcionar també amb una taula buida. Parametritza el nom.
nom_sensor = "Sensor d'entrada"

# Exercici 3 - Intermedi - Corregir i eliminar lectures
# Implementa actualitzar_valor(ruta, identificador, valor) amb UPDATE i
# eliminar_lectura(ruta, identificador) amb DELETE.
# Les dues funcions retornen cursor.rowcount, el nombre de files afectades.
# En una base nova amb les dues lectures inicials, actualitza id 1 a 3.5
# i elimina id 2. Cadascuna de les crides ha de retornar 1.
# SELECT id,sensor,valor,unitat ORDER BY id ha de recuperar
# [(1, "Sensor d'entrada", 3.5, 'V')].
# Actualitzar o eliminar id 999 ha de retornar 0 i conservar les altres files.
identificador_inexistent = 999

# Exercici 4 - Repte opcional - Un lot indivisible
# Implementa afegir_lot(ruta, lectures). Insereix les tuples en una transacció.
# Fes commit només quan totes s'hagin inserit. Davant sqlite3.Error,
# fes rollback i propaga l'excepció.
# La connexió s'ha de tancar en tots els casos.
# Sobre una taula amb les dues lectures inicials, un lot vàlid ha d'afegir
# dues files. Un lot buit ha de conservar el contingut anterior.
# lot_invalid insereix primer una fila correcta i després envia None al sensor.
# La restricció NOT NULL genera sqlite3.IntegrityError. Captura'l a la prova.
# Després del lot rebutjat, la base ha de conservar exactament el contingut
# anterior al lot. Comprova també aquest comportament sobre una taula buida.
lot_valid = [("H1", 45.0, "%"), ("H1", 46.0, "%")]
lot_invalid = [("H2", 50.0, "%"), (None, 51.0, "%")]
