import builtins
import pytest

import app.main
from app.main import board
from app.main import players_choice, insert_choice, check_win, starting_menu
from unittest.mock import patch, MagicMock
from app.main import reset_game, rows
from app.main import ask_replay, game_status


@pytest.mark.parametrize('values, expected', [
    (['*', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'], "X|O|X\n-----\nO|X|O\n-----\nX|O|X\n")
])
def test_board(values, expected, capfd):
    board(values)
    output = capfd.readouterr()
    assert output.out == expected


def test_players_choice_valid():
    with patch('builtins.input', side_effect=['7']):
        res = players_choice()
    assert res == 7


def test_players_choice_invalid_and_last_valid():
    with patch('builtins.input', side_effect=['0', '15', '100', 'Six', '7']):
        res = players_choice()
    assert res == 7


@pytest.mark.parametrize('rows, player_symbol, number', [
    (['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 'X', 5),
    (['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 'O', 7)
])
def test_insert_choice_valid(rows, player_symbol, number):
    # rows = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # player_symbol = 'X'
    mock_players_choice = MagicMock(return_value=number)
    with patch('app.main.players_choice', mock_players_choice):
        insert_choice(player_symbol, rows)
    assert rows[number] == player_symbol


@pytest.mark.parametrize('rows, players_symbol, expected', [
    (['*', 'X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '], 'X', 'win'),
    (['*', 'O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' '], 'O', 'win'),
    (['*', 'X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X'], 'X', 'win'),
    (['*', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O'], 'O', 'draw'),
    (['*', ' ', 'O', 'X', 'X', 'O', 'O', ' ', ' ', 'O'], 'X', None)
])
def test_check_win(rows, players_symbol, expected):
    assert check_win(players_symbol, rows) == expected


def test_starting_menu(capsys):
    starting_menu()
    capture = capsys.readouterr()
    expected = (
        "Welcome to the Tic Tac Toe game!\n"
        "\n"
        "Each Player will insert a number that is attached to certain area of the TicTacToe board. \n"
        "        The positional numbers are 1-9 and they are configured like this: "
        "\n1|2|3\n-----\n4|5|6\n-----\n7|8|9\n"
    )
    assert capture.out == expected


def test_reset_game():
    reset_game()
    assert rows == ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
