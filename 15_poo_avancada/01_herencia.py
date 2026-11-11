###
# 15 - Herència, polimorfisme i encapsulació bàsica
# Ampliació opcional. 1 h de teoria i 1 h de pràctica addicionals.
###

# OBJECTIUS D'APRENENTATGE
# - Especialitzar una classe existent mitjançant herència.
# - Reutilitzar la inicialització i la validació amb super().
# - Aplicar una mateixa operació a instàncies de classes diferents.
# - Protegir l'històric amb una convenció d'ús intern i retornar-ne una còpia.

from math import isfinite


# 1. UNA CLASSE BASE AMB UNA INTERFÍCIE COMUNA
# registrar, ultima_lectura, mitjana i obtenir_lectures són les operacions
# públiques que utilitzarem amb qualsevol tipus de sensor.
class Sensor:
    """Model general d'un sensor amb un històric de nombres finits."""

    def __init__(self, nom, unitat):
        """Crea un sensor amb identificació i estat propi."""
        self.nom = nom
        self.unitat = unitat
        # El prefix _ indica ús intern per convenció. Python permet
        # accedir-hi, però el codi client utilitza els mètodes públics.
        self._lectures = []

    def _validar(self, valor):
        """Comprova les condicions comunes abans de canviar l'estat."""
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("La lectura ha de ser un nombre.")
        if isinstance(valor, float) and not isfinite(valor):
            raise ValueError("La lectura ha de ser finita.")

    def registrar(self, valor):
        """Valida una lectura i després l'afegeix a l'històric."""
        # self._validar selecciona el mètode de la instància concreta.
        self._validar(valor)
        self._lectures.append(valor)

    def ultima_lectura(self):
        """Retorna l'última lectura o None si l'històric és buit."""
        if not self._lectures:
            return None
        return self._lectures[-1]

    def mitjana(self):
        """Retorna la mitjana aritmètica o None si no hi ha lectures."""
        if not self._lectures:
            return None
        return sum(self._lectures) / len(self._lectures)

    def obtenir_lectures(self):
        """Retorna una còpia de la llista per consultar l'històric."""
        # Les mesures són nombres immutables. Una còpia de la llista
        # permet modificar la llista retornada sense alterar l'original.
        return self._lectures.copy()


# 2. HERÈNCIA I ESPECIALITZACIÓ
# SensorTemperatura és un tipus de Sensor. Hereta els mètodes anteriors.
# super() permet cridar el comportament de la classe base.
# El rang és una especificació didàctica del sensor simulat.
class SensorTemperatura(Sensor):
    """Sensor simulat de temperatura entre -40 i 85 °C, extrems inclosos."""

    def __init__(self, nom):
        """Reutilitza la inicialització i fixa la unitat de temperatura."""
        super().__init__(nom, "°C")

    def _validar(self, valor):
        """Combina la validació numèrica i el rang de temperatura."""
        super()._validar(valor)
        if not -40 <= valor <= 85:
            raise ValueError("La temperatura ha d'estar entre -40 i 85 °C.")


class SensorHumitat(Sensor):
    """Sensor simulat d'humitat relativa entre 0 i 100 %, inclosos."""

    def __init__(self, nom):
        """Reutilitza la inicialització i fixa la unitat d'humitat."""
        super().__init__(nom, "%")

    def _validar(self, valor):
        """Combina la validació numèrica i el rang d'humitat."""
        super()._validar(valor)
        if not 0 <= valor <= 100:
            raise ValueError("La humitat ha d'estar entre 0 i 100 %.")


# 3. POLIMORFISME
# Podem cridar els mateixos mètodes sobre instàncies de tipus diferents.
# registrar és heretat i crida la versió de _validar de cada instància.
# Afegir un nou tipus amb la mateixa interfície permet reutilitzar el bucle.
def mostrar_resums(sensors):
    """Consulta sensors de tipus diferents mitjançant mètodes comuns."""
    for sensor in sensors:
        print(sensor.nom, sensor.ultima_lectura(), sensor.mitjana(),
              sensor.unitat)


def main():
    """Mostra especialització, polimorfisme i còpia de l'històric."""
    temperatura = SensorTemperatura("T1")
    humitat = SensorHumitat("H1")
    for lectura in [20.0, 24.0]:
        temperatura.registrar(lectura)
    for lectura in [40.0, 60.0]:
        humitat.registrar(lectura)
    mostrar_resums([temperatura, humitat])
    # T1 24.0 22.0 °C
    # H1 60.0 50.0 %

    try:
        temperatura.registrar(90.0)
    except ValueError as error:
        print(error)
    print(temperatura.ultima_lectura())  # 24.0

    copia = temperatura.obtenir_lectures()
    copia.append(999.0)
    print(copia)  # [20.0, 24.0, 999.0]
    print(temperatura.obtenir_lectures())  # [20.0, 24.0]

    # ACTIVITAT GUIADA
    # Segueix una crida temperatura.registrar(25) fins a append.
    # Identifica quan intervenen Sensor i SensorTemperatura.
    # Prediu què passa amb -40, 85, -41, True, "25" i float("nan").


# RELACIÓ AMB EL DISSENY DEL BLOC 12
# Un SistemaMonitoratge conté sensors. Aquesta relació utilitza composició
# d'objectes. SensorTemperatura especialitza Sensor mitjançant herència.
# Podem combinar les dues relacions en un mateix sistema.
# L'herència és adequada quan cada especialització conserva les operacions
# comunes i n'adapta una part del comportament.
# Exercicis a 01_herencia_exercicis.py i solucions a 01_herencia_solucions.py.

if __name__ == "__main__":
    main()
