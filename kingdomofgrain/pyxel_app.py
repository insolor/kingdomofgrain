import pyxel


class App:
    def __init__(self):
        pyxel.init(256, 192)

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        pyxel.run(self.update, self.draw)


if __name__ == "__main__":
    App().run()
