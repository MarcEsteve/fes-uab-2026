# Planificació docent de Python

FES · UAB · Curs 2026–2027 · Primer curs dels graus d'Enginyeria de Sistemes de Telecomunicacions i d'Enginyeria Electrònica de Telecomunicacions.

## Abast i prerequisits

El tram obligatori comprèn els blocs 08–13, amb **8 sessions de teoria d'1 hora** i **6 sessions de pràctiques d'1 hora**. L'alumnat ja ha treballat variables, condicionals, llistes, bucles, funcions, diccionaris i tuples als blocs 00–07.

Les prioritats essencial i alta de la ruta del [README](README.md) orienten el temps dedicat a cada contingut. Tots els blocs 08–13 formen part del tram obligatori. Els blocs 14–15 i els exercicis classificats com a repte opcional serveixen d'ampliació. Les quatre hores estimades per a les dues ampliacions queden fora de les 14 hores programades.

Cada subtema té teoria executable, notebook explicatiu, quatre enunciats i quatre solucions corresponents. Els exercicis 1 i 2 són bàsics, el 3 és intermedi i el 4 és un repte opcional. Els exemples utilitzen la biblioteca estàndard, dades simulades i fitxers temporals.

## Sessions de teoria

### T1 · 12 de novembre de 2026 · Mòduls

- **Objectius**. Importar funcionalitats de la biblioteca estàndard, repartir funcions entre mòduls i distingir importació i execució directa.
- **Material**. [01_moduls.py](08_moduls/01_moduls.py), [notebook](08_moduls/01_moduls.ipynb), [conversions.py](08_moduls/conversions.py) i [sensors.py](08_moduls/sensors.py).
- **Distribució dels 60 minuts**. 10 min de repàs de funcions, 15 min d'`import`, `from` i `as`, 20 min de mòduls propis, 10 min de guarda `__main__` i 5 min de síntesi amb una predicció d'execució.
- **Activitat suggerida**. Llegir i provar els exercicis 1 i 2 dels [enunciats](08_moduls/01_moduls_exercicis.py). Identificar la responsabilitat de cada mòdul.
- **Criteri de tancament**. Explicar quines instruccions s'executen quan s'importa un mòdul i convertir 3300 mV en 3,3 V mitjançant una funció importada.
- **Ampliació possible**. Exercici 4. La instal·lació de paquets queda com a lectura posterior.

### T2 · 13 de novembre de 2026 · Excepcions

- **Objectius**. Interpretar `ValueError` i `FileNotFoundError`, gestionar errors concrets i validar abans de canviar les dades.
- **Material**. [01_excepcions.py](09_excepcions/01_excepcions.py) i [notebook](09_excepcions/01_excepcions.ipynb).
- **Distribució dels 60 minuts**. 10 min de lectura d'una fallada, 20 min de `try`, `except`, `else` i `finally`, 20 min de `raise` i rangs físics simulats, 5 min de fitxer absent i 5 min de síntesi.
- **Activitat suggerida**. Exercicis 1 i 2 dels [enunciats](09_excepcions/01_excepcions_exercicis.py), amb entrades vàlides, text invàlid i extrems del domini.
- **Criteri de tancament**. Explicar qui valida i qui decideix com comunicar un error. Reconèixer que `finally` s'executa tant si hi ha error com si l'operació té èxit.
- **Ampliació possible**. Exercici 4 i valors `nan` o `inf`.

### T3 · 19 de novembre de 2026 · TXT i rutes

- **Objectius**. Construir rutes portables, gestionar recursos amb `with` i recuperar mesures a partir de línies de text.
- **Material**. [01_txt.py](10_fitxers/01_txt.py) i [notebook](10_fitxers/01_txt.ipynb).
- **Distribució dels 60 minuts**. 10 min de `Path`, 15 min d'`open`, modes i UTF-8, 20 min de lectura i escriptura per línies, 10 min de funcions reutilitzables i 5 min de casos buits o absents.
- **Activitat suggerida**. Exercicis 1 i 2 dels [enunciats](10_fitxers/01_txt_exercicis.py). Predir el contingut després d'escriure amb `w` i afegir amb `a`.
- **Criteri de tancament**. Recuperar una llista de temperatures i distingir fitxer buit, text invàlid i fitxer absent.
- **Ampliació possible**. Exercici 4 de registre acumulatiu.

