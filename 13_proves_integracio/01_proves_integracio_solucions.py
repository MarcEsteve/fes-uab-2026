###
# SOLUCIONS - Proves, depuració i integració
# Executa el fitxer per comprovar els assert i catorze proves de unittest.
###

import importlib
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest


ARREL = Path(__file__).resolve().parents[1]
if str(ARREL) not in sys.path:
    sys.path.insert(0, str(ARREL))

modul_disseny = importlib.import_module(
    "12_poo_disseny.01_sistema_monitoratge"
)
modul_csv = importlib.import_module("10_fitxers.02_csv")
modul_json = importlib.import_module("10_fitxers.03_json")
Sensor = modul_disseny.Sensor
SistemaMonitoratge = modul_disseny.SistemaMonitoratge


# Exercici 1 - Bàsic - Comprovar una conversió
def volts_a_milivolts(tensio):
    """Converteix una tensió numèrica de volts a mil·livolts."""
    return tensio * 1000


def comprovar_conversio():
    """Verifica el zero, una tensió positiva i una de negativa."""
    assert volts_a_milivolts(0) == 0, "Conversió del zero incorrecta"
    assert volts_a_milivolts(1.2) == 1200.0, "Conversió positiva incorrecta"
    assert volts_a_milivolts(-0.5) == -500.0, "Conversió negativa incorrecta"
    print("Exercici 1 superat")


# Exercici 2 - Bàsic - Comportament d'un sensor
class TestSensor(unittest.TestCase):
    """Comprova el contracte públic d'un sensor."""

    def test_sensor_buit(self):
        sensor = Sensor("T1", "°C")
        self.assertIsNone(sensor.ultima_lectura())
        self.assertIsNone(sensor.mitjana())

    def test_registre_i_mitjana(self):
        sensor = Sensor("V1", "V")
        sensor.registrar(0.1)
        sensor.registrar(0.2)
        self.assertEqual(sensor.ultima_lectura(), 0.2)
        self.assertAlmostEqual(sensor.mitjana(), 0.15)

    def test_estat_independent(self):
        primer = Sensor("T1", "°C")
        segon = Sensor("T2", "°C")
        primer.registrar(22.5)
        self.assertIsNone(segon.ultima_lectura())

    def test_error_conserva_estat(self):
        sensor = Sensor("T1", "°C")
        sensor.registrar(22.5)
        with self.assertRaises(ValueError):
            sensor.registrar("desconnectat")
        self.assertEqual(sensor.ultima_lectura(), 22.5)


# Exercici 3 - Intermedi - Persistència del resum
def lectures_disponibles(sistema):
    """Selecciona les files amb lectura i conserva el zero."""
    disponibles = []
    for fila in sistema.resum():
        if fila["valor"] is not None:
            disponibles.append(fila)
    return disponibles


