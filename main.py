from sys import stdin
from safe_typing import List
from re import sub
from butter_bot import Cell, ButterBotStateSpace
from search import (
    BFSearch,
    DFSearch,
    IDSearch,
    UCSearch,
    AStar,
    BestFirstSearch,
)

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


bfs = BFSearch()
# print(bfs(state_space))


dfs = DFSearch()
# print(dfs(state_space))


ids = IDSearch()
# print(ids(state_space))


ucs = UCSearch()
# print(ucs(state_space))


astar = AStar()
# print(astar(state_space))


best_first_search = BestFirstSearch()
print(best_first_search(state_space))
