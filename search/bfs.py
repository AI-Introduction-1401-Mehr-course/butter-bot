from abstracts import Search, StateSpace
from safe_typing import List, NamedTuple, Tuple


class BFSearch(Search):
    """
    Breadth-first search implementation.
    Expands nodes from fringe in fifo order.
    """

    def __call__(self, state_space: StateSpace) -> List[StateSpace.Action] | None:
        class Node(NamedTuple):
            state_space: StateSpace
            path: List[StateSpace.Action]

        queue = [Node(state_space=state_space, path=[])]
        visited = []

        while queue:
            current_node = queue.pop(0)
            if current_node.state_space.is_goal():
                return current_node.path
            if current_node.state_space.state in visited:
                continue
            visited.append(current_node.state_space.state)
            for action in current_node.state_space.action():
                queue.append(
                    Node(
                        current_node.state_space.result(action),
                        [*current_node.path, action],
                    )
                )
