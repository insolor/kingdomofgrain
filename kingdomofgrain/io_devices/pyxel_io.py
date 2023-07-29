import pyxel

from kingdomofgrain import RESOURCES
from kingdomofgrain.font_utils import char_to_image_index
from kingdomofgrain.io_devices.abstract_io import AbstractIO


class PyxelIO(AbstractIO):
    def __init__(self):
        self.screen = pyxel.Image(256, 192)
        self.font = pyxel.Image(8, 768)
        self.font.load(0, 0, str(RESOURCES / "font.png"))

        self.row = 0
        self.column = 0

        self.ink_color = 11
        self.paper_color = 0
        self.brightness = 0

    def cls(self):
        self.screen.cls(self.paper_color)
        return self

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

    def draw_char(self, column: int, row: int, char: str, ink_color: int):
        char_index = char_to_image_index[char]
        self.screen.blt(column * 8, row * 8, self.font, 0, char_index * 8, 8, 8)

    def draw_text(self, column: int, row: int, text: str, ink_color: int):
        for i, char in enumerate(text):
            self.draw_char(column + i, row, char, ink_color)

    def print(self, text: str = ""):
        self.draw_text(self.column * 8, self.row * 8, text, self.ink_color)
        self.row += 1
        self.column = 0
        print(text)
        return self

    def input(self) -> str:
        return input()  # FIXME

    def wait_key(self) -> str:
        return input()  # FIXME
