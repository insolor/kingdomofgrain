from threading import Thread

import pyxel

from kingdomofgrain import game
from kingdomofgrain.io_devices.pyxel_io import PyxelIO


class App:
    def __init__(self):
        pyxel.init(256, 192)
        self.device = PyxelIO()
        self.screen = self.device.screen

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, self.screen, 0, 0, 256, 192)
        pass

    def run(self):
        Thread(target=game.main, args=(self.device,)).start()
        pyxel.run(self.update, self.draw)


if __name__ == "__main__":
    App().run()