### T4 · 20 de novembre de 2026 · CSV i JSON

- **Objectius**. Representar taules i estructures natives, conservar noms i unitats i convertir els tipus recuperats.
- **Material**. [02_csv.py](10_fitxers/02_csv.py), [notebook CSV](10_fitxers/02_csv.ipynb), [03_json.py](10_fitxers/03_json.py) i [notebook JSON](10_fitxers/03_json.ipynb).
- **Distribució dels 60 minuts**. 30 min de CSV amb capçalera, `DictWriter`, `DictReader` i `newline`, seguits de 30 min de JSON amb `dump`, `load`, tipus i errors de sintaxi.
- **Activitat suggerida**. Exercici 2 de [CSV](10_fitxers/02_csv_exercicis.py) i exercici 1 de [JSON](10_fitxers/03_json_exercicis.py). Comparar una mesura llegida com a text amb una mesura numèrica.
- **Criteri de tancament**. Fer una anada i tornada de registres `sensor`, `valor`, `unitat` i explicar per què un JSON correcte pot tenir una estructura inadequada.
- **Ampliació possible**. Exercicis 4 de CSV/JSON i validació detallada de l'esquema. El conjunt de comprovacions del lector es proporciona com a referència.

### T5 · 27 de novembre de 2026 · Primeres classes

- **Objectius**. Distingir classe i instància, interpretar `self` i crear un estat propi dins d'`__init__`.
- **Material**. Primera part de [01_sensor.py](11_classes/01_sensor.py) i [notebook](11_classes/01_sensor.ipynb), fins al registre de lectures.
- **Distribució dels 60 minuts**. 10 min de transició des d'un diccionari, 20 min de constructor i atributs, 20 min de mètodes i crides, 10 min de dues instàncies i predicció de l'estat.
- **Activitat suggerida**. Exercicis 1 i 2 dels [enunciats](11_classes/01_sensor_exercicis.py). Dibuixar les dades dels sensors T1 i H1 després de cada crida.
- **Criteri de tancament**. Explicar per què cada objecte té la seva llista de lectures i què rep `self` en executar un mètode.
- **Ampliació possible**. Simular un tercer sensor de tensió sense modificar el constructor.

### T6 · 4 de desembre de 2026 · Estat i comportament

- **Objectius**. Consultar estat, tractar l'absència de dades i conservar l'històric quan falla la validació.
- **Material**. Segona part de [01_sensor.py](11_classes/01_sensor.py) i [notebook](11_classes/01_sensor.ipynb), consultes, errors i activitat guiada.
- **Distribució dels 60 minuts**. 10 min de repàs d'instàncies, 20 min d'última lectura i mitjana, 15 min de validació abans de modificar, 10 min de casos `None` i zero, 5 min de síntesi de responsabilitats.
- **Activitat suggerida**. Exercici 3 dels [enunciats](11_classes/01_sensor_exercicis.py), amb sensor buit i sensor que registra zero.
- **Criteri de tancament**. Retornar `None` quan falten lectures i conservar les dades anteriors després d'intentar registrar text o una mesura no finita.
- **Ampliació possible**. Exercici 4, recompte de superacions d'un llindar.

### T7 · 11 de desembre de 2026 · Composició i disseny

- **Objectius**. Assignar responsabilitats, delegar operacions i representar una relació entre classes amb UML introductori.
- **Material**. [01_sistema_monitoratge.py](12_poo_disseny/01_sistema_monitoratge.py) i [notebook](12_poo_disseny/01_sistema_monitoratge.ipynb), inclòs el diagrama de classes textual.
- **Distribució dels 60 minuts**. 10 min de responsabilitat única, 20 min de diccionari d'objectes i delegació, 15 min de resum i errors d'identificació, 10 min d'UML i multiplicitat, 5 min de revisió.
- **Activitat suggerida**. Exercicis 1 i 2 dels [enunciats](12_poo_disseny/01_sistema_monitoratge_exercicis.py). Explicar on correspon validar el valor i on correspon rebutjar un nom duplicat.
- **Criteri de tancament**. Registrar dades en dos sensors mitjançant el sistema i interpretar `0..*` al costat Sensor d'una associació UML.
- **Ampliació possible**. Exercici 4 d'alarmes filtrades per unitat. L'herència es treballa al bloc opcional 15.

### T8 · 18 de desembre de 2026 · Proves, depuració i integració

- **Objectius**. Expressar expectatives, verificar casos límit i errors i recórrer el sistema fins al fitxer recuperat.
- **Material**. [01_proves_integracio.py](13_proves_integracio/01_proves_integracio.py) i [notebook](13_proves_integracio/01_proves_integracio.ipynb), amb components facilitats als blocs 10 i 12.
- **Distribució dels 60 minuts**. 10 min d'`assert` i límits d'ús, 20 min de `unittest.TestCase` i comprovacions bàsiques, 15 min de proves d'integració, 10 min de depuració d'una mitjana i 5 min de revisió del projecte.
- **Activitat suggerida**. Exercicis 1 i 2 dels [enunciats](13_proves_integracio/01_proves_integracio_exercicis.py). Comparar la prova d'un sensor amb una prova sistema–fitxer.
- **Criteri de tancament**. Executar proves independents, comprovar una excepció amb `assertRaises` i explicar el resultat d'un sistema buit i d'una lectura zero.
- **Ampliació possible**. Exercici 4 de regressió i depuració. Executar amb `-O` per observar el comportament d'`assert`.

## Sessions de pràctiques

Les sis sessions comparteixen una pauta de 5 min de revisió, 40 min de resolució i experimentació, 10 min de casos límit i 5 min de posada en comú. Els reptes opcionals s'ofereixen si l'alumnat completa els objectius previstos. El docent pot repartir els minuts dels exercicis dins del bloc de resolució.

| Sessió i data de 2026 | Objectius i material | Exercicis suggerits durant els 40 min | Casos límit i tancament | Ampliació possible |
|---|---|---|---|---|
| **P1 · 13 de novembre** | Separar funcions i validar dades. [08](08_moduls/01_moduls_exercicis.py) i [09](09_excepcions/01_excepcions_exercicis.py). | 15 min per 08 E1–E2, 15 min per 09 E1–E2 i 10 min per 09 E3. | Comprovar conversió, text invàlid i extrems del rang. Justificar la ubicació de cada responsabilitat. | 08 E4 o 09 E4. |
| **P2 · 20 de novembre** | Desar i recuperar mesures. [TXT](10_fitxers/01_txt_exercicis.py), [CSV](10_fitxers/02_csv_exercicis.py) i [JSON](10_fitxers/03_json_exercicis.py). | 10 min per TXT E2, 15 min per CSV E3 i 15 min per JSON E1–E2. | Fitxer buit, capçalera sola, nom amb coma i mitjana d'històric buit. Mostrar les dades recuperades i els seus tipus. | TXT E3 o JSON E3 per consolidar errors, seguits de JSON E4 si hi ha temps. |
| **P3 · 27 de novembre** | Construir objectes i registrar estat. [Sensor](11_classes/01_sensor_exercicis.py). | E1 durant 15 min i E2 durant 25 min. | Dues instàncies independents. Provar una entrada invàlida després d'una entrada correcta i inspeccionar l'estat. | Incorporar un tercer sensor i proposar dades de prova. |
| **P4 · 4 de desembre** | Consultar lectures i mitjana, validar el model. [Sensor](11_classes/01_sensor_exercicis.py). | E3 durant 25 min i 15 min per revisar les resolucions pròpies d'E1–E2. | Sensor buit, una lectura zero i diverses lectures. Calcular una mitjana a mà i explicar `None`. | E4 de recompte de llindars. |
| **P5 · 11 de desembre** | Coordinar objectes i explicar el disseny. [SistemaMonitoratge](12_poo_disseny/01_sistema_monitoratge_exercicis.py). | 10 min per E1, 10 min per E2 i 20 min per E3 amb UML. | Sistema buit, nom duplicat, sensor desconegut i sensor sense dades. Revisar el resum en ordre d'incorporació. | E4 d'alarmes per unitat. |
| **P6 · 18 de desembre** | Verificar funcionalitats i integració. [Proves](13_proves_integracio/01_proves_integracio_exercicis.py). | 10 min per E1, 10 min per E2 i 20 min per E3. | Executar des de dades inicials netes. Revisar excepcions i verificar l'anada i tornada tant en CSV com en JSON. | E4 de depuració i regressió. |

