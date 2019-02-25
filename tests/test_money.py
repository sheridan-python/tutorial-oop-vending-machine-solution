"""Tests the models.money module."""
from models import money


def test_dollar_amount_repr():
    """
    Asserts that the repr() of DollarAmount can be used to
    construct an identical object.
    """
    amount = money.DollarAmount('9.9')
    expected = "DollarAmount('9.9')"

    assert repr(amount) == expected


def test_dollar_amount_str():
    """
    Asserts that the str() of DollarAmount renders a friendly,
    readable value
    """
    amount = money.DollarAmount('55.2')
    assert str(amount) == '$55.20'


def test_dollar_amount_str_adds_commas_to_thousands():
    """
    Asserts that the returned string includes commas between
    thousands.
    """
    amount = money.DollarAmount('123456')
    assert str(amount) == '$123,456.00'
