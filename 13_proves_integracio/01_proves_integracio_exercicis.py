###
# EXERCICIS - Proves, depuració i integració
# Objectiu: justificar el comportament amb exemples normals, límits i errors.
# Cada activitat parteix dels components facilitats als blocs 10 i 12.
# Per importar-los, pots reutilitzar l'adaptador de la teoria.
###

# Exercici 1 - Bàsic - Comprovar una conversió
# Implementa volts_a_milivolts(tensio), que multiplica una tensió numèrica
# expressada en volts per 1000. Escriu tres assert amb missatges entenedors.
# Entrades i sortides esperades: 0 → 0, 1.2 → 1200.0, -0.5 → -500.0.
# El valor negatiu representa una tensió amb polaritat inversa.
# Executa el fitxer i imprimeix "Exercici 1 superat" si totes passen.
# TODO: funció i tres comprovacions.

# Exercici 2 - Bàsic - Comportament d'un sensor
# Crea TestSensor, derivada de unittest.TestCase, amb quatre mètodes test_.
# Utilitza el Sensor facilitat al bloc 12, sense modificar-ne el codi.
# 1. T1 acabat de crear: ultima_lectura() i mitjana() retornen None.
# 2. V1 amb 0.1 i 0.2: última lectura 0.2 i mitjana aproximada 0.15.
# 3. T1 i T2 són instàncies diferents: registrar 22.5 a T1 deixa T2 buit.
# 4. T1 conté 22.5: registrar "desconnectat" genera ValueError i conserva 22.5.
# Empra assertEqual, assertAlmostEqual, assertIsNone i assertRaises.
# Sortida esperada del runner per aquesta classe: 4 proves correctes, OK.
# TODO: classe de proves i execució amb unittest.

# Exercici 3 - Intermedi - Persistència del resum
# Crea TestIntegracio amb sis proves, tres per CSV i tres per JSON.
# A la prova de dades completes crea un SistemaMonitoratge nou, afegeix T1
# (°C) i H1 (%), registra 22.5 a T1 i 48.0 a H1, i desa el resum temporalment.
# Recupera les dades amb les funcions facilitades al bloc 10 i compara-les.
# Ordre esperat: primer T1, després H1.
# Resultat esperat en tots dos formats:
# [{"sensor": "T1", "unitat": "°C", "valor": 22.5},
#  {"sensor": "H1", "unitat": "%", "valor": 48.0}]
# Afegeix lectures_disponibles(sistema), que exclou del resum els sensors
# sense lectures. Les files amb valor 0 s'han de conservar.
# Verifica també aquests dos casos en cadascun dels formats:
# - Sistema sense sensors: recuperes [].
# - T1 (°C) sense lectures i V1 (V) amb 0: recuperes només
#   [{"sensor": "V1", "unitat": "V", "valor": 0.0}].
# Usa TemporaryDirectory, Path i els components de la teoria.
# Sortida esperada per aquesta classe: 6 proves correctes, OK.
# TODO: el filtre i sis proves sense fitxers permanents al repositori.

# Exercici 4 - Repte opcional - Reproduir i corregir una errada
# Una funció de mitjana usa el divisor len(lectures) + 1 i retorna 0 per [].
# Reprodueix l'error per a [20, 24] abans de corregir-lo.
# Escriu mitjana_corregida(lectures) i quatre proves independents.
# Entrades i sortides esperades:
# [] → None, [0] → 0.0, [20, 24] → 22.0, [-2, 2] → 0.0.
# El domini d'entrada és una llista de nombres finits.
# Documenta en un comentari la causa de l'error del divisor i el cas buit.
# Sortida esperada per aquesta classe: 4 proves correctes, OK.
# TODO: reproducció, correcció i proves de regressió.
