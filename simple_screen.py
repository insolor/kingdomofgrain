from abstract_screen import AbstractScreen


class SimpleScreen(AbstractScreen):
    def print(self, text: str = ""):
        print(text)

    def input(self) -> str:
        return input()

    def key(self) -> str:
        return input()
