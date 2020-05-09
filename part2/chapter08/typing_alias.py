from typing import NewType, List, Tuple

Item = Tuple[str, int, int]
Cart = List[Item]


def calc_price(cart:Cart) -> int:
    total = 0
    for item in cart:
        total += item[1] * item[2]
    return total

