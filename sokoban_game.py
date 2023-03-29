from board_game_setup import *

from helper_printing_game_state import *

from search_astar_algorithm import *

from sokoban_heuristic_algorithm import *

if __name__ == '__main__':

    state19 = np.array([[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 4],
                        [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 2, 0, 4, 1, 0, 0, 0]])
    printstate(state19)
    sokoban(state19, heuristic_optimal_func)
