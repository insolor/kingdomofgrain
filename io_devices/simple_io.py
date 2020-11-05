from io_devices.abstract_io import AbstractIO


class SimpleIO(AbstractIO):
    def print(self, text: str = ""):
        print(text)
        return self

    def input(self) -> str:
        return input()

    def wait_key(self) -> str:
        return input()
