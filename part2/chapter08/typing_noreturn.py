from typing import NoReturn


def something_return() -> NoReturn:
    return True


def raise_if_true(flag:bool) -> NoReturn:
    if flag:
       raise Exception('raise!')


def raise_always() -> NoReturn:
    raise Exception('raise always')


