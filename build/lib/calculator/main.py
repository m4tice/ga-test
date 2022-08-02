"""main module."""

import sys

from calculator.utils import add

sys.path.append("../../src")


def main():
    """
    Testing utils functions implementation
    :return: nothing.
    """
    result_1 = add(1, 2)
    print(result_1)


if __name__ == '__main__':
    main()
