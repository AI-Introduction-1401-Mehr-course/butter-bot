from butter_bot import (
    ButterBotStateSpace,
    state_space_from_io,
    print_path,
    alpha,
    beta,
    gamma,
    delta,
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

for h in (alpha, beta, gamma, delta):
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
