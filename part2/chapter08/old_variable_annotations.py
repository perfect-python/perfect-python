a = 1  # type: int
b = 2  # type: int
c = '1'  # type: str
d = '2'  # type: str
e = 1


def add(x:int, y:int) -> int:
    return x + y


if __name__ == '__main__':
    print(add(a, b))
    print(add(c, d))
    e = '1'

