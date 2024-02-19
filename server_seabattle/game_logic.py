from string import ascii_uppercase
from typing import List

# Координаты
# Поля для учета положения кораблей
# Выбор кораблей
# Проверка статуса координаты

# Переключение хода
# Отслеживание статуса кораблей

# north - N
# west - W  east - E
# south - S
# ПАКА:D :))

# Написать проверки для S и E

# [
#     'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10',
#     'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10',
#     'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10',
#     'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10',
#     'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10',
#     'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10',
#     'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10',
#     'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10',
#     'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10',
#     'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10',
#     'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10'
# ]

# "A1" "D10" -> ("A", 1) ("D", 10)

empty = 'empty'
attacked = 'attacked'
ship = 'ship'  # link to ship

damaged = 'damaged'
destroyed = 'destroyed'

armored = 'armored'


class Field(object):

    def __init__(self) -> None:
        self._field = self.generate_field()
        self.letters = ascii_uppercase[:11]
        self.digits = list(range(1, 11))

    @property
    def field(self):
        return self._field

    def generate_field(self):
        f = {}
        for l in self.letters:
            for d in self.digits:
                f[f'{l}{d}'] = empty

        return f

    def set_ship(self, ship: object, coords: str, vector: str):  # here!
        # написать логику где относительно направлеия пробегаемся по клеткам и вставляем ссылку на корабль
        pass

    def calculate_ceils(self, start_coord: str, size: int, vector: str) -> List[str]:
        if vector == 'S':
            pass

    def check_coords(self, start_coord: str, size: int, vector: str):
        """Метод получает координату, размер и направление и проверяет свободны ли эти клетки"""
        coords = self.calculate_ceils(start_coord, size, vector)
        for c in coords:
            if not self.is_empty_ceil(c):
                return False
        return True

    def is_empty_ceil(self, ceil):
        return not isinstance(self.field[ceil], AbstractShip)


class AbstractShip(object):
    SIZE = None

    def __init__(self, coords):
        self.coords = coords

    def get_coords(self):
        return self.coords


class Ship1(AbstractShip):
    SIZE = 1


class Ship2(AbstractShip):
    SIZE = 2


class Ship3(AbstractShip):
    SIZE = 3


class Ship4(AbstractShip):
    SIZE = 4


class Player(object):

    def __init__(self):
        self._ships = self.generate_ships()

    def generate_ships(self):
        """я забыл что она делает xD"""
        pass

    def ship_set(self, ship, start_coor, vector):  # like chipset.
        """Fuction used for player to set ships on field."""
        pass


class Interface(object):
    def __init__(self, player, field):
        self.player = player
        self.field = field

    def set_ship_on_the_field(self, ship, vector):
        self.field.set_ship(ship)

    def mark_attacked(self):
        pass

    def mark_damaged(self):
        pass

    def mark_destroed(self):
        pass

    def set_status_ready(self):
        pass

    def render_field(self):
        pass
