from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractIO(ABC):
    def cls(self):
        return self

    def print(self, text: str = "") -> AbstractIO:
        return self

    def at(self, row: int, column: int) -> AbstractIO:
        return self

    def ink(self, color: int) -> AbstractIO:
        return self

    def bright(self, brightness: int) -> AbstractIO:
        return self

    @abstractmethod
    def wait_key(self) -> str:
        # 4010 IF INKEY$<>"" THEN GO TO VAL "4012"
        # 4011 GO TO VAL "4010"
        # 4012 RETURN
        pass

    @abstractmethod
    def input(self) -> str:
        pass

    @abstractmethod
    def show_image(self, name: str):
        pass
