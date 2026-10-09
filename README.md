# Fonaments d'Enginyeria de Software amb Python

Repositori de materials de l'assignatura **Fonaments d'Enginyeria de Software (FES)** de la Universitat Autònoma de Barcelona, curs acadèmic **2026–2027**.

El material està pensat per a l'alumnat del **Grau d'Enginyeria d'Electrònica de Telecomunicacions** i del **Grau d'Enginyeria de Sistemes de Telecomunicacions**. Mitjançant exemples i exercicis en Python, s'hi treballen els fonaments de la programació i la construcció progressiva de solucions de programari.

> Aquest repositori és un material docent en evolució. Els continguts disponibles i l'organització dels exercicis poden créixer o canviar durant el curs.

## Com fer servir aquest repositori

Els materials s'organitzen en carpetes numerades que indiquen un **ordre recomanat d'aprenentatge**. Dins de cada carpeta, els fitxers principals presenten exemples i conceptes; quan hi ha fitxers d'exercicis i solucions, segueixen aquests exemples.

Un cicle d'estudi recomanat:

1. Llegeix i executa el fitxer principal del tema.
2. Modifica els exemples: canvia les dades, prediu el resultat i comprova'l.
3. Fes els exercicis sense consultar les solucions.
4. Executa el teu codi amb diversos casos, inclosos els casos límit.
5. Compara'l amb les solucions i assegura't d'entendre'n les diferències.

Les solucions són una possible manera de resoldre cada exercici; no necessàriament l'única.

## Requisits i execució

Cal tenir Python instal·lat. Per comprovar-ho, obre un terminal:

```powershell
py --version
```

En alguns sistemes també es pot fer servir:

```bash
python --version
```

Executa les ordres des de la carpeta arrel del repositori. Per exemple, a Windows:

```powershell
py .\01_basic\01_print.py
```

O bé, si `python` és la comanda disponible:

```bash
python ./01_basic/01_print.py
```

Canvia el camí del fitxer per executar qualsevol altre exemple. Els fitxers que fan servir `input()` esperen que introdueixis dades al terminal. Els notebooks `.ipynb` es poden obrir amb Jupyter Notebook o amb VS Code i l'extensió de Jupyter.

### Obrir els materials amb Jupyter Notebook

Si Jupyter Notebook està en funcionament a `http://localhost:8888`, pots obrir el repositori al navegador i accedir directament a alguns materials:

