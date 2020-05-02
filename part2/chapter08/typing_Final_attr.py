from typing import Final


class Spam:
    egg: Final[int]
    ham: Final[int]
    toast: Final
    butter: Final = '10g'

    def __init__(self) -> None:
        self.egg = 10
        self.egg = 11
        self.toast = 1

