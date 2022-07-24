"""Testing of utils"""

from src.calculator.utils import add


def test_add():
    """
    Test add function
    :return:
    """
    assert add(1, 2), 3
