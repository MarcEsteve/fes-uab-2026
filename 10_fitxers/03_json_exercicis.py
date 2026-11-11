###
# EXERCICIS - JSON
# Fes servir json i fitxers temporals amb codificació UTF-8.
###

# Exercici 1 - Bàsic - Configuració d'un dispositiu
# Implementa desar_configuracio(ruta, configuracio) i llegir_configuracio(ruta)
# amb json.dump i json.load. Fes servir ensure_ascii=False per als accents.
# El diccionari següent s'ha de recuperar igual, incloent-hi True com a bool.
# Cas límit, {} es recupera com {}.
configuracio = {"dispositiu": "Estació UAB", "actiu": True, "periode_s": 5}

# Exercici 2 - Bàsic - Mitjana d'un històric
# Implementa mitjana_historic(ruta). El JSON conté una llista de diccionaris
# vàlids amb sensor, valor i unitat, tots de temperatura i amb valors finits.
# Retorna la mitjana dels camps valor. Amb aquestes lectures s'espera 21.0.
# Amb [] s'espera None. Prepara el fitxer amb json.dump abans de llegir-lo.
historic = [
    {"sensor": "T1", "valor": 20.0, "unitat": "°C"},
    {"sensor": "T1", "valor": 22.0, "unitat": "°C"},
]

# Exercici 3 - Intermedi - Detectar JSON malmès
# Implementa carregar_o_informar(ruta). Retorna les dades si json.load té èxit.
# Si el fitxer falta, imprimeix "Fitxer absent" i retorna None.
# Si el JSON és invàlid, imprimeix "JSON invàlid" i retorna None.
# Casos de prova, fitxer absent, text '{"actiu":' i text '{"actiu": true}'.
# L'últim cas retorna {"actiu": True}. Un JSON null retorna None sense avís.
text_incomplet = '{"actiu":'

# Exercici 4 - Repte opcional - Històric de sensors
# Implementa afegir_lectura(ruta, lectura). Si el fitxer falta, parteix de [].
# Si existeix, recupera la llista, afegeix-hi la lectura i desa-la de nou.
# Precondició, fitxer existent amb una llista JSON vàlida i lectures vàlides.
# Després de dues crides, el fitxer ha de contenir aquestes dues lectures
# en el mateix ordre. La tercera crida amb la primera lectura ha d'afegir-la
# de nou. Conserva l'històric anterior. json.JSONDecodeError s'ha de propagar.
# Aquest exercici s'executa en un únic procés i sense escriptors simultanis.
lectures_noves = [
    {"sensor": "H1", "valor": 45.0, "unitat": "%"},
    {"sensor": "H1", "valor": 46.0, "unitat": "%"},
]
