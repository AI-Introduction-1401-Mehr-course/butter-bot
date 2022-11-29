from butter_bot import (
    ButterBotStateSpace,
    state_space_from_io,
    print_path,
    number_of_butters_not_on_a_target,
    number_of_targets_with_no_butter,
    sum_of_min_cost_of_filling_target_cells_with_butter,
    min_of_total_cost_of_filling_target_cells_with_butter,
    bot_to_nearest_butter_to_nearest_target_distance_heuristic,
    bot_to_nearest_butter_that_is_nearest_to_target_to_nearest_target_heuristic,
    min_cost_of_reaching_any_butter,
)
from safe_typing import Callable
from search import BestFirstSearch
from datetime import timedelta, datetime

run_time_limit = timedelta(seconds=1)


class RunTimeLimitExceeded(Exception):
    pass


def count_wrapper(method: Callable):
    def new_func(self, *args, **kwargs):
        if datetime.now() - new_func.start_time > run_time_limit:
            raise RunTimeLimitExceeded
        new_func.explored_node_counter += 1
        return method(self, *args, **kwargs)

    return new_func


ButterBotStateSpace.is_goal = count_wrapper(ButterBotStateSpace.is_goal)

state_space = state_space_from_io(
    open(input())
)  # TODO: Replace with a procedural problem generator

for h in (
    number_of_targets_with_no_butter,
    number_of_butters_not_on_a_target,
    sum_of_min_cost_of_filling_target_cells_with_butter,
    min_of_total_cost_of_filling_target_cells_with_butter,
    bot_to_nearest_butter_to_nearest_target_distance_heuristic,
    bot_to_nearest_butter_that_is_nearest_to_target_to_nearest_target_heuristic,
    min_cost_of_reaching_any_butter,
    lambda x: min_cost_of_reaching_any_butter(x)
    + min_of_total_cost_of_filling_target_cells_with_butter(x),
):
    ButterBotStateSpace.is_goal.explored_node_counter = 0
    ButterBotStateSpace.is_goal.start_time = datetime.now()
    try:
        path = BestFirstSearch(h)(state_space)
        # print_path(state_space, path)
        print(
            "astar returned with "
            + str(
                (datetime.now() - ButterBotStateSpace.is_goal.start_time).microseconds
            )
            + "\tmicroseconds run time and "
            + str(ButterBotStateSpace.is_goal.explored_node_counter)
            + "\tnodes explored for "
            + h.__name__
            + "heuristic function."
        )
    except RunTimeLimitExceeded:
        print(f"{h.__name__} didn't finish in {run_time_limit.seconds} seconds.")
