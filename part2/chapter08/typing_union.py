from typing import Union


def add(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    return a + b


if __name__ == '__main__':
    print(add(1.1, 1.2))
    print(add(1, 1.2))
    print(add(1, 2))

