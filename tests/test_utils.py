"""Testing of utils"""

import sys

from calculator.utils import add

sys.path.append("../../src")


def test_add():
    """
    Test add function
    :return:
    """

    assert add(1, 2) == 3
    assert add(3, 4) == 7
    assert add(0, 2) == 2
    assert add(0, 0) == 0
    assert add(0, -1) == -1
    assert add(-1, -2) == -3
    assert add(1, -1) == 0
    assert add(3, -4) == -1
    assert add(5, -3) == 2
