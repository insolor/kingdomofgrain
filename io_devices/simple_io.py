from io_devices.abstract_io import AbstractIO


class SimpleIO(AbstractIO):
    def show_image(self, name: str):
        print("Здесь должна быть картинка:", name)

    def print(self, text: str = ""):
        print(text)
        return self

    def input(self) -> str:
        return input()

    def wait_key(self) -> str:
        return input()
