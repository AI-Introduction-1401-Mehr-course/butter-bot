from functools import partial

from .butter_bot_state_space import ButterBotStateSpace


def bot_to_nearest_butter_to_nearest_target_distance_heuristic(
    state_space: ButterBotStateSpace,
) -> float:

    state = state_space.state

    def distance(cell_A, cell_B) -> int:
        return abs(cell_A[0] - cell_B[0]) + abs(cell_A[1] - cell_B[1])

    bot_cell = state.bot_cell
    butter_cells = [
        cell for cell in state.butter_cells if cell not in state.target_cells
    ]
    target_cells = [
        cell for cell in state.target_cells if cell not in state.butter_cells
    ]
    if not target_cells:
        return 0
    if not butter_cells:
        return float("inf")
    nearest_butter = min(butter_cells, key=partial(distance, bot_cell))
    nearest_target = min(target_cells, key=partial(distance, nearest_butter))
    return distance(bot_cell, nearest_butter) + distance(nearest_butter, nearest_target)
