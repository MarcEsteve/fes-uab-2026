###
# EXERCICIS - Herència i polimorfisme
# Ampliació opcional. 1 h de pràctica addicional.
# Pots reutilitzar la classe Sensor del fitxer de teoria. Manté les operacions
# registrar, ultima_lectura, mitjana i obtenir_lectures per a tots els tipus.
###

# Exercici 1 - Bàsic - Especialitzar la construcció
# Crea SensorTemperatura i SensorHumitat com a subclasses de Sensor.
# Els seus constructors només reben nom. Utilitza super().__init__ per fixar
# la unitat a °C i %, respectivament, i crear l'històric propi.
# Crea SensorTemperatura("T1") i SensorHumitat("H1").
# Mostra nom, unitat i obtenir_lectures() per a cadascun.
# Sortida esperada
# T1 °C []
# H1 % []
# Cas límit. Les dues instàncies han de començar amb historials independents.


# Exercici 2 - Bàsic - Adaptar la validació
# Especialitza _validar(valor) a cada subclasse i crida super()._validar(valor)
# abans de comprovar el rang. Temperatura admet [-40, 85] °C.
# La humitat admet [0, 100] %.
# Els extrems són vàlids. Rebutja amb ValueError qualsevol lectura invàlida
# abans de canviar l'històric, incloent bool, text, nan i infinits.
# A T1 registra -40 i 85. A H1 registra 0 i 100. Mostra els historials.
# Sortides esperades. [-40, 85] i [0, 100]
# Prova -41 i 86 a T1, i -1 i 101 a H1. Captura cada ValueError i mostra
# Lectura rebutjada. Mostra de nou els historials, que han de conservar-se.
# Prova també True, "25", float("nan") i float("inf") en un sensor buit.
# Tots quatre intents han de ser rebutjats i l'històric ha de continuar buit.


# Exercici 3 - Intermedi - Polimorfisme i còpies
# Implementa obtenir_lectures() a Sensor perquè retorni una còpia de _lectures.
# Crea nous T1 i H1. Registra [20.0, 24.0] a T1 i [40.0, 60.0] a H1.
# Recorre [T1, H1] amb un únic bucle que mostri nom, última lectura, mitjana
# i unitat, utilitzant les mateixes crides per a tots dos tipus.
# Sortida esperada
# T1 24.0 22.0 °C
# H1 60.0 50.0 %
# Afegeix 999.0 a la llista retornada per obtenir_lectures() de T1.
# Mostra l'històric real de T1. Sortida esperada. [20.0, 24.0]
# Cas límit. ultima_lectura() i mitjana() d'un sensor buit retornen None.
# Explica que el prefix _ és una convenció d'ús intern de Python.


# Exercici 4 - Repte opcional - Afegir un tipus de sensor
# Crea SensorTensio com a subclasse de Sensor. Fixa la unitat a V i admet
# lectures entre 0 i 5, amb els dos extrems inclosos.
# Reutilitza la inicialització i la validació numèrica de la classe base.
# Crea V1 i registra 0.0 i 5.0. Intenta registrar 6.0 i captura ValueError.
# Sortida esperada del rebuig. Lectura rebutjada
# Afegeix V1 a la llista de l'exercici 3 i reutilitza el mateix bucle.
# Sortides esperades
# T1 24.0 22.0 °C
# H1 60.0 50.0 %
# V1 5.0 2.5 V
# Cas límit. Després del rebuig, l'històric de V1 és [0.0, 5.0].
# Relaciona aquest disseny amb un SistemaMonitoratge que conté sensors.
