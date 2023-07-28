import pyxel

from kingdomofgrain.io_devices.abstract_io import AbstractIO


class PyxelIO(AbstractIO):
    def __init__(self):
        self.row = 0
        self.column = 0

        self.ink_color = 7
        self.paper_color = 0
        self.brightness = 0

    def cls(self):
        pyxel.cls(0)
        return self  # FIXME

    def at(self, row: int, column: int):
        self.row = row
        self.column = column
        return self

    def ink(self, color: int):
        self.ink_color = color
        return self

    def paper(self, color: int):
        self.paper_color = color
        return self

    def bright(self, brightness: int):
        self.brightness = brightness
        return self

    def show_image(self, name: str):
        print("Здесь должна быть картинка:", name)  # FIXME

    def print(self, text: str = ""):
        print(text)  # FIXME
        return self

    def input(self) -> str:
        return input()  # FIXME

    def wait_key(self) -> str:
        return input()  # FIXME
