from safe_typing import List
from abstracts import Search, StateSpace


class IDSearch(Search):
    def __call__(self, state_space: StateSpace) -> List[StateSpace.Action] | None:
        depth = 0
        while self._limited_dfs(state_space, depth) is None:
            depth = depth + 1

        return self._limited_dfs(state_space, depth)

    def _limited_dfs(self, state_space: StateSpace, depth: int):
        if depth == 0:
            if state_space.is_goal():
                return []
            return None

        for action in state_space.action():
            path = self._limited_dfs(state_space.result(action), depth - 1)
            if not isinstance(path, type(None)):
                return [action, *path]
