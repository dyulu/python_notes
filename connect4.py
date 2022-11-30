#!/usr/bin/python3

# c4_data, a 2-D array, represents the connect-4 game board
#   0: the space is available
#   1: the space is occupied by play 1
#   2: the space is occupied by play 2
# The game board looks like the following When it is reset:
# Col  0  1  2  3  4  5  6
#     [0, 0, 0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0, 0, 0]
c4_rows, c4_cols = (6, 7)

# Reset game board
def c4_reset():
    global c4_data
    c4_data = [ [ 0 for col in range(c4_cols) ] for row in range(c4_rows) ]

# Visual representation of the game board
def c4_view():
    print("Current game board:")
    print("Col  0  1  2  3  4  5  6")
    for row in c4_data:
        print(f"    {row}")
    print()

# Ask player to make a move: the column with first row available is eligible
def c4_ask_for_move(player):
    eligible_cols = [col for col in range(c4_cols) if c4_data[0][col] == 0]
    # Game is over and is a draw if no more moves can be made
    if len(eligible_cols) == 0:
        return None

    while True:
        the_move = input(f"Player {player}, please make a move by selecting an eligible column from {eligible_cols}: ")

        # Make sure player entered a integer
        try:
            the_move = int(the_move)
        except:
            continue

        # Make sure player made a valid move
        if the_move in eligible_cols:
            break

    return the_move

# Place the move: player has made a valid move by selecting an eligible column; need to see which row it should
#                 end up with by looking at what space is occupied
def c4_place_the_move(player, the_move):
    # It is known that the first row is available
    row = 0
    next_row = row + 1
    # Move it down one row if next row is available until next row is occupied or no more rows
    while next_row < c4_rows and c4_data[next_row][the_move] == 0:
        row = next_row
        next_row = row + 1

    # Place the move by making it occupied by the player
    c4_data[row][the_move] = player

    # Return the current location (row, the_move)
    return row, the_move

# Determine whether a move is a winning move or not
def c4_is_win(player, row, col):
    return (is_downward_win(player, row, col) or
            is_horizontal_win(player, row, col) or
            is_left_diag_win(player, row, col) or
            is_right_diag_win(player, row, col))

def is_downward_win(player, row, col):
    # Count (row, col)
    count = 1

    # Count downward from (row, col)
    next_row = row + 1
    while next_row < c4_rows and c4_data[next_row][col] == player:
        count += 1
        next_row += 1

    return count >= 4
    
def is_horizontal_win(player, row, col):
    # Count (row, col)
    count = 1

    # Search horizontally to the left from (row, col)
    next_col = col - 1
    while next_col >= 0 and c4_data[row][next_col] == player:
        count += 1
        next_col -= 1

    # Search horizontally to the right from (row, col)
    next_col = col + 1
    while next_col < c4_cols and c4_data[row][next_col] == player:
        count += 1
        next_col += 1

    return count >= 4

def is_left_diag_win(player, row, col):
    # Count (row, col)
    count = 1

    # Search diagonally down-left from (row, col)
    next_row, next_col = (row + 1, col - 1)
    while next_row < c4_rows and next_col >= 0 and c4_data[next_row][next_col] == player:
        count += 1
        next_row, next_col = (next_row + 1, next_col - 1)

    # Search diagonally up-right from (row, col)
    next_row, next_col = (row - 1, col + 1)
    while next_row >= 0 and next_col < c4_cols and c4_data[next_row][next_col] == player:
        count += 1
        next_row, next_col = (next_row - 1, next_col + 1)

    return count >= 4

def is_right_diag_win(player, row, col):
    # Count (row, col)
    count = 1

    # Search diagonally down-right from (row, col)
    next_row, next_col = (row + 1, col + 1)
    while next_row < c4_rows and next_col < c4_cols and c4_data[next_row][next_col] == player:
        count += 1
        next_row, next_col = (next_row + 1, next_col + 1)

    # Search diagonally up-left from (row, col)
    next_row, next_col = (row - 1, col - 1)
    while next_row >= 0 and next_col >= 0 and c4_data[next_row][next_col] == player:
        count += 1
        next_row, next_col = (next_row - 1, next_col - 1)

    return count >= 4

# Ask plays whether they want to play again after game over
def c4_play_again():
    play_again = input("Do you want to play again [Y/N]? ")
    if play_again == "Y":
        c4_reset()
        return True

    return False


if __name__ == '__main__':
    c4_reset()
    c4_view()

    next_player = 1
    while True:
        the_move = c4_ask_for_move(next_player)
        if the_move is None:
            print("Game over: draw!")
            if not c4_play_again():
                break

        row, col = c4_place_the_move(next_player, the_move)
        c4_view()

        if c4_is_win(next_player, row, col):
            print(f"Game over: player {next_player} won!")
            if not c4_play_again():
                break

        if next_player == 1:
            next_player = 2
        else:
            next_player = 1
