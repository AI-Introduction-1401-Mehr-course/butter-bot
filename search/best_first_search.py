from bisect import insort

from abstracts import InformedSearch, StateSpace
from safe_typing import List, NamedTuple, Tuple


class BestFirstSearch(InformedSearch):
    """
    Best-first search (Greedy) implementation.
    Expands nodes which are closest to the goal node and the closest cost is estimated by heuristic function.
    """
    def __call__(self, state_space: StateSpace) -> List[StateSpace.Action] | None:
        class Node(NamedTuple):
            state_space: StateSpace
            path: List[StateSpace.Action]

        list = [Node(state_space=state_space, path=[])]

        while list:
            current_node = list.pop(0)
            if current_node.state_space.is_goal():
                return current_node.path
            for action in current_node.state_space.action():
                insort(
                    list,
                    Node(
                        current_node.state_space.result(action),
                        [*current_node.path, action],
                    ),
                    key=lambda x: self.heuristic(x.state_space),
                )
