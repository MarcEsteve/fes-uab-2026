# Fonaments d'Enginyeria de Software amb Python

Materials docents de l'assignatura **Fonaments d'Enginyeria de Software (FES)** de la Universitat Autònoma de Barcelona (**UAB**), curs acadèmic **2026–2027** (Graus d'Enginyeria d'Electrònica de Telecomunicacions i de Sistemes de Telecomunicacions).

---

## Estructura i convenció de fitxers

Els continguts s'organitzen en carpetes temàtiques numerades seguint una progressió lògica d'aprenentatge. Per a cada tema es troba:

- `NN_tema.py`: Explicacions i exemples de codi executables.
- `NN_tema.ipynb`: Versió interactiva en format Jupyter Notebook.
- `NN_tema_exercicis.py`: Enunciats d'exercicis pràctics.
- `NN_tema_solucions.py`: Propostes de resolució dels exercicis.

---

## Ruta d'aprenentatge

| Bloc | Carpeta / Fitxers | Continguts principals | Prioritat | Durada estimada |
|---|---|---|---|---|
| **00. Introducció** | [`00_exemple.py`](00_exemple.py)<br>[`00_explicacio_exemple.ipynb`](00_explicacio_exemple.ipynb) | Primer programa en Python i sortida per consola. | Essencial | 15 min de repàs |
| **01. Conceptes bàsics** | [`01_basic/`](01_basic/) | Sortida (`print`), tipus de dades (`types`), conversions (`cast`), variables i entrada d'usuari (`input`). Inclou recopilatori d'exercicis bàsics. | Essencial | 2 h de repàs |
| **02. Condicionals** | [`02_condicional_if/`](02_condicional_if/) | Estructures de control `if`, `elif`, `else` i operadors booleans (`and`, `or`, `not`). | Essencial | 1 h de repàs |
| **03. Llistes** | [`03_llistes/`](03_llistes/) | Creació, indexació, slicing i mètodes de llista (`append`, `insert`, `remove`, `pop`, `sort`, etc.). | Essencial | 1 h de repàs |
| **04. Bucles** | [`04_bucles/`](04_bucles/) | Bucles `while`, `for`, `break`, `continue` i generació de seqüències amb `range()`. | Essencial | 2 h de repàs |
| **05. Funcions** | [`05_funcions/`](05_funcions/) | Definició de funcions (`def`), paràmetres, arguments i retorn de valors (`return`). | Essencial | 90 min de repàs |
| **06. Diccionaris** | [`06_diccionaris/`](06_diccionaris/) | Estructures clau-valor (`dict`), accés, mètodes i iteració. | Essencial | 1 h de repàs |
| **07. Tuples** | [`07_tuples/`](07_tuples/) | Seqüències immutables (`tuple`), accés, propietats i comparativa amb llistes. | Alta | 30 min de repàs |
| **08. Mòduls** | [`08_moduls/`](08_moduls/) | `import`, `from`, `as`, biblioteca estàndard, mòduls propis i guarda `__main__`. | Essencial | 1 h de teoria |
| **09. Excepcions** | [`09_excepcions/`](09_excepcions/) | `try`, `except`, `else`, `finally`, errors concrets, `raise` i validació. | Essencial | 1 h de teoria |
| **10. Fitxers** | [`10_fitxers/`](10_fitxers/) | `pathlib`, `with`, `open`, TXT, CSV amb `csv` i JSON amb `json`. | Essencial | 2 h de teoria |
| **11. Classes** | [`11_classes/`](11_classes/) | Classes, instàncies, `__init__`, `self`, atributs, mètodes i estat. | Essencial | 2 h de teoria |
| **12. POO i disseny** | [`12_poo_disseny/`](12_poo_disseny/) | Responsabilitats, composició, relacions entre classes i UML introductori. | Essencial | 1 h de teoria |
| **13. Proves i integració** | [`13_proves_integracio/`](13_proves_integracio/) | `assert`, `unittest`, casos límit, depuració i integració de components. | Alta | 1 h de teoria |
| **14. SQLite** | [`14_sqlite/`](14_sqlite/) | Taules, CRUD, consultes parametritzades i persistència d'històrics. | Ampliació | 1 h de teoria + 1 h de pràctica addicionals |
| **15. POO avançada** | [`15_poo_avancada/`](15_poo_avancada/) | Herència, `super()`, polimorfisme i encapsulació bàsica. | Ampliació | 1 h de teoria + 1 h de pràctica addicionals |

Les durades dels blocs 00–07 són estimacions orientatives de repàs dels prerequisits. Els blocs **08–13 són obligatoris** i ocupen les **8 hores de teoria i 6 hores de pràctiques** disponibles. Les pràctiques combinen diversos blocs segons el calendari. Els blocs **14–15 són opcionals**, amb temps addicional al tram de 14 hores. Cada subtema ofereix quatre exercicis, amb el quart classificat com a repte opcional.

### Calendari recomanat del tram 08–13

| Data de 2026 | Teoria, 1 h | Pràctica, 1 h |
|---|---|---|
| 12 de novembre | 08 · Mòduls | — |
| 13 de novembre | 09 · Excepcions | Mòduls i validació de lectures |
| 19 de novembre | 10 · TXT, rutes i recursos | — |
| 20 de novembre | 10 · CSV i JSON | Persistència de mesures |
| 27 de novembre | 11 · Constructors, atributs i mètodes | Construcció i estat de sensors |
| 4 de desembre | 11 · Instàncies, consultes i validació | Estat independent i casos límit |
| 11 de desembre | 12 · Composició i UML | Sistema de monitoratge |
| 18 de desembre | 13 · Proves, depuració i integració | Verificació del sistema complet |

El detall de les 14 sessions, els exercicis suggerits i els criteris de tancament es troba a [PLANIFICACIO_DOCENT.md](PLANIFICACIO_DOCENT.md).

---

## Execució del codi

### Scripts de Python (`.py`)

Executa qualsevol fitxer des de l'arrel del repositori:

```bash
# Windows
py ./01_basic/01_print.py

# Linux / macOS
python3 ./01_basic/01_print.py
```

Per als blocs nous es recomana **Python 3.10 o posterior**. Els scripts utilitzen la biblioteca estàndard i es poden executar amb Python, sense instal·lar paquets addicionals. Exemples des de l'arrel del repositori, amb `python` substituïble per `py` a Windows o `python3` a Linux/macOS.

```bash
python 08_moduls/01_moduls.py
python 09_excepcions/01_excepcions_solucions.py
python 10_fitxers/02_csv.py
python 11_classes/01_sensor.py
python 12_poo_disseny/01_sistema_monitoratge.py
python 13_proves_integracio/01_proves_integracio.py
python 13_proves_integracio/01_proves_integracio_solucions.py
```

Els exemples de persistència utilitzen carpetes temporals que s'eliminen en acabar. Els exercicis proporcionen enunciats i dades inicials perquè hi escriguis la resolució. Els mòduls auxiliars `08_moduls/conversions.py` i `08_moduls/sensors.py` permeten practicar importacions reals.

El bloc 13 reutilitza els components facilitats als blocs 10 i 12. L'adaptador d'importació ja està preparat per als noms numerats de les carpetes. Per comprovar el resultat de les proves, busca `OK` al final de l'informe.

Les ampliacions es poden explorar amb `python 14_sqlite/01_sqlite.py` i `python 15_poo_avancada/01_herencia.py`.

### Notebooks interactius (`.ipynb`)

Els fitxers `.ipynb` es poden obrir directament a **VS Code** (recomanat, amb l'extensió oficial de Jupyter) o bé executant Jupyter Notebook al terminal:

```bash
jupyter notebook
```

Jupyter i el kernel Python són eines per executar els notebooks. Obre el notebook des de la seva carpeta o des de l'arrel del repositori i selecciona **Reinicia el kernel i executa totes les cel·les**. Les cel·les segueixen una seqüència d'objectius, explicacions, exemples i pràctica. Els notebooks nous es distribueixen amb les sortides netes per facilitar l'experimentació.

---

## Metodologia de treball recomanada

1. **Explorar**: Llegeix i executa el fitxer d'exemples (`.py` o `.ipynb`).
2. **Experimentar**: Modifica valors i prediu el comportament abans d'executar.
3. **Practicar**: Resol el fitxer `_exercicis.py` de manera autònoma.
4. **Validar**: Compara el teu resultat amb `_solucions.py` i analitza possibles alternatives.

## Projecte evolutiu de monitoratge de sensors

El fil conductor simula un petit sistema amb sensors de temperatura, humitat i tensió. Funciona amb dades locals, sense maquinari ni serveis externs.

1. **08** separa conversions i resum de lectures en mòduls.
2. **09** valida les mesures i gestiona errors concrets.
3. **10** guarda i recupera registres TXT, CSV i JSON.
4. **11** agrupa nom, unitat, lectures i operacions en la classe `Sensor`.
5. **12** coordina diversos sensors amb `SistemaMonitoratge` i distribueix responsabilitats.
6. **13** verifica els components i el recorregut de dades entre sistema i fitxers.
7. **14**, opcional, conserva l'històric en una base de dades SQLite.
8. **15**, opcional, especialitza sensors i reutilitza comportament amb herència.

Els subtemes inclouen totes les dades necessàries per practicar-los. Els exemples de classes recuperen un model breu i autònom de `Sensor`. El bloc 13 integra les implementacions de referència facilitades. En exportar el resum, l'adaptador d'exportació selecciona els sensors que ja disposen d'una lectura i conserva correctament els valors zero.

Els rangs del sensor de temperatura simulat són de −40 a 85 °C. La humitat relativa admet de 0 a 100 %. La classe genèrica `Sensor` accepta nombres finits i cada especialització opcional pot restringir-ne el domini. Els registres compartits per CSV i JSON tenen les claus `sensor`, `valor` i `unitat`.

