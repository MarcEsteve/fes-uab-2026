"""Conversions d'unitats reutilitzables del sistema de sensors."""


def celsius_a_kelvin(temperatura):
    """Converteix una temperatura en graus Celsius a kelvins."""
    return temperatura + 273.15


def milivolts_a_volts(tensio):
    """Converteix una tensió en mil·livolts a volts."""
    return tensio / 1000


# Aquesta demostració s'executa en llançar el fitxer directament.
# Quan un altre fitxer importa conversions, només es defineixen les funcions.
if __name__ == "__main__":
    print(celsius_a_kelvin(25))  # 298.15
    print(milivolts_a_volts(3300))  # 3.3
