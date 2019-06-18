from dataclasses import FrozenInstanceError
import pytest

import coins


def test_nickel_value():
    coin = coins.Nickel()
    assert coin.value == 5


def test_nickel_str():
    coin = coins.Nickel()
    assert str(coin) == '5¢'


def test_dime_value():
    coin = coins.Dime()
    assert coin.value == 10


def test_dime_str():
    coin = coins.Dime()
    assert str(coin) == '10¢'


def test_quarter_value():
    coin = coins.Quarter()
    assert coin.value == 25


def test_quarter_str():
    coin = coins.Quarter()
    assert str(coin) == '25¢'


def test_loonie_value():
    coin = coins.Loonie()
    assert coin.value == 100


def test_loonie_str():
    coin = coins.Loonie()
    assert str(coin) == '$1'


def test_toonie_value():
    coin = coins.Toonie()
    assert coin.value == 200


def test_toonie_str():
    coin = coins.Toonie()
    assert str(coin) == '$2'


def test_the_coin_constructor_takes_no_arguments():
    """
    Ensure that a developer does not accidentally overwrite the
    coin `value` by providing an argument.

    In other words, we must ensure that __init__ accepts no
    arguments.
    """
    with pytest.raises(TypeError):
        coins.Coin(100)  # Ensure that this isn't possible


def test_the_instance_value_property_is_immutable():
    """
    Ensure that the `value` property of the object cannot be
    modified on an instance of a coin class.

    This is a special feature of Python 3.7 dataclasses which
    allow instance immutability by setting `frozen=True` in the
    dataclass decorator.

    E.g.
        >>> @dataclass(frozen=True)
        >>> class MyClass:
        >>>     ...
    """
    coin = coins.Quarter()
    with pytest.raises(FrozenInstanceError):
        coin.value = 100  # Ensure that this isn't possible
