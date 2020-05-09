from typing import final


class Spam:

    @final
    def eat(self) -> None:
        pass


class Egg(Spam):

    def eat(self) -> None:
        pass

