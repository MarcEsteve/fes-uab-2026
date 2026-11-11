###
# EXERCICIS - Classes i objectes
# Implementa les activitats en aquest fitxer. Treballa amb dades simulades.
# Els exercicis 1-3 construeixen progressivament la mateixa classe Sensor.
###

# Exercici 1 - Bàsic - Construcció i instàncies
# Defineix Sensor amb __init__(nom, unitat) i els atributs nom, unitat i
# lectures, una llista buida pròpia de cada instància.
# Crea Sensor("T1", "°C") i Sensor("H1", "%").
# Mostra nom, unitat i lectures de cadascun.
# Sortides esperades amb print(nom, unitat, lectures)
# T1 °C []
# H1 % []
# Cas límit. Dos sensors acabats de crear han de tenir historials independents.


# Exercici 2 - Bàsic - Registrar i validar
# Afegeix registrar(valor). Accepta int i float finits, rebutja bool, textos,
# nan i infinits amb ValueError abans de canviar lectures.
# Per a T1 registra 20.0 i 24.0. Per a H1 registra 55.0.
# Sortides esperades dels historials
# [20.0, 24.0]
# [55.0]
# Intenta registrar "error", True i float("inf") a T1 i captura cada error.
# Sortida esperada per cada intent rebutjat. Lectura rebutjada
# Després dels intents, l'històric de T1 ha de continuar sent [20.0, 24.0].
# Cas límit. 0 és vàlid i float("nan") ha de provocar ValueError.


# Exercici 3 - Intermedi - Consultar l'estat
# Afegeix ultima_lectura() i mitjana(). Retornen None si no hi ha lectures.
# Amb les lectures de T1 de l'exercici 2, les consultes retornen 24.0 i 22.0.
# Crea V1 amb unitat V. Abans de registrar res, les dues retornen None.
# Registra 0 a V1. Ara les consultes han de retornar 0 i 0.0.
# Mostra els sis resultats, cadascun en una línia.
# Sortida esperada. 24.0, 22.0, None, None, 0, 0.0 en aquest ordre.
# Cas límit. Una lectura única té com a mitjana el seu propi valor.


# Exercici 4 - Repte opcional - Comptar superacions
# Afegeix comptar_superiors(llindar) a Sensor.
# Rep un llindar numèric finit i retorna quantes lectures són estrictament
# superiors al llindar. No modifiquis l'històric.
# Amb lectures [20.0, 24.0, 24.0, 30.0] i llindar 24.0, retorna 1.
# Amb el mateix històric i llindar 19.0, retorna 4.
# Amb un sensor buit retorna 0. Mostra els tres recomptes.
# Sortida esperada. 1, 4, 0 en aquest ordre.
# Cas límit. Les lectures iguals al llindar no compten com a superacions.
