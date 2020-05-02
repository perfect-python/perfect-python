from typing import overload


@overload
def spam(a: int, b:int) -> int:
    ...

@overload
def spam(a: str, b:str, times:int) -> str:
    ...

def spam(a, b, c=None):
    ab = a + b
    if c:
        return ab * c
    return ab

if __name__ == '__main__':
    spam(1, 2)
    spam('x', 'y', 3)
    spam('x', 'y', 'z')
    spam(1.1, 1.2)

