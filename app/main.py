rows = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
positional_values = ['*', '1', '2', '3', '4', '5', '6', '7', '8', '9']
game_status = True


def board(values):
    print('|'.join(values[1:4]))
    print('-----')
    print('|'.join(values[4:7]))
    print('-----')
    print('|'.join(values[7:10]))


def players_choice():
    while True:
        position = input('Insert the position (1-9):  ')
        if position.isdigit() and int(position) in range(1, 10):
            break
        else:
            print('Invalid value for position! Please select a value between 1 and 9')
    return int(position)


def insert_choice(player_symbol, game_board):
    while True:
        choice = players_choice()
        if game_board[choice] == ' ':
            game_board[choice] = player_symbol
            break
        else:
            print('That box is already filled! Please place your symbol in an empty one.')


def check_win(player_symbol, game_board):
    if game_board[1:4] == [player_symbol, player_symbol, player_symbol]:
        return 'win'
    elif game_board[4:7] == [player_symbol, player_symbol, player_symbol]:
        return 'win'
    elif game_board[7:10] == [player_symbol, player_symbol, player_symbol]:
        return 'win'
    elif game_board[1] == player_symbol and game_board[4] == player_symbol and game_board[7] == player_symbol:
        return 'win'
    elif game_board[2] == player_symbol and game_board[5] == player_symbol and game_board[8] == player_symbol:
        return 'win'
    elif game_board[3] == player_symbol and game_board[6] == player_symbol and game_board[9] == player_symbol:
        return 'win'
    elif game_board[1] == player_symbol and game_board[5] == player_symbol and game_board[9] == player_symbol:
        return 'win'
    elif game_board[3] == player_symbol and game_board[5] == player_symbol and game_board[7] == player_symbol:
        return 'win'
    elif " " not in game_board:
        return 'draw'


def starting_menu():
    print('Welcome to the Tic Tac Toe game!\n')
    print(
        '''Each Player will insert a number that is attached to certain area of the TicTacToe board. 
        The positional numbers are 1-9 and they are configured like this: ''')
    board(positional_values)


def reset_game():
    global rows
    rows = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def ask_replay():
    global game_status
    while True:
        response = input('Do you want to play again? (yes/no) ')
        if response.lower() == 'yes':
            reset_game()
            break
        elif response.lower() == 'no':
            game_status = False
            break
        else:
            print('Invalid answer! Please use yes or no.')


def show_result(player):
    if check_win(player, rows) == 'win':
        board(rows)
        print('\n------Congratulations! Player 1 Won! :) --------')
        return True
    elif check_win(player, rows) == 'draw':
        board(rows)
        print('\n-----------Its a draw!-----------')
        return True
    else:
        return False


if __name__ == '__main__':
    starting_menu()
    while game_status:
        d = {'Player1': 'X', 'Player2': 'O'}
        print('\n--------------------------')
        board(rows)
        print('\nPlayer 1 turn: ')
        insert_choice(d['Player1'], rows)
        if show_result(d['Player1']):
            ask_replay()
            continue
        board(rows)
        print('\nPlayer 2 turn: ')
        insert_choice(d['Player2'], rows)
        if show_result(d['Player2']):
            ask_replay()
            continue
    print('\nThank you for playing! Have a nice day!')
