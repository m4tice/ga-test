"""Testing of utils"""

import sys

from calculator.utils import add

sys.path.append("../../src")


def test_add():
    """
    Test add function
    :return:
    """

    return add(0, 0)
#     assert add(1, 2) is 3
#     assert add(3, 4) is 7
#     assert add(0, 2) is 2
#     assert add(0, 0) is 0
#     assert add(0, -1) is -1
#     assert add(-1, -2) is -3
#     assert add(1, -1) is 0
#     assert add(3, -4) is -1
#     assert add(5, -3) is 2


def test_main():
    """
    Main test function
    :return:
    """

    print(test_add())


if __name__ == '__main__':
    test_main()
