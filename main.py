from sys import stdin

from butter_bot import alpha, beta, gamma, delta
from butter_bot import print_path, state_space_from_io
from search import AStar, BestFirstSearch, BFSearch, DFSearch, IDSearch, UCSearch

state_space = state_space_from_io(stdin)


bfs = BFSearch()
# print_path(state_space, bfs(state_space))


dfs = DFSearch()
# print_path(state_space, dfs(state_space))


ids = IDSearch()
# print_path(state_space, ids(state_space))


ucs = UCSearch()
# print_path(state_space, ucs(state_space))


astar = AStar(beta)
# print_path(state_space, astar(state_space))


best_first_search = BestFirstSearch(beta)
# print_path(state_space, best_first_search(state_space))
