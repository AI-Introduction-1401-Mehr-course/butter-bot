from sys import stdin
from typing import List
from re import sub

from butter_bot import Cell, ButterBotStateSpace

columns, rows = (int(i) for i in next(stdin).split())

cells = [next(stdin).split() for _ in range(columns)]

cost_table: List[List[int]] = [
    [int(sub(r"\D", "", cells[i][j])) if cells[i][j] != "x" else 0 for j in range(rows)]
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


state_space = ButterBotStateSpace(
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

from bfs import BFSearch

bfs = BFSearch()
# print(bfs(state_space))

from dfs import DFSearch

dfs = DFSearch()
# print(dfs(state_space))

from ids import IDSearch

ids = IDSearch()
# print(ids(state_space))

from ucs import UCSearch
ucs = UCSearch()
print(ucs(state_space))

