from typing import Literal


def use_ten(ten: Literal[10]) -> None:
    print(ten)


if __name__ == '__main__':
    use_ten(10)
    use_ten(11)

