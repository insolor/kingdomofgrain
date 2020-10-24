from io_devices.abstract_io import AbstractIO


class SimpleIO(AbstractIO):
    def print(self, text: str = ""):
        print(text)

    def input(self) -> str:
        return input()

    def key(self) -> str:
        return input()
