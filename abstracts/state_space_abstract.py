from abc import ABC, abstractmethod
from enum import Enum

from safe_typing import List, Self, Type


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
