import pytest

import coins
import products
from vending_machine import VendingMachine


def test_insert_coin_rejects_integer():
    machine = VendingMachine()
    with pytest.raises(ValueError):
        machine.insert_coin(25)


def test_insert_coin_accepts_quarter():
    machine = VendingMachine()
    quarter = coins.Quarter()
    machine.insert_coin(quarter)


def test_insert_coin_accepts_dime():
    machine = VendingMachine()
    dime = coins.Dime()
    machine.insert_coin(dime)


def test_inserted_coins_are_appended_to_coin_list():
    machine = VendingMachine()
    machine.insert_coin(coins.Loonie())
    machine.insert_coin(coins.Toonie())
    machine.insert_coin(coins.Quarter())

    assert machine.inserted_coins == [
        coins.Loonie(),
        coins.Toonie(),
        coins.Quarter()
    ]


def test_buy_product_rejects_strings():
    machine = VendingMachine()

    with pytest.raises(ValueError):
        machine.buy_product(str)

def test_buy_product_accepts_chips():
    machine = VendingMachine()
    machine.buy_product(products.Chips)


def test_buy_product_accepts_drink():
    machine = VendingMachine()
    machine.buy_product(products.Drink)


def test_buy_product_accepts_candy():
    machine = VendingMachine()
    machine.buy_product(products.Candy)
