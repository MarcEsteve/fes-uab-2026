###
# SOLUCIONS - SQLite
# Tot el bloc és ampliació opcional.
###

import sqlite3
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory


# Exercici 1 - Bàsic - Crear i omplir l'històric
def crear_historic(ruta):
    """Crea la taula de lectures i conserva la que ja existeixi."""
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


def afegir_lectura(ruta, sensor, valor, unitat):
    """Desa una lectura i retorna el seu identificador."""
    with closing(sqlite3.connect(ruta)) as connexio:
        cursor = connexio.execute(
            "INSERT INTO lectures (sensor, valor, unitat) "
            "VALUES (?, ?, ?)",
            (sensor, valor, unitat),
        )
        connexio.commit()
        return cursor.lastrowid


# Exercici 2 - Bàsic - Consultar un sensor
def lectures_sensor(ruta, nom):
    """Retorna les mesures d'un sensor en ordre d'inserció."""
    with closing(sqlite3.connect(ruta)) as connexio:
        cursor = connexio.execute(
            "SELECT valor, unitat FROM lectures "
            "WHERE sensor = ? ORDER BY id",
            (nom,),
        )
        return cursor.fetchall()


# Exercici 3 - Intermedi - Corregir i eliminar lectures
def actualitzar_valor(ruta, identificador, valor):
    """Modifica una lectura i retorna el nombre de files afectades."""
    with closing(sqlite3.connect(ruta)) as connexio:
        cursor = connexio.execute(
            "UPDATE lectures SET valor = ? WHERE id = ?",
            (valor, identificador),
        )
        connexio.commit()
        return cursor.rowcount


def eliminar_lectura(ruta, identificador):
    """Elimina una lectura i retorna el nombre de files afectades."""
    with closing(sqlite3.connect(ruta)) as connexio:
        cursor = connexio.execute(
            "DELETE FROM lectures WHERE id = ?", (identificador,)
        )
        connexio.commit()
        return cursor.rowcount


# Exercici 4 - Repte opcional - Un lot indivisible
def afegir_lot(ruta, lectures):
    """Desa el lot complet o el desfà i propaga l'error SQLite."""
    with closing(sqlite3.connect(ruta)) as connexio:
        try:
            for sensor, valor, unitat in lectures:
                connexio.execute(
                    "INSERT INTO lectures (sensor, valor, unitat) "
                    "VALUES (?, ?, ?)",
                    (sensor, valor, unitat),
                )
            connexio.commit()
        except sqlite3.Error:
            connexio.rollback()
            raise


def main():
    """Prova les quatre solucions en bases de dades temporals."""
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "historic.sqlite"
        crear_historic(ruta)
        print(lectures_sensor(ruta, "Sensor d'entrada"))  # []
        print(afegir_lectura(ruta, "Sensor d'entrada", 3.3, "V"))  # 1
        print(afegir_lectura(ruta, "T1", 21.5, "°C"))  # 2
        crear_historic(ruta)  # Conserva les lectures anteriors.

        afegir_lectura(ruta, "Sensor d'entrada", 3.4, "V")
        print(lectures_sensor(ruta, "Sensor d'entrada"))
        # [(3.3, 'V'), (3.4, 'V')]
        print(lectures_sensor(ruta, "desconegut"))  # []

        # Base independent per reproduir exactament les dades de l'exercici 3.
        ruta_correccio = Path(carpeta) / "correccio.sqlite"
        crear_historic(ruta_correccio)
        afegir_lectura(ruta_correccio, "Sensor d'entrada", 3.3, "V")
        afegir_lectura(ruta_correccio, "T1", 21.5, "°C")
        print(actualitzar_valor(ruta_correccio, 1, 3.5))  # 1
        print(eliminar_lectura(ruta_correccio, 2))  # 1
        print(actualitzar_valor(ruta_correccio, 999, 4.0))  # 0
        print(eliminar_lectura(ruta_correccio, 999))  # 0
        with closing(sqlite3.connect(ruta_correccio)) as connexio:
            print(connexio.execute(
                "SELECT id, sensor, valor, unitat FROM lectures ORDER BY id"
            ).fetchall())  # [(1, "Sensor d'entrada", 3.5, 'V')]

        # Base independent per a la transacció del repte.
        ruta_lots = Path(carpeta) / "lots.sqlite"
        crear_historic(ruta_lots)
        afegir_lot(ruta_lots, [
            ("Sensor d'entrada", 3.3, "V"), ("T1", 21.5, "°C")
        ])
        afegir_lot(ruta_lots, [("H1", 45.0, "%"), ("H1", 46.0, "%")])
        afegir_lot(ruta_lots, [])
        try:
            afegir_lot(ruta_lots, [("H2", 50.0, "%"), (None, 51.0, "%")])
        except sqlite3.IntegrityError:
            print("Lot rebutjat")
        with closing(sqlite3.connect(ruta_lots)) as connexio:
            files = connexio.execute(
                "SELECT id FROM lectures"
            ).fetchall()
            print(len(files))  # 4

        ruta_buida = Path(carpeta) / "buida.sqlite"
        crear_historic(ruta_buida)
        try:
            afegir_lot(ruta_buida, [("H2", 50.0, "%"), (None, 51.0, "%")])
        except sqlite3.IntegrityError:
            print("Lot buit després del rebuig:")
            print(lectures_sensor(ruta_buida, "H2"))  # []


if __name__ == "__main__":
    main()
