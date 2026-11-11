###
# 13 - Proves, depuració i integració
# Imprescindible: assert, unittest, casos límit i integració de dades.
# Objectius d'aprenentatge
# - Expressar resultats esperats amb comprovacions reproduïbles.
# - Verificar comportaments normals, límits i errors de manera aïllada.
# - Integrar els components facilitats als blocs 10 i 12.
###

import importlib
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest


# 1. Recuperar components que ja funcionen
# Les carpetes i els fitxers docents comencen amb números. importlib permet
# importar-los mitjançant el nom complet escrit com a cadena. Afegim l'arrel
# al camí de cerca perquè l'script funcioni des de qualsevol directori.
# Aquest petit adaptador ja està preparat. La pràctica se centra en les proves.
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


# 2. assert comprova una expectativa durant el desenvolupament
# Si és falsa, Python genera AssertionError amb el missatge indicat.
# Amb python -O es poden desactivar els assert. La validació d'entrades
# es manté dins dels components amb if i raise, tal com vam veure al bloc 09.
def volts_a_milivolts(tensio):
    """Converteix una tensió numèrica de volts a mil·livolts."""
    return tensio * 1000


def demostrar_asserts():
    """Comprova un exemple conegut i el límit zero."""
    assert volts_a_milivolts(1.2) == 1200.0, "Conversió incorrecta"
    assert volts_a_milivolts(0) == 0, "El zero s'ha de conservar"
    print("Les dues comprovacions amb assert han passat.")


# 3. unittest agrupa proves i informa de cada error
# Una classe de proves deriva de unittest.TestCase. Aquí el patró està donat.
# Cada mètode test_... és una prova independent amb dades acabades de crear.
# assertEqual compara valors. assertIsNone comprova l'absència de lectura.
# assertAlmostEqual admet les petites diferències dels nombres decimals.
# assertRaises comprova que l'error esperat es produeix dins del with.
class TestSensor(unittest.TestCase):
    """Proves unitàries del comportament d'un únic sensor."""

    def test_sensor_sense_lectures(self):
        sensor = Sensor("T1", "°C")
        self.assertIsNone(sensor.ultima_lectura())
        self.assertIsNone(sensor.mitjana())

    def test_registre_i_mitjana(self):
        sensor = Sensor("V1", "V")
        sensor.registrar(0.1)
        sensor.registrar(0.2)
        self.assertEqual(sensor.ultima_lectura(), 0.2)
        self.assertAlmostEqual(sensor.mitjana(), 0.15)

    def test_instancies_independents(self):
        primer = Sensor("T1", "°C")
        segon = Sensor("T2", "°C")
        primer.registrar(22.5)
        self.assertIsNone(segon.ultima_lectura())

    def test_valor_invalid_conserva_estat(self):
        sensor = Sensor("T1", "°C")
        sensor.registrar(22.5)
        with self.assertRaises(ValueError):
            sensor.registrar("desconnectat")
        self.assertEqual(sensor.ultima_lectura(), 22.5)


# 4. Una prova d'integració recorre diversos components
# Creem el sistema, registrem una mesura, exportem el resum i el recuperem.
# TemporaryDirectory manté cada prova aïllada i elimina els fitxers en acabar.
# La prova compara totes les dades, inclosos el nom, la unitat i el valor.
# Un sensor pot existir sense lectures. El resum expressa aquest estat amb
# None, mentre que CSV i JSON de mesures esperen un valor numèric finit.
# Preparem les files disponibles abans de persistir-les. El valor 0 és una
# lectura vàlida, per això comprovem is not None en lloc de si és cert.
def lectures_disponibles(sistema):
    """Retorna només les files del resum que ja tenen una lectura."""
    disponibles = []
    for fila in sistema.resum():
        if fila["valor"] is not None:
            disponibles.append(fila)
    return disponibles


class TestIntegracio(unittest.TestCase):
    """Proves del recorregut sensor → sistema → fitxer → dades."""

    def test_recorregut_csv(self):
        sistema = SistemaMonitoratge()
        sistema.afegir_sensor(Sensor("T1", "°C"))
        sistema.registrar("T1", 22.5)
        esperat = [{"sensor": "T1", "unitat": "°C", "valor": 22.5}]
        with TemporaryDirectory() as directori:
            ruta = Path(directori) / "lectures.csv"
            modul_csv.desar_csv(ruta, lectures_disponibles(sistema))
            recuperat = modul_csv.llegir_csv(ruta)
        self.assertEqual(recuperat, esperat)

    def test_recorregut_json(self):
        sistema = SistemaMonitoratge()
        sistema.afegir_sensor(Sensor("H1", "%"))
        sistema.registrar("H1", 48.0)
        esperat = [{"sensor": "H1", "unitat": "%", "valor": 48.0}]
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


# 5. Depurar amb una prova que reprodueix l'error
# Exemple de fallada: una mitjana de [20, 24] retorna 14.666... perquè el
# divisor és len(lectures) + 1. El resultat esperat és 22.0.
# Passos de treball
# - Reproduir el problema amb dades petites i un resultat calculat a mà.
# - Localitzar la línia amb un punt d'interrupció o un print temporal.
# - Inspeccionar suma i nombre de lectures i corregir el divisor.
# - Executar la prova original i afegir els casos [] i [0].
# Una prova que conserva aquest exemple evita repetir la mateixa errada.
# Consulta l'exercici 4 per fer aquesta activitat de depuració.


def executar_proves():
    """Executa les deu proves i retorna el resultat detallat."""
    carregador = unittest.TestLoader()
    suite = unittest.TestSuite([
        carregador.loadTestsFromTestCase(TestSensor),
        carregador.loadTestsFromTestCase(TestIntegracio),
    ])
    return unittest.TextTestRunner(verbosity=2).run(suite)


# Execució: python 13_proves_integracio/01_proves_integracio.py
# En importar el fitxer, les definicions estan disponibles per reutilitzar.
if __name__ == "__main__":
    demostrar_asserts()
    resultat = executar_proves()
    if not resultat.wasSuccessful():
        raise SystemExit(1)

# Pràctica: 01_proves_integracio_exercicis.py
# Solucions: 01_proves_integracio_solucions.py
