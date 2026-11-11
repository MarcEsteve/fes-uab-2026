###
# EXERCICIS - Disseny i composició
# Construeix la classe SistemaMonitoratge progressivament als exercicis 1-3.
# Reutilitza o copia la classe Sensor del bloc 11 o del material de teoria.
# Sensor té nom, unitat, registrar(valor) i ultima_lectura().
###

# Exercici 1 - Bàsic - Organitzar sensors
# Dissenya SistemaMonitoratge amb un diccionari sensors inicialment buit.
# Implementa afegir_sensor(sensor), amb el nom del sensor com a clau.
# Si el nom ja existeix, llança ValueError i conserva el sensor original.
# Afegeix Sensor("T1", "°C") i Sensor("H1", "%").
# Mostra list(sistema.sensors). Sortida esperada. ['T1', 'H1']
# Intenta afegir un segon T1, captura ValueError i mostra Nom duplicat.
# Cas límit. El sistema acabat de crear té zero sensors.


# Exercici 2 - Bàsic - Delegar el registre
# Afegeix registrar(nom, valor), que busca el sensor i crida el seu registrar.
# Si el nom és desconegut, llança ValueError sense crear cap sensor.
# Registra 20.0 i 24.0 a T1, i 50.0 a H1.
# Mostra les últimes lectures. Sortides esperades. 24.0 i 50.0
# Intenta registrar 3.3 a V1 i "error" a T1, captura cada ValueError i
# mostra Registre rebutjat per cada intent. T1 ha de conservar 24.0.
# Cas límit. La validació numèrica es delega al Sensor corresponent.


# Exercici 3 - Intermedi - Produir un resum
# Afegeix resum(). Retorna una llista de diccionaris amb les claus sensor,
# unitat i valor. valor és l'última lectura o None si l'històric és buit.
# Conserva l'ordre d'incorporació dels sensors.
# En un sistema nou, afegeix T1 en °C i H1 en %, i registra 22.5 a T1.
# Sortida esperada
# [{'sensor': 'T1', 'unitat': '°C', 'valor': 22.5},
#  {'sensor': 'H1', 'unitat': '%', 'valor': None}]
# Cas límit. El resum d'un sistema sense sensors és [].
# Dibuixa també les dues classes i una associació amb 0..* al costat Sensor.
# Explica que un sistema pot contenir zero o diversos sensors.


# Exercici 4 - Repte opcional - Seleccionar alarmes
# Afegeix alarmes(unitat, llindar). Retorna els noms dels sensors de la unitat
# indicada amb última lectura estrictament superior al llindar.
# Ignora els sensors sense lectures i conserva l'ordre d'incorporació.
# Dades. T1 (°C, 28.0), T2 (°C, 25.0), H1 (%, 70.0) i T3 (°C, sense lectures).
# alarmes("°C", 25.0) retorna ['T1'].
# alarmes("V", 3.0) retorna []. En un sistema buit també retorna [].
# Cas límit. Una lectura igual al llindar no genera alarma.
# Raona per què comparem només mesures amb la mateixa unitat.
