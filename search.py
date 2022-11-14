from abc import ABC, abstractmethod
from typing import List

from state_space import StateSpace


class Search(ABC):
    @abstractmethod
    def __call__(self, state_space: StateSpace) -> List[StateSpace.Action] | None:
        ...
