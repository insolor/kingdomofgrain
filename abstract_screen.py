from __future__ import annotations

from abc import ABC, abstractmethod


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

    @abstractmethod
    def key(self) -> str:
        # 4010 IF INKEY$<>"" THEN GO TO VAL "4012"
        # 4011 GO TO VAL "4010"
        # 4012 RETURN
        pass

    @abstractmethod
    def input(self) -> str:
        pass
