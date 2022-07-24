"""Testing of utils"""

from src.calculator.utils import add, subtract, multiply


def test_add():
    """
    Test add function
    :return:
    """
    assert add(1, 2), 3
