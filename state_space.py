from abc import ABC, abstractmethod
from typing import NamedTuple, List, Type, Self
from enum import Enum


class StateSpace(ABC):

    Action = Type[Enum]

    @abstractmethod
    def result(self, action: Action) -> Self:
        ...

    @abstractmethod
    def action(self) -> List[Action]:
        ...

    @abstractmethod
    def cost(self, action: Action) -> int:
        ...