- [Obrir la carpeta del repositori a Jupyter](http://localhost:8888/tree/OneDrive/Escritorio/UAB/2026-2027/FES/fes-uab-2026)
- [Obrir l'exemple `01_print.py`](http://localhost:8888/tree/OneDrive/Escritorio/UAB/2026-2027/FES/fes-uab-2026/01_basic/01_print.py)
- [Obrir el notebook `01_print.ipynb`](http://localhost:8888/notebooks/OneDrive/Escritorio/UAB/2026-2027/FES/fes-uab-2026/01_basic/01_print.ipynb)

Els enllaços són locals: només funcionen quan el servidor Jupyter està iniciat al port `8888` i pot accedir a aquesta ruta del repositori.

## Ruta d'aprenentatge

### 0. Primer contacte amb Python

Fitxers d'introducció a l'arrel:

- [`exemple.py`](exemple.py): primer programa i sortida per pantalla.
- [`explicacio_exemple.ipynb`](explicacio_exemple.ipynb): explicació interactiva de l'exemple.

### 1. Conceptes bàsics

Carpeta [`01_basic/`](01_basic/). Presenta els elements necessaris per escriure i executar programes petits:

| Ordre | Fitxer principal | Contingut |
|---|---|---|
| 1 | [`01_print.py`](01_basic/01_print.py) | Mostrar informació amb `print()` i treballar amb cadenes de text. |
| 2 | [`02_types.py`](01_basic/02_types.py) | Tipus de dades bàsics. |
| 3 | [`03_cast.py`](01_basic/03_cast.py) | Conversió entre tipus de dades. |
| 4 | [`04_variables.py`](01_basic/04_variables.py) | Variables, assignació, f-strings i convencions de noms. |
| 5 | [`05_input.py`](01_basic/05_input.py) | Entrada de dades amb `input()` i conversió de valors. |

Per practicar, hi ha exercicis i solucions específics per tema, com ara [`01_print_exercicis.py`](01_basic/01_print_exercicis.py) i [`01_print_solucions.py`](01_basic/01_print_solucions.py). També hi ha els fitxers agregats [`exercicis-basics.py`](01_basic/exercicis-basics.py) i [`solucions-basics.py`](01_basic/solucions-basics.py).

### 2. Control del flux i estructures de dades

Carpeta [`02_control_flux/`](02_control_flux/). Practica la presa de decisions i les primeres estructures de dades:

| Ordre | Fitxer principal | Contingut |
|---|---|---|
| 1 | [`01_if.py`](02_control_flux/01_if.py) | Condicionals `if`, `elif` i `else`, operadors lògics i expressions condicionals. |
| 2 | [`02_booleans.py`](02_control_flux/02_booleans.py) | Valors booleans, comparacions i operadors `and`, `or` i `not`. |
| 3 | [`03_list.py`](02_control_flux/03_list.py) | Creació de llistes, índexs, slicing i modificació d'elements. |
| 4 | [`04_list_methods.py`](02_control_flux/04_list_methods.py) | Mètodes de llista per afegir, eliminar, ordenar i consultar elements. |

Els exercicis i les solucions estan separats en fitxers com [`01_if_exercicis.py`](02_control_flux/01_if_exercicis.py), [`01_if_solucions.py`](02_control_flux/01_if_solucions.py), [`02_booleans_exercicis.py`](02_control_flux/02_booleans_exercicis.py), [`02_booleans_solucions.py`](02_control_flux/02_booleans_solucions.py), [`03_list_exercicis.py`](02_control_flux/03_list_exercicis.py), [`03_list_solucions.py`](02_control_flux/03_list_solucions.py), [`04_list_methods_exercicis.py`](02_control_flux/04_list_methods_exercicis.py) i [`04_list_methods_solucions.py`](02_control_flux/04_list_methods_solucions.py).

### 3. Bucles i altres estructures

Carpeta [`03_bucles/`](03_bucles/). Aplega materials de bucles i altres estructures que permeten organitzar programes:

| Fitxer | Contingut |
|---|---|
| [`01_loop_while.py`](03_bucles/01_loop_while.py) | Bucle `while`, comptadors, `break`, `continue`, `else` i validació repetida. Inclou exercicis comentats al mateix fitxer. |
| [`02_loop_for.py`](03_bucles/02_loop_for.py) | Iteració amb `for`, `enumerate()`, bucles imbricats i comprensions de llista. Inclou exercicis comentats al mateix fitxer. |
| [`03_range.py`](03_bucles/03_range.py) | Exemples amb `range()`. |
| [`04_functions.py`](03_bucles/04_functions.py) | Definició de funcions, paràmetres, arguments i valors de retorn. |
| [`05_dictionaries.py`](03_bucles/05_dictionaries.py) | Diccionaris i operacions amb parelles clau-valor. |
| [`06_tuplas.py`](03_bucles/06_tuplas.py) | Tuples, accés als elements, immutabilitat i mètodes disponibles. |

En aquesta carpeta conviuen fitxers de solucions amb el sufix `_solutions.py` —com [`02_loop_for_solutions.py`](03_bucles/02_loop_for_solutions.py) i [`03_range_solutions.py`](03_bucles/03_range_solutions.py)— i exercicis inclosos als fitxers principals. Consulta la carpeta per veure quins materials estan disponibles per a cada tema; aquesta part del repositori s'anirà completant.

## Organització i noms dels fitxers

En general, els fitxers segueixen aquests patrons:

- `NN_tema.py`: exemples i contingut principal del tema.
- `NN_tema_exercicis.py`: enunciats per practicar sense solucions.
- `NN_tema_solucions.py` o `NN_tema_solutions.py`: solucions dels exercicis.

La convenció encara no és uniforme a tot el repositori. En alguns temes, els exercicis apareixen comentats al fitxer principal o s'agrupen en un únic fitxer. Fes servir l'índex de cada carpeta i aquesta guia com a orientació; els fitxers disponibles són la referència definitiva.

## Àmbit de l'assignatura

La ruta actual comença amb els conceptes bàsics de Python, continua amb condicionals i estructures de dades, i introdueix bucles, funcions, diccionaris i tuples. Aquests fonaments permeten avançar cap a la resolució algorítmica de problemes i l'aplicació de la programació a contextos d'enginyeria, electrònica, sistemes i telecomunicacions.

El repositori és complementari a les explicacions i activitats de classe: no substitueix les indicacions del professorat sobre el calendari, els lliuraments o els continguts avaluables.
