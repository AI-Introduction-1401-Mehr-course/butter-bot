from typing import List, NamedTuple, Tuple
from search import Search
from state_space import StateSpace


class BFSearch(Search):
    def __call__(self, state_space: StateSpace) -> List[StateSpace.Action] | None:
        class Node(NamedTuple):
            state_space: StateSpace
            path: List[StateSpace.Action]

        queue = [Node(state_space=state_space, path=[])]

        while queue:
            current_node = queue.pop(0)
            if current_node.state_space.is_goal():
                return current_node.path
            for action in current_node.state_space.action():
                queue.append(
                    Node(
                        current_node.state_space.result(action),
                        [*current_node.path, action],
                    )
                )