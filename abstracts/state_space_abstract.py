from abc import ABC, abstractmethod
from safe_typing import Self, List, Type
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

    @abstractmethod
    def is_goal(self) -> bool:
        ...