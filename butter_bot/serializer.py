from re import sub

from abstracts import StateSpace
from butter_bot import ButterBotStateSpace
from safe_typing import IO, Cell, List

from .butter_bot_state_space import ButterBotStateSpace


def state_space_from_io(io: IO):

    columns, rows = (int(i) for i in next(io).split())

    cells = [next(io).split() for _ in range(columns)]

    cost_table: List[List[int]] = [
        [
            int(sub(r"\D", "", cells[i][j])) if cells[i][j] != "x" else -1
            for j in range(rows)
        ]
        for i in range(columns)
    ]

    butter_cells: List[Cell] = []
    target_cells: List[Cell] = []
    blocked_cells: List[Cell] = []
    bot_cell: Cell = (0, 0)

    for i in range(columns):
        for j in range(rows):
            for symbol, cell_list in {
                "b": butter_cells,
                "p": target_cells,
                "x": blocked_cells,
            }.items():
                if cells[i][j].count(symbol):
                    cell_list.append((i, j))
            if cells[i][j].count("r"):
                bot_cell = (i, j)

    return ButterBotStateSpace(
        {
            "columns": columns,
            "rows": rows,
            "cost_table": cost_table,
            "bot_cell": bot_cell,
            "butter_cells": butter_cells,
            "target_cells": target_cells,
            "blocked_cells": blocked_cells,
        }
    )


def print_path(root: StateSpace, path: List[StateSpace.Action] | None):
    if isinstance(path, type(None)):
        return print("can't pass the butter")

    cost, state_hodler = 0, root
    for action in path:
        cost += state_hodler.cost(action)
        state_hodler = state_hodler.result(action)

    print(" ".join(action.name[3] for action in path))
    print(cost)
    print(len(path))
