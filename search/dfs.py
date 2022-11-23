from safe_typing import List
from abstracts import Search, StateSpace


class DFSearch(Search):
    def __call__(self, state_space: StateSpace) -> List[StateSpace.Action] | None:
        if state_space.is_goal():
            return []

        for action in state_space.action():
            path = self(state_space.result(action))
            if not isinstance(path, type(None)):
                return [action, *path]
