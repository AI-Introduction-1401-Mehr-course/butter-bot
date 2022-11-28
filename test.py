from butter_bot import (
    ButterBotStateSpace,
    state_space_from_io,
    print_path,
    number_of_targets_with_no_butter,
    sum_of_min_cost_of_filling_target_cells_with_butter,
    bot_to_nearest_butter_to_nearest_target_distance_heuristic,
    bot_to_nearest_butter_that_is_nearest_to_target_to_nearest_target_heuristic,
)
from safe_typing import Callable
from search import AStar


def count_wrapper(method: Callable):
    def new_func(self, *args, **kwargs):
        new_func.explored_node_counter += 1
        return method(self, *args, **kwargs)

    return new_func


ButterBotStateSpace.is_goal = count_wrapper(ButterBotStateSpace.is_goal)

state_space = state_space_from_io(
    open(input())
)  # TODO: Replace with a procedural problem generator

for h in (
    # number_of_targets_with_no_butter,
    sum_of_min_cost_of_filling_target_cells_with_butter,
    bot_to_nearest_butter_to_nearest_target_distance_heuristic,
    bot_to_nearest_butter_that_is_nearest_to_target_to_nearest_target_heuristic,
):
    ButterBotStateSpace.is_goal.explored_node_counter = 0
    print_path(state_space, AStar(h)(state_space))
    print(ButterBotStateSpace.is_goal.explored_node_counter)
