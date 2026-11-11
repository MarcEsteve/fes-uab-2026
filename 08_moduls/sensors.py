"""Càlculs senzills sobre lectures simulades de sensors."""


def mitjana(lectures):
    """Retorna la mitjana de les lectures o None si la llista és buida."""
    if not lectures:
        return None
    return sum(lectures) / len(lectures)


if __name__ == "__main__":
    print(mitjana([20.0, 22.0, 24.0]))  # 22.0
    print(mitjana([]))  # None
