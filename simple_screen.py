from abstract_screen import AbstractScreen


class SimpleScreen(AbstractScreen):
    def print(self, text: str = ""):
        print(text)
