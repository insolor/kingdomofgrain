from threading import Thread

import pyxel

from kingdomofgrain import grain
from kingdomofgrain.io_devices.pyxel_io import PyxelIO


class App:
    def __init__(self):
        pyxel.init(256, 192)
        self.device = PyxelIO()

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        Thread(target=grain.main, args=(self.device,)).run()
        pyxel.run(self.update, self.draw)


if __name__ == "__main__":
    App().run()
