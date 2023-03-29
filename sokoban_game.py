from board_game_setup import *

from helper_printing_game_state import *

from search_astar_algorithm import *

if __name__ == '__main__':
    state_2 = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 1, 0, 3, 0, 0, 0, 1],
                        [1, 0, 0, 2, 0, 2, 0, 0, 1],
                        [1, 0, 4, 1, 0, 1, 0, 0, 1],
                        [1, 0, 1, 0, 0, 0, 4, 0, 1],
                        [1, 0, 1, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1]
                        ])
    printstate(state_2)
