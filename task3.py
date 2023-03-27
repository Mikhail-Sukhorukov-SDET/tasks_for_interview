"""Есть вагон из 9 купе - в каждом купе по 4 места - всего 36 мест
нужно определить по номеру места номер купе."""


def get_kupe_number(place_number: int) -> int:
    """Определить номер купе по номеру места"""
    pass


assert get_kupe_number(4) == 1
assert get_kupe_number(5) == 2
assert get_kupe_number(19) == 5
assert get_kupe_number(20) == 5
assert get_kupe_number(21) == 6
