from safe_typing import List, NamedTuple, Tuple
from abstracts import InformedSearch, StateSpace
from bisect import insort


class BestFirstSearch(InformedSearch):
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
