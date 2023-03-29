import numpy as np

# Define some global variables
blank = 0
wall = 1
box = 2
keeper = 3
star = 4
boxstar = 5
keeperstar = 6


# Some helper functions for checking the content of a square
def isBlank(v):
    return (v == blank)

def isWall(v):
    return (v == wall)

def isBox(v):
    return (v == box)

def isKeeper(v):
    return (v == keeper)

def isStar(v):
    return (v == star)

def isBoxstar(v):
    return (v == boxstar)

def isKeeperstar(v):
    return (v == keeperstar)

# Help function for get KeeperPosition
# Given state s (numpy array), return the position of the keeper by row, col
# The top row is the zeroth row
# The first (right) column is the zeroth column
def getKeeperPosition(s):
    row = s.shape[0]
    col = s.shape[1]
    for i in range(row):
        for j in range(col):
            if (isKeeper(s[i, j]) or isKeeperstar(s[i, j])):
                return i, j


# For input list s_list, remove all None element
# For example, if s_list = [1, 2, None, 3], returns [1, 2, 3]
def cleanUpList(s_list):
    clean = []
    for state in s_list:
        if state is not None:
            clean.append(state)
    return clean

# goal_test takes a single argument state representing the game state.
# Return True if that state is a goal test where there is no boxes left.
# Check if there is a box in that state, return true if there is none.
# Return False otherwise.

def goal_test(s):

    row, col = s.shape[0], s.shape[1]  # Get rows and cols fro the state

    # Check every single box associated with (r,c) if there is a box left, return false
    for r in range(row):
        for c in range(col):
            if isBox(s[r, c]):
                return False
    return True  # no more boxes left on the board

# next_states takes an argument s as the current state
# it returns a list of all reachable state from the current state with each direction move from try_move
def next_states(s):

    s_list = []
    s1 = np.copy(s)

    s_list = [try_move(s1, 'UP'), try_move(s1, 'DOWN'),
              try_move(s1, 'LEFT'), try_move(s1, 'RIGHT')]

    return cleanUpList(s_list)

# get_square takes 3 args state, row, col and return the integer content of the square at state of (r,c)
# If the square is outside of the scope, return value of a wall
def get_square(state, row, col):

    return state[row, col] if row < state.shape[0] and col < state.shape[1] else wall

# set_square takes 4 args, state, row, col, and a square content as int v.
# set_quare returns a new state value by setting its state to the square content value
def set_square(state, row, col, square_content_int_v):

    # Make a copy of the state to a new state
    new_state = np.copy(state)

    # Set the content v to state square position
    new_state[row, col] = square_content_int_v

    return new_state

# ------- CHECK INVALID MOVE -----------
# invalid_move_up takes in 3 args, state, row, and col
# it returns False if the keeper can move up with one or two step aways from its row  and return True otherwise
def invalid_move_up(state, row, col):

    next_row = row - 1

    future_row = row - 2

    # check if the current row is 0 and the next row is wall -> return invalid
    if row == 0 or state[next_row, col] == wall:
        return True

    # if the current row is 1 and the next row is not star or not blank -> return invalid
    elif row == 1:
        if state[next_row, col] != star and state[next_row, col] != blank:
            return True
    # if the next row is box or boxstar and the future_row (which is two row away) is not blank and not star --> return invalid
    elif row >= 2:
        if (state[next_row, col] == box or state[next_row, col] == boxstar) and (state[future_row, col] != blank and state[future_row, col] != star):
            return True

    # Otherwise return False
    return False

# invalid_move_down takes in 3 args, state, row, and col
# it returns False if the keeper can move down with one or two step aways from its row and return True otherwise
def invalid_move_down(state, row, col):

    next_row = row + 1

    future_row = row + 2

    board_row = state.shape[0]

    # check if the current row is the board row - 1 and the next row is wall -> return invalid
    if row == board_row - 1 or state[next_row, col] == wall:
        return True

    # Check if the current row is the board row - 2 and the next row is not star or not blank -> return invalid
    elif row == board_row - 2:
        if state[next_row, col] != star and state[next_row, col] != blank:
            return True

    # Check if the next row is box or boxstar and the future_row (which is two row away) is not blank and not star --> return invalid
    elif row <= board_row - 3:
        if (state[next_row, col] == box or state[next_row, col] == boxstar) and (state[future_row, col] != blank and state[future_row, col] != star):
            return True

    # Otherwise return False
    return False

# invalid_move_left takes in 3 args, state, row, and col
# it returns False if the keeper can move left with one or two cols aways from its row  and return True otherwise
def invalid_move_left(state, row, col):

    next_col = col - 1

    future_col = col - 2

    # Check if the col is 0 and the next col is wall -> return invalid
    if col == 0 or state[row, next_col] == wall:
        return True

    # Check if the col is 1 and the next col is not star or blank -> return invalid
    elif col == 1:
        if state[row, next_col] != star and state[row, next_col] != blank:
            return True
    # Check if the next col is box or boxstar and the future col (two cols away) is not blank or star -> return invalid
    elif col >= 2:
        if (state[row, next_col] == box or state[row, next_col] == boxstar) and (state[row, future_col] != blank and state[row, future_col] != star):
            return True

    return False

