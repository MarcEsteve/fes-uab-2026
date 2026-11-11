###
# 14 - SQLite i històrics de sensors
# Ampliació opcional, fora de les 14 hores obligatòries.
# Dedicació addicional orientativa d'1 h de teoria i 1 h de pràctica.
# Objectius d'aprenentatge
# - Crear una taula i inserir, consultar, modificar i eliminar lectures.
# - Separar les dades del text SQL amb paràmetres ?.
# - Confirmar o desfer una transacció i tancar la connexió.
###

import sqlite3
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory

# Una base de dades relacional organitza registres en taules.
# Cada fila serà una lectura. Les columnes indiquen el seu identificador,
# el nom del sensor, el valor i la unitat. INTEGER, TEXT i REAL són tipus SQL.
# PRIMARY KEY identifica cada fila. NOT NULL exigeix que hi hagi un valor.
# sqlite3 forma part de Python i treballa amb un fitxer local, sense servidor.


def crear_historic(ruta):
    """Crea la taula de lectures si encara no existeix."""
    # connect obre o crea la base de dades a la ruta rebuda.
    # closing tanca la connexió en sortir, també si es produeix un error.
    # El context propi de la connexió gestiona transaccions, però no la tanca.
    with closing(sqlite3.connect(ruta)) as connexio:
        connexio.execute("""
            CREATE TABLE IF NOT EXISTS lectures (
                id INTEGER PRIMARY KEY,
                sensor TEXT NOT NULL,
                valor REAL NOT NULL,
                unitat TEXT NOT NULL
            )
        """)
        connexio.commit()


def afegir_lot(ruta, lectures):
    """Desa tot un lot o desfà les insercions si hi ha un error SQLite."""
    with closing(sqlite3.connect(ruta)) as connexio:
        try:
            for sensor, valor, unitat in lectures:
                # Els ? indiquen posicions de dades. Els valors van separats.
                # execute tracta correctament apòstrofs i altres caràcters.
                connexio.execute(
                    "INSERT INTO lectures (sensor, valor, unitat) "
                    "VALUES (?, ?, ?)",
                    (sensor, valor, unitat),
                )
            # Una transacció agrupa canvis que volem confirmar conjuntament.
            connexio.commit()
        except sqlite3.Error:
            # rollback desfà els canvis del lot encara pendents de confirmar.
            connexio.rollback()
            raise


def llegir_historic(ruta):
    """Recupera tuples (id, sensor, valor, unitat) ordenades per id."""
    with closing(sqlite3.connect(ruta)) as connexio:
        cursor = connexio.execute(
            "SELECT id, sensor, valor, unitat FROM lectures ORDER BY id"
        )
        # execute retorna un cursor. fetchall recupera totes les files.
        return cursor.fetchall()


def main():
    """Demostra les cinc operacions SQL amb una base de dades temporal."""
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "historic.sqlite"
        crear_historic(ruta)
        print(llegir_historic(ruta))  # []
        with closing(sqlite3.connect(ruta)) as connexio:
            cursor = connexio.execute(
                "INSERT INTO lectures (sensor, valor, unitat) "
                "VALUES (?, ?, ?)",
                ("Sensor d'entrada", 3.3, "V"),
            )
            # lastrowid és l'identificador assignat a la nova fila.
            print(cursor.lastrowid)  # 1
            connexio.commit()
        afegir_lot(ruta, [("T1", 21.5, "°C")])
        print(llegir_historic(ruta))

        with closing(sqlite3.connect(ruta)) as connexio:
            # WHERE selecciona files. ORDER BY fixa l'ordre dels resultats.
            # La coma de (nom,) crea una tupla amb un únic element.
            nom = "Sensor d'entrada"
            cursor = connexio.execute(
                "SELECT valor, unitat FROM lectures "
                "WHERE sensor = ? ORDER BY id",
                (nom,),
            )
            print(cursor.fetchall())  # [(3.3, 'V')]

            # UPDATE modifica les files seleccionades per WHERE.
            cursor = connexio.execute(
                "UPDATE lectures SET valor = ? WHERE id = ?", (3.4, 1)
            )
            # rowcount indica el nombre de files modificades o eliminades.
            print(cursor.rowcount)  # 1
            # DELETE elimina les files seleccionades. El filtre és important.
            cursor = connexio.execute(
                "DELETE FROM lectures WHERE id = ?", (2,)
            )
            print(cursor.rowcount)  # 1
            connexio.commit()
        print(llegir_historic(ruta))  # [(1, "Sensor d'entrada", 3.4, 'V')]

        try:
            afegir_lot(ruta, [("H1", 45.0, "%"), (None, 46.0, "%")])
        except sqlite3.IntegrityError:
            # None s'envia com a NULL i incompleix sensor TEXT NOT NULL.
            print("Lot rebutjat i desfet")
        print(llegir_historic(ruta))  # La lectura H1 tampoc s'ha incorporat.

# El fitxer SQLite conserva les dades entre connexions. La carpeta temporal
# només limita la durada de la demostració i es neteja en acabar.
# Les consultes parametritzades separen dades i instruccions SQL.
# Comprovar el resultat després d'un error permet verificar la consistència.
# Pràctica a 01_sqlite_exercicis.py. Tot el bloc és ampliació opcional.
if __name__ == "__main__":
    main()
