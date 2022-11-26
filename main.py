from sys import stdin

from butter_bot import (
    bot_to_nearest_butter_to_nearest_target_distance_heuristic as btnbtnt_distance_heuristic,
    bot_to_nearest_butter_that_is_nearest_to_target_to_nearest_target_heuristic as btnbtintttnt_distance_heuristic,
    number_of_butters_not_on_a_target as nobnot_heuristic,
)
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


astar = AStar(btnbtnt_distance_heuristic)
# print(astar(state_space))


best_first_search = BestFirstSearch(btnbtnt_distance_heuristic)
print_path(state_space, best_first_search(state_space))