# invalid_move_right takes in 3 args, state, row, and col
# it returns False if the keeper can move right with one or two cols aways from its row  and return True otherwise
def invalid_move_right(state, row, col):

    next_col = col + 1

    future_col = col + 2

    board_col = state.shape[1]

    # Check if the col is the boarder col -1 or next col is wall -> return invalid
    if col == board_col - 1 or state[row, next_col] == wall:
        return True

    # Check if the col is the boarder col - 2 and the next col is not star and blank -> return invalid
    elif col == board_col - 2:
        if state[row, next_col] != star and state[row, next_col] != blank:
            return True

    # Check if the col is the boarder col -3 and next col is box or boxstar and the future cols not blank or star -> return invalid
    elif col <= board_col - 3:
        if (state[row, next_col] == box or state[row, next_col] == boxstar) and (state[row, future_col] != blank and state[row, future_col] != star):
            return True

    return False

# --------------- Move Vertically 'UP' OR 'DOWN' -----------------
# updated_keeper_next_move takes in 5 args, state, row, col, next_move, direction
# direction in here is whether the keeper is going 'UP' or 'DOWN'
# it will check if the next move is blank, is star, is box, and is boxstar
# it will update the state accordingly throughout each condition.


def updated_keeper_next_move(state, row, col, next_move, direction):

    if isBlank(next_move):
        # Update keeper and blank
        update_state = update_keeper_star_blank_star(
            state, row, col, keeper, blank, direction)

    elif isStar(next_move):
        # Update keeper star with blank
        update_state = update_keeper_star_blank_star(
            state, row, col, keeperstar, blank, direction)

    elif isBox(next_move):
        # update kepper blank
        update_state = update_keeper_box(
            state, row, col, keeper, blank, direction)

    elif isBoxstar(next_move):
        # update keeper star with balnk
        update_state = update_keeper_box(
            state, row, col, keeperstar, blank, direction)

    return update_state

# updated_keeper_star_next_move takes in 5 args, state, row, col, next_move, direction
# direction in here is whether the keeper is going 'UP' or 'DOWN'
# it will check if the next move is blank, is star, is box, and is boxstar
# it will update the state accordingly throughout each condition.


def updated_keeper_star_next_move(state, row, col, next_move, direction):

    if isBlank(next_move):
        # Update keeper and star
        update_state = update_keeper_star_blank_star(
            state, row, col, keeper, star, direction)

    elif isStar(next_move):
        # Update keeperstar and star
        update_state = update_keeper_star_blank_star(
            state, row, col, keeperstar, star, direction)

    elif isBox(next_move):
        # Update keeper and star
        update_state = update_keeper_box(
            state, row, col, keeper, star, direction)

    elif isBoxstar(next_move):
        # Update keeperstar and star
        update_state = update_keeper_box(
            state, row, col, keeperstar, star, direction)

    return update_state

# update_keeper_star_blank_star takes in 6 args, state, row, col, keeper position, square value, and direction
# direction in here is whether the keeper is going 'UP' or 'DOWN' so that the row is updated accordingly
# it will update the square accordingly throughout each condition.
def update_keeper_star_blank_star(state, row, col, keeper_position, square_value, direction):

    if direction == 'UP':
        update_row = row - 1

    elif direction == 'DOWN':
        update_row = row + 1

    update_keeper = set_square(state, update_row, col, keeper_position)

    return set_square(update_keeper, row, col, square_value)

# update_keeper_box is a helper function to update the box with the keeper position
# it takes 6 args, state, row, col, keeper position, square values, and direction
# it returns the update keeper star or blank star based on the keeper position values, square values, and the direction
def update_keeper_box(state, row, col, keeper_position, square_values, direction):

    if direction == 'UP':
        two_step_away = row - 2

    elif direction == 'DOWN':
        two_step_away = row + 2

    two_step_away_state = None

    if isBlank(state[two_step_away, col]):

        two_step_away_state = set_square(state, two_step_away, col, box)

    elif isStar(state[two_step_away, col]):

        two_step_away_state = set_square(state, two_step_away, col, boxstar)

    return update_keeper_star_blank_star(two_step_away_state, row, col, keeper_position, square_values, direction)

# --------------- Move Horizontally 'LEFT' OR 'RIGHT' -----------------
# updated_keeper_horizontal_next_move takes in 5 args, state, row, col, next move, and direction
# it will check if the next move is blank, is star, is box, or is box star
# and it returns the updated state accordingly with the keeper
def updated_keeper_horizontal_next_move(state, row, col, next_move, direction):

    if isBlank(next_move):
        # Update keeper and blank
        update_state = update_horizontal_move_keeper_star_blank_star(
            state, row, col, keeper, blank, direction)

    elif isStar(next_move):
        # Update keeper star and blank
        update_state = update_horizontal_move_keeper_star_blank_star(
            state, row, col, keeperstar, blank, direction)

    elif isBox(next_move):
        # update keeper and blank
        update_state = update_keeper_box_horizontally(
            state, row, col, keeper, blank, direction)

    elif isBoxstar(next_move):
        # update keeperstar and blank
        update_state = update_keeper_box_horizontally(
            state, row, col, keeperstar, blank, direction)

    return update_state

