from functools import partial
from itertools import filterfalse, permutations
from math import inf

from .butter_bot_state_space import ButterBotStateSpace
from safe_typing import Cell, List


def distance(cell_A: Cell, cell_B: Cell) -> int:
    """
    Returns distance between two cells.
    """

    return abs(cell_A[0] - cell_B[0]) + abs(cell_A[1] - cell_B[1])


def min_cost_from_cell_matrix(
    cell: Cell, cost_table: List[List[int]]
) -> List[List[int]]:
    """
    Returns matrix of minimum cost requierd to reach any cell starting from `cell`.
    """

    ans: List[List[int]] = [[-1 for _ in i] for i in cost_table]
    queue = [cell]
    ans[cell[0]][cell[1]] = 0

    while queue:
        current_cell = queue.pop(0)
        for new_cell in (
            (current_cell[0] + i.value[0], current_cell[1] + i.value[1])
            for i in ButterBotStateSpace.Action
        ):
            if (
                0 <= new_cell[0] < len(ans)
                and 0 <= new_cell[1] < len(ans[0])
                and cost_table[new_cell[0]][new_cell[1]] != -1
                and (
                    ans[new_cell[0]][new_cell[1]] == -1
                    or (
                        ans[new_cell[0]][new_cell[1]]
                        > ans[current_cell[0]][current_cell[1]]
                        + cost_table[new_cell[0]][new_cell[1]]
                    )
                )
            ):
                ans[new_cell[0]][new_cell[1]] = (
                    ans[current_cell[0]][current_cell[1]]
                    + cost_table[new_cell[0]][new_cell[1]]
                )
                queue.append(new_cell)

    return ans


def bot_to_nearest_butter_that_is_nearest_to_target_to_nearest_target_heuristic(
    state_space: ButterBotStateSpace,
) -> float:
    """
    Returns distance from current state to goal
    by calculating distance from bot to nearest butter that is nearest to a target plus distance from that butter to nearest target.
    """
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
        return inf

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
    """
    Returns distance from current state to goal
    by calculating distance from bot to nearest butter plus distance from that butter to nearest point.
    """
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
        return inf
    nearest_butter = min(butter_cells, key=partial(distance, bot_cell))
    nearest_target = min(target_cells, key=partial(distance, nearest_butter))
    return distance(bot_cell, nearest_butter) + distance(nearest_butter, nearest_target)


def number_of_butters_not_on_a_target(
    state_space: ButterBotStateSpace,
) -> float:
    """
    Returns distance from current state to goal
    by calculating number of remaining butters that have not reached a target.
    """
    state = state_space.state
    butter_cells = [
        cell for cell in state.butter_cells if cell not in state.target_cells
    ]
    return len(butter_cells)


def number_of_targets_with_no_butter(state_space: ButterBotStateSpace) -> float:

    state = state_space.state
    return sum(1 for cell in state.target_cells if cell not in state.butter_cells)


def min_cost_of_reaching_any_butter(state_space: ButterBotStateSpace) -> float:

    state = state_space.state

    min_cost_from_bot_matrix = min_cost_from_cell_matrix(
        state.bot_cell, state.cost_table
    )
    try:
        return min(
            min_cost_from_bot_matrix[i[0]][i[1]] - state.cost_table[i[0]][i[1]]
            for i in state.butter_cells
            if i not in state.target_cells
        )
    except ValueError:
        return 0


# Heuristics derived from relaxed versions of the problem:


def sum_of_min_cost_of_filling_target_cells_with_butter(
    state_space: ButterBotStateSpace,
) -> float:
    """
    Teleporting bot with ability of picking up butters.
    Also duplicating butters and walking through them and stuff...
    """

    state = state_space.state
    try:
        return sum(
            min(
                cost_matrix[butter_cell[0]][butter_cell[1]]
                for butter_cell in state.butter_cells
                if cost_matrix[butter_cell[0]][butter_cell[1]] != -1
            )
            for cost_matrix in (
                min_cost_from_cell_matrix(cell, state.cost_table)
                for cell in state.target_cells
                if cell not in state.butter_cells
            )
        )
    except ValueError:
        return inf


def min_of_total_cost_of_filling_target_cells_with_butter(
    state_space: ButterBotStateSpace,
) -> float:
    """
    Teleporting bot with ability of picking up butters.
    Also duplicating butters and walking through them and stuff...
    """

    state = state_space.state

    b_cells = [cell for cell in state.butter_cells if cell not in state.target_cells]
    t_cells = [cell for cell in state.target_cells if cell not in state.butter_cells]
    costs = [
        [cost_matrix[butter_cell[0]][butter_cell[1]] for butter_cell in b_cells]
        for cost_matrix in (
            min_cost_from_cell_matrix(target_cell, state.cost_table)
            for target_cell in t_cells
        )
    ]

    try:
        return min(
            sum(costs[i][j[i]] for i in range(len(t_cells)))
            for j in permutations(range(len(b_cells)), len(t_cells))
            if all(costs[i][j[i]] != -1 for i in range(len(t_cells)))
        )
    except ValueError:
        return inf
