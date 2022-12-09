import argparse
import multiprocessing
from sys import stdin

from search import search_algorithms_dict
from butter_bot import heuristic_functions_dict, state_space_from_io, print_path
from abstracts import InformedSearch

parser = argparse.ArgumentParser()

parser.add_argument(
    "-i",
    "--input-file",
    required=False,
    type=argparse.FileType(),
    help="read from file instead of stdin",
)

parser.add_argument(
    "-s",
    "--search-algorithm",
    default="best_first_search",
    type=lambda x: search_algorithms_dict[x],
    help="algorithm for executing search\noptions:\n( "
    + " | ".join(key for key in search_algorithms_dict.keys())
    + " )",
)

parser.add_argument(
    "-e",
    "--heuristic-function",
    default="alpha",
    type=lambda x: heuristic_functions_dict[x],
    help="heuristic for informed searchs\noptions:\n( "
    + " | ".join(key for key in heuristic_functions_dict.keys())
    + " )",
)

parser.add_argument(
    "-t",
    "--timeout",
    default=3,
    type=int,
    help="time limit of search execution",
)


def execute(state_space):
    args = parser.parse_args()
    search = (
        args.search_algorithm(args.heuristic_function)
        if issubclass(args.search_algorithm, InformedSearch)
        else args.search_algorithm()
    )

    print_path(state_space, search(state_space))


if __name__ == "__main__":
    search_process = multiprocessing.Process(
        target=execute,
        args=[state_space_from_io(parser.parse_args().input_file or stdin)],
    )
    search_process.start()
    search_process.join(parser.parse_args().timeout)
    if search_process.is_alive():
        print("Search execution timed out.")
        search_process.terminate()
        search_process.join()
