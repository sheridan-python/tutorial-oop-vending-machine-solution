"""
Stores coin definitions
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Nickel:
    value: int = 5


@dataclass(frozen=True)
class Dime:
    value: int = 10


@dataclass(frozen=True)
class Quarter:
    value: int = 25


@dataclass(frozen=True)
class Loonie:
    value: int = 100


@dataclass(frozen=True)
class Toonie:
    value: int = 200
