from dataclasses import dataclass

@dataclass
class Product:
    name: str = ''
    price: int = 0

    def __str__(self):
        return f'{self.name}: ${self.price / 100}'


@dataclass
class Chips(Product):
    name: str = 'Chips'
    price: int = 225


@dataclass
class Drink(Product):
    name: str = 'Drink'
    price: int = 275


@dataclass
class Candy(Product):
    name: str = 'Candy'
    price: int = 315
