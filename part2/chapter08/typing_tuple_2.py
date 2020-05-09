from typing import Tuple


def sum_all(data:Tuple[int, ...]) -> int:
    return sum(data)


if __name__ == '__main__':
    print(sum_all((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

