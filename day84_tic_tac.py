def create_board():
    c = [[" " for _ in range(3)] for _ in range(3)] # Nested list with list of three empty string
    for num,i in enumerate(c):
        print("|".join(i)) # Join each list with | where there is comma(,) in list
        if num < 2: # after 2 iteration means a new list started and create line before that list
            print('--'*5)

    return c


# Check if moves is valid and empty
def check_moves(board,row,col):
    '''
    :param board:
    :param row:
    :param col:
    :return: check if row and col are in range and also check in that range is that clear?
    '''
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

# board = create_board()
# board[0][1] = 'X'
# print(board)
# print(check_moves(board, 0, 2))


# if move is clear and good than make the mark there

def make_move(board, row, col, player):
    # check if move good ?
    if check_moves(board, row, col):
        board[row][col] = player # Mark the move
        return True # Return true after the mark
    return False

# Check the board with many win conditions if these conditions have no " " it means current player has won

def is_winner(board):
    '''

    :param board: Take Board only
    :return: check if board in win condtions
    '''

    win_conditions = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]],
        ]

    for condition in win_conditions:
        if condition[0] == condition[1] == condition[2] != ' ':
            return True
    return False


def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True



def play_game():

    board = create_board()

    current_player = 'X'

    while True:
        print(board)
        print(f"It is Turn of {current_player}")

        try:
            row = int(input('Enter Row within range of 0 to 2 '))
            col = int(input('Enter Column within range of 0 to 2 '))
        except ValueError:
            print('Invalid Input.. Try again')
            continue
    #not make_move(...): This checks if make_move(...) returns False. In other words,
        # it checks if the move was not successful (i.e., the move was invalid).
        if make_move(board, row, col, current_player):
            print('Good Move')
        else:
            print('Invalid Move! Try again')



        winner = is_winner(board)

        if winner:
            print(board)
            print(f'{current_player} has won!')
            break

        if is_draw(board):
            print(board)
            print('''It's a draw ''')
            break

        current_player = 'O' if current_player == 'X' else 'X'




play_game()