class TestIntegracio(unittest.TestCase):
    """Verifica dues persistències amb el mateix contracte de dades."""

    def test_resum_csv(self):
        sistema = SistemaMonitoratge()
        sistema.afegir_sensor(Sensor("T1", "°C"))
        sistema.afegir_sensor(Sensor("H1", "%"))
        sistema.registrar("T1", 22.5)
        sistema.registrar("H1", 48.0)
        esperat = [
            {"sensor": "T1", "unitat": "°C", "valor": 22.5},
            {"sensor": "H1", "unitat": "%", "valor": 48.0},
        ]
        with TemporaryDirectory() as directori:
            ruta = Path(directori) / "lectures.csv"
            modul_csv.desar_csv(ruta, lectures_disponibles(sistema))
            recuperat = modul_csv.llegir_csv(ruta)
        self.assertEqual(recuperat, esperat)

    def test_resum_json(self):
        sistema = SistemaMonitoratge()
        sistema.afegir_sensor(Sensor("T1", "°C"))
        sistema.afegir_sensor(Sensor("H1", "%"))
        sistema.registrar("T1", 22.5)
        sistema.registrar("H1", 48.0)
        esperat = [
            {"sensor": "T1", "unitat": "°C", "valor": 22.5},
            {"sensor": "H1", "unitat": "%", "valor": 48.0},
        ]
        with TemporaryDirectory() as directori:
            ruta = Path(directori) / "lectures.json"
            modul_json.desar_json(ruta, lectures_disponibles(sistema))
            recuperat = modul_json.llegir_json(ruta)
        self.assertEqual(recuperat, esperat)

    def test_sistema_buit_csv(self):
        sistema = SistemaMonitoratge()
        with TemporaryDirectory() as directori:
            ruta = Path(directori) / "buit.csv"
            modul_csv.desar_csv(ruta, lectures_disponibles(sistema))
            recuperat = modul_csv.llegir_csv(ruta)
        self.assertEqual(recuperat, [])

    def test_sistema_buit_json(self):
        sistema = SistemaMonitoratge()
        with TemporaryDirectory() as directori:
            ruta = Path(directori) / "buit.json"
            modul_json.desar_json(ruta, lectures_disponibles(sistema))
            recuperat = modul_json.llegir_json(ruta)
        self.assertEqual(recuperat, [])

    def test_sistema_mixt_csv(self):
        sistema = SistemaMonitoratge()
        sistema.afegir_sensor(Sensor("T1", "°C"))
        sistema.afegir_sensor(Sensor("V1", "V"))
        sistema.registrar("V1", 0)
        esperat = [{"sensor": "V1", "unitat": "V", "valor": 0.0}]
        with TemporaryDirectory() as directori:
            ruta = Path(directori) / "mixt.csv"
            modul_csv.desar_csv(ruta, lectures_disponibles(sistema))
            recuperat = modul_csv.llegir_csv(ruta)
        self.assertEqual(recuperat, esperat)

    def test_sistema_mixt_json(self):
        sistema = SistemaMonitoratge()
        sistema.afegir_sensor(Sensor("T1", "°C"))
        sistema.afegir_sensor(Sensor("V1", "V"))
        sistema.registrar("V1", 0)
        esperat = [{"sensor": "V1", "unitat": "V", "valor": 0.0}]
        with TemporaryDirectory() as directori:
            ruta = Path(directori) / "mixt.json"
            modul_json.desar_json(ruta, lectures_disponibles(sistema))
            recuperat = modul_json.llegir_json(ruta)
        self.assertEqual(recuperat, esperat)


# Exercici 4 - Repte opcional - Reproduir i corregir una errada
# Amb [20, 24], el divisor incorrecte 3 produeix 14.666... en lloc de 22.0.
# Cal dividir pel nombre real de lectures i tractar la llista buida.
def mitjana_corregida(lectures):
    """Retorna la mitjana de nombres finits, o None si la llista és buida."""
    if not lectures:
        return None
    return sum(lectures) / len(lectures)


class TestMitjanaCorregida(unittest.TestCase):
    """Conserva els casos que van permetre detectar i corregir l'errada."""

    def test_llista_buida(self):
        self.assertIsNone(mitjana_corregida([]))

    def test_lectura_zero(self):
        self.assertEqual(mitjana_corregida([0]), 0.0)

    def test_dues_lectures(self):
        self.assertEqual(mitjana_corregida([20, 24]), 22.0)

    def test_valors_oposats(self):
        self.assertEqual(mitjana_corregida([-2, 2]), 0.0)


if __name__ == "__main__":
    comprovar_conversio()
    lectures_problema = [20, 24]
    resultat_erroni = sum(lectures_problema) / (len(lectures_problema) + 1)
    print("Reproducció de l'errada de l'exercici 4:", resultat_erroni)
    print("Resultat corregit:", mitjana_corregida(lectures_problema))
    # argv explícit també permet reutilitzar aquest patró en un notebook.
    unittest.main(argv=["proves_sensors"], verbosity=2)
