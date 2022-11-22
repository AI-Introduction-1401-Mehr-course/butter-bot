from enum import Enum
from safe_typing import Dict, List, NamedTuple, Tuple, Self
from state_space import StateSpace
from functools import partial

Cell = Tuple[int, int]


class ButterBotStateSpace(StateSpace):
    class ButterBotState(NamedTuple):
        columns: int
        rows: int
        cost_table: List[List[int]]
        bot_cell: Cell
        butter_cells: List[Cell]
        target_cells: List[Cell]
        blocked_cells: List[Cell]

    state: ButterBotState

    def __init__(self, state_dict: Dict):
        self.state = self.ButterBotState(**state_dict)

    class Action(Enum):
        value: Cell

        GO_UP = (-1, 0)
        GO_LEFT = (0, -1)
        GO_DOWN = (1, 0)
        GO_RIGHT = (0, 1)

    def _is_valid(self) -> bool:
        state = self.state

        cells = (state.bot_cell, *state.butter_cells)

        for cell in cells:
            if not (
                0 <= cell[0] < self.state.columns and 0 <= cell[1] < self.state.rows
            ):
                return False
            if cell in self.state.blocked_cells:
                return False
            if cells.count(cell) > 1:
                return False

        return True

    def result(self, action: Action) -> Self:
        new_bot_cell = tuple(i + j for i, j in zip(self.state.bot_cell, action.value))
        new_butter_cells = self.state.butter_cells

        if new_bot_cell in self.state.butter_cells:
            moved_butter_cell = tuple(i + j for i, j in zip(new_bot_cell, action.value))
            butter_cell_index = self.state.butter_cells.index(new_bot_cell)
            new_butter_cells = [
                *self.state.butter_cells[:butter_cell_index],
                moved_butter_cell,
                *self.state.butter_cells[butter_cell_index + 1 :],
            ]

        return ButterBotStateSpace(
            {
                **self.state._asdict(),
                "bot_cell": new_bot_cell,
                "butter_cells": new_butter_cells,
            }
        )

    def action(self) -> List[Action]:
        return list(action for action in self.Action if self.result(action)._is_valid())

    def cost(self, action: Action) -> int:
        new_bot_cell = tuple(i + j for i, j in zip(self.state.bot_cell, action.value))
        return self.state.cost_table[new_bot_cell[0]][new_bot_cell[1]]

    def is_goal(self) -> bool:
        return all(
            target_cell in self.state.butter_cells
            for target_cell in self.state.target_cells
        )

    def heuristic(self) -> int:
        def distance(cell_A, cell_B):
            return abs(cell_A[0] - cell_B[0]) + abs(cell_A[1] - cell_B[1])

        bot_cell = self.state.bot_cell
        butter_cells = [
            cell
            for cell in self.state.butter_cells
            if cell not in self.state.target_cells
        ]
        target_cells = [
            cell
            for cell in self.state.target_cells
            if cell not in self.state.butter_cells
        ]
        if not target_cells:
            return 0
        if not butter_cells:
            return float("inf")
        nearest_butter = min(butter_cells, key=partial(distance, bot_cell))
        nearest_target = min(target_cells, key=partial(distance, nearest_butter))
        return distance(bot_cell, nearest_butter) + distance(
            nearest_butter, nearest_target
        )