# updated_keeper_star_horizontal_next_move takes in 5 args, state, row, col, next move, direction
# it will check if the next move is blank, is star, is box, or is box star
# and it returns the updated state accordingly with the keeper star
def updated_keeper_star_horizontal_next_move(state, row, col, next_move, direction):

    if isBlank(next_move):
        # Update keeper and blank
        update_state = update_horizontal_move_keeper_star_blank_star(
            state, row, col, keeper, star, direction)

    elif isStar(next_move):

        update_state = update_horizontal_move_keeper_star_blank_star(
            state, row, col, keeperstar, star, direction)

    elif isBox(next_move):

        update_state = update_keeper_box_horizontally(
            state, row, col, keeper, star, direction)

    elif isBoxstar(next_move):

        update_state = update_keeper_box_horizontally(
            state, row, col, keeperstar, star, direction)

    return update_state

# update_horizontal_move_keeper_star_blank_star takes in 6 args, state, row, col, keeper position, square value, and direction
# it returns the square values with the updated from keeper position, and square values.
def update_horizontal_move_keeper_star_blank_star(state, row, col, keeper_position, square_value, direction):

    if direction == 'LEFT':
        update_col = col - 1

    elif direction == 'RIGHT':
        update_col = col + 1

    update_keeper = set_square(state, row, update_col, keeper_position)

    return set_square(update_keeper, row, col, square_value)

# update_keeper_box_horizontally is a helper function to update the box with the keeper position
# it takes 6 args, state, row, col, keeper position, square values, and direction
# it returns the update keeper star or blank star based on the keeper position values, square values, and the direction
def update_keeper_box_horizontally(state, row, col, keeper_position, square_values, direction):

    if direction == 'LEFT':
        two_step_away = col - 2

    elif direction == 'RIGHT':
        two_step_away = col + 2

    two_step_away_state = None

    if isBlank(state[row, two_step_away]):

        two_step_away_state = set_square(state, row, two_step_away, box)

    elif isStar(state[row, two_step_away]):

        two_step_away_state = set_square(state, row, two_step_away, boxstar)

    return update_horizontal_move_keeper_star_blank_star(two_step_away_state, row, col, keeper_position, square_values, direction)

# updated_keeper_vertically takes in 6 args
# it returns keeper next move or keeper star next move based on the current move
def updated_keeper_vertically(state, row, col, current_move, next_move, direction):

    # the current move is Keeper
    if isKeeper(current_move):
        return updated_keeper_next_move(state, row, col, next_move, direction)

    # the current move is Keeperstar
    elif isKeeperstar(current_move):
        return updated_keeper_star_next_move(state, row, col, next_move, direction)

# updated_keeper_horizontally takes in 6 args
# it returns keeper next move or keeper star next move based on the current move


def updated_keeper_horizontally(state, row, col, current_move, next_move, direction):

    # the current move is Keeper
    if isKeeper(current_move):
        return updated_keeper_horizontal_next_move(state, row, col, next_move, direction)

    # the current move is Keeperstar
    elif isKeeperstar(current_move):
        return updated_keeper_star_horizontal_next_move(state, row, col, next_move, direction)

# try_move takes in 2 args, state and direction
# it returns None if the direction has invalid move
# otherwise, return the updated keeper accordingly to the direction


def try_move(s, d):
    row, col = getKeeperPosition(s)

    directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

    dr = [-1, 1, 0, 0]      # direction row is [up, down, 0, 0]
    dc = [0, 0, -1, 1]     # direction col is [0, 0, left, right]

    direction = directions.index(d)  # get index of direction

    next_row, next_col = row + dr[direction], col + dc[direction]

    current_move, next_move = get_square(
        s, row, col), get_square(s, next_row, next_col)

    # Up -> Row - 1
    if d == "UP":
        if invalid_move_up(s, row, col):
            return None
        else:
           return updated_keeper_vertically(s, row, col, current_move, next_move, d)

    # Down -> Row + 1
    elif d == "DOWN":
        if invalid_move_down(s, row, col):
            return None
        else:
            return updated_keeper_vertically(s, row, col, current_move, next_move, d)

    # Left -> Col - 1
    elif d == "LEFT":
        if invalid_move_left(s, row, col):
            return None

        else:
            return updated_keeper_horizontally(s, row, col, current_move, next_move, d)

    # Right -> Col + 2
    elif d == "RIGHT":
        if invalid_move_right(s, row, col):
            return None
        else:
            return updated_keeper_horizontally(s, row, col, current_move, next_move, d)
