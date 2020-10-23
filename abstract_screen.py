from __future__ import annotations

from abc import ABC


class AbstractScreen(ABC):
    def cls(self):
        return self

    def print(self, text: str = "") -> AbstractScreen:
        return self

    def at(self, row: int, column: int) -> AbstractScreen:
        return self

    def ink(self, color: int) -> AbstractScreen:
        return self

    def bright(self, brightness: int) -> AbstractScreen:
        return self
