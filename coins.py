"""
Stores coin definitions
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Coin:
    value: int
    label: str

    def __str__(self):
        return self.label


@dataclass(frozen=True)
class Nickel(Coin):
    value: int = 5
    label: str = '5¢'


@dataclass(frozen=True)
class Dime(Coin):
    value: int = 10
    label: str = '10¢'


@dataclass(frozen=True)
class Quarter(Coin):
    value: int = 25
    label: str = '25¢'


@dataclass(frozen=True)
class Loonie(Coin):
    value: int = 100
    label: str = '$1'


@dataclass(frozen=True)
class Toonie(Coin):
    value: int = 200
    label: str = '$2'
