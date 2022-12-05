from sys import stdin

from butter_bot import alpha
from butter_bot import print_path, state_space_from_io
from search import AStar, BestFirstSearch, BFSearch, DFSearch, IDSearch, UCSearch

state_space = state_space_from_io(stdin)


bfs = BFSearch()
# print(bfs(state_space))


dfs = DFSearch()
# print(dfs(state_space))


ids = IDSearch()
# print(ids(state_space))


ucs = UCSearch()
# print(ucs(state_space))


astar = AStar(alpha)
# print(astar(state_space))


best_first_search = BestFirstSearch(alpha)
print_path(state_space, best_first_search(state_space))
