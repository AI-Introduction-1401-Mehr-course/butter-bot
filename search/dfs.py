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

        path = []
        state_stack = [state_space]
        action_iterator_stack = [iter(state_space.action())]

        while action_iterator_stack:
            try:
                action = next(action_iterator_stack[-1])
                new_state = state_stack[-1].result(action)
                path.append(action)

                if new_state.is_goal():
                    return path

                state_stack.append(new_state)
                action_iterator_stack.append(iter(i for i in new_state.action()))
            except StopIteration:
                try:
                    path.pop()
                except IndexError:
                    return
                state_stack.pop()
                action_iterator_stack.pop()

    def recursive__call__(
        self, state_space: StateSpace
    ) -> List[StateSpace.Action] | None:
        if state_space.is_goal():
            return []

        for action in state_space.action():
            path = self(state_space.result(action))
            if not isinstance(path, type(None)):
                return [action, *path]
