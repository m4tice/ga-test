"""main module."""

from src.calculator.utils import add, subtract


def main():
    """
    Testing utils functions implementation
    :return: nothing.
    """
    result_1 = add(1, 2)
    print(result_1)

    result_2 = subtract(2, 1)
    print(result_2)


if __name__ == '__main__':
    main()
