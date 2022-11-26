from functools import partial

from .butter_bot_state_space import ButterBotStateSpace


def distance(cell_A, cell_B) -> int:
    return abs(cell_A[0] - cell_B[0]) + abs(cell_A[1] - cell_B[1])


def bot_to_nearest_butter_that_is_nearest_to_target_to_nearest_target_heuristic(
    state_space: ButterBotStateSpace,
) -> float:

    state = state_space.state

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

    nearest_butter = butter_cells[0]
    for butter_cell in butter_cells:
        if distance(butter_cell, bot_cell) < distance(nearest_butter, bot_cell):
            nearest_butter = butter_cell
        elif distance(butter_cell, bot_cell) == distance(nearest_butter, bot_cell):
            nearest_target_to_butter_cell = min(
                target_cells, key=partial(distance, butter_cell)
            )
            nearest_target_to_nearest_butter = min(
                target_cells, key=partial(distance, nearest_butter)
            )
            if distance(butter_cell, nearest_target_to_butter_cell) < distance(
                nearest_butter, nearest_target_to_nearest_butter
            ):
                nearest_butter = butter_cell

    nearest_target = min(target_cells, key=partial(distance, nearest_butter))
    return distance(bot_cell, nearest_butter) + distance(nearest_butter, nearest_target)


def bot_to_nearest_butter_to_nearest_target_distance_heuristic(
    state_space: ButterBotStateSpace,
) -> float:

    state = state_space.state

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

def number_of_butters_not_on_a_target(
    state_space: ButterBotStateSpace,
) -> float:

    state = state_space.state
    butter_cells = [
        cell for cell in state.butter_cells if cell not in state.target_cells
    ]
    return len(butter_cells)
