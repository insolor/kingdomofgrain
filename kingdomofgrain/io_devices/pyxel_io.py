from kingdomofgrain.io_devices.abstract_io import AbstractIO


class PyxelIO(AbstractIO):
    def cls(self):
        return self  # FIXME

    def at(self, row: int, column: int):
        return self  # FIXME

    def ink(self, color: int):
        return self  # FIXME

    def bright(self, brightness: int):
        return self  # FIXME

    def show_image(self, name: str):
        print("Здесь должна быть картинка:", name)  # FIXME

    def print(self, text: str = ""):
        print(text)  # FIXME
        return self

    def input(self) -> str:
        return input()  # FIXME

    def wait_key(self) -> str:
        return input()  # FIXME
