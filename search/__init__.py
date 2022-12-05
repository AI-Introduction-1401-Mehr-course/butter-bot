from .a_star import AStar
from .best_first_search import BestFirstSearch
from .bfs import BFSearch
from .dfs import DFSearch
from .ids import IDSearch
from .ucs import UCSearch

search_algorithms_dict = {
    "a_star": AStar,
    "best_first_search": BestFirstSearch,
    "bfs": BFSearch,
    "dfs": DFSearch,
    "ids": IDSearch,
    "ucs": UCSearch,
}