Les solucions de cada quartet permeten la revisió final. Cada exercici bàsic inclou les seves dades i es pot resoldre amb el material de referència facilitat. Es recomana preparar les dades de fitxer en una carpeta temporal i tornar a executar les proves després de cada canvi.

## Fites del projecte de sensors

| Bloc | Resultat observable | Concepte d'enginyeria del programari |
|---|---|---|
| [08](08_moduls/) | Funcions de conversió i resum importables. | Modularitat i reutilització. |
| [09](09_excepcions/) | Lectures acceptades o rebutjades amb un error concret. | Validació i contractes. |
| [10](10_fitxers/) | Registres guardats i recuperats en TXT, CSV i JSON. | Separació de persistència i càlcul. |
| [11](11_classes/) | Objectes Sensor amb estat independent. | Agrupació de dades i comportament. |
| [12](12_poo_disseny/) | SistemaMonitoratge que conté sensors i delega el registre. | Responsabilitat única i composició. |
| [13](13_proves_integracio/) | Proves reproduïbles de components i dades recuperades. | Verificació, integració i mantenibilitat. |

El resum d'un sensor sense lectures conté `None`. L'adaptador d'exportació del bloc 13 selecciona les files amb una mesura disponible abans d'escriure CSV o JSON. Un zero es conserva com a mesura vàlida. Aquest acord evita confondre absència de dades amb una lectura real.

## Ampliacions fora del calendari obligatori

### Bloc 14 · SQLite · 2 hores addicionals estimades

- **Material**. [01_sqlite.py](14_sqlite/01_sqlite.py), [notebook](14_sqlite/01_sqlite.ipynb), [exercicis](14_sqlite/01_sqlite_exercicis.py) i [solucions](14_sqlite/01_sqlite_solucions.py).
- **Objectius**. Crear una taula d'històrics, inserir i consultar lectures i aplicar `UPDATE` i `DELETE` amb paràmetres.
- **Teoria, 60 min**. 15 min de connexió i esquema, 20 min d'`INSERT`/`SELECT`, 15 min d'`UPDATE`/`DELETE` i 10 min de transaccions i tancament.
- **Pràctica, 60 min**. Exercicis 1–3 amb una base de dades temporal. Verificar persistència, absència de files i ús de paràmetres. E4 com a repte opcional.
- **Resultat del projecte**. Històric de lectures guardat en una base de dades local.

### Bloc 15 · POO avançada · 2 hores addicionals estimades

- **Material**. [01_herencia.py](15_poo_avancada/01_herencia.py), [notebook](15_poo_avancada/01_herencia.ipynb), [exercicis](15_poo_avancada/01_herencia_exercicis.py) i [solucions](15_poo_avancada/01_herencia_solucions.py).
- **Objectius**. Especialitzar sensors amb herència, reutilitzar inicialització amb `super()` i tractar instàncies amb una interfície comuna.
- **Teoria, 60 min**. 15 min de relació d'especialització, 15 min de `super()`, 15 min de polimorfisme i 15 min d'encapsulació bàsica amb atributs d'ús intern.
- **Pràctica, 60 min**. Exercicis 1–3 amb sensors simulats i comprovacions de límit. E4 com a repte opcional.
- **Resultat del projecte**. Tipus de sensor especialitzats que comparteixen operacions i apliquen les seves validacions.

## Execució i revisió

Executa els scripts des de l'arrel amb `python ruta/al/fitxer.py`, `py` a Windows o `python3` a Linux/macOS. Els exemples i les solucions funcionen amb la biblioteca estàndard de Python. Els notebooks requereixen Jupyter i un kernel Python.

Per revisar un notebook, reinicia el kernel i executa totes les cel·les en ordre. Per revisar una resolució, contrasta el resultat amb l'enunciat, prova el cas límit indicat i comprova que una execució repetida conserva el comportament esperat. Les proves del bloc 13 han d'acabar amb `OK`.

La progressió combina explicació, predicció, execució i justificació. Les qüestions de disseny demanen explicar qui conserva cada dada i qui és responsable de cada operació.
