"""main module."""

from calculator.utils import add

import sys

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
