import pytest

import coins
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

    assert machine.coins == [
        coins.Loonie(),
        coins.Toonie(),
        coins.Quarter()
    ]
