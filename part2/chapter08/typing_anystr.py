from typing import AnyStr


def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b


if __name__ == '__main__':
    concat(b'abc', b'def')
    concat('abc', 'def')
    concat('abc', b'def')
    concat(123, 456)

