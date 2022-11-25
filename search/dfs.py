from abstracts import Search, StateSpace
from safe_typing import List


class DFSearch(Search):
    """
    Depth-first search implementation.
    Expands leftmost node(first of most deep nodes) from fringe.
    """

    def __call__(self, state_space: StateSpace) -> List[StateSpace.Action] | None:
        if state_space.is_goal():
            return []

        for action in state_space.action():
            path = self(state_space.result(action))
            if not isinstance(path, type(None)):
                return [action, *path]
