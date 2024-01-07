# Tic Tac Toe Game
## Overview
This is a simple implementation of the classic Tic Tac Toe game in Python. 
The game supports two players taking turns to place their symbols ('X' and 'O') 
on a 3x3 board. The game continues until one player wins or the board is filled, 
resulting in a draw.

## How to Play
- Run the Python script `tic_tac_toe.py`.
- Each player takes turns entering a number (1-9) corresponding to the position on the Tic Tac Toe board.
- The game checks for a winner or a draw after each move.
- At the end of the game, players have the option to replay.

## Files

- `tic_tac_toe.py`: The main Python script containing the game logic.
- `README.md:` This file, providing information about the game.

## Functions
- board(values): Displays the Tic Tac Toe board with the current values.
- players_choice(): Takes user input for the position on the board.
- insert_choice(player_symbol, game_board): Inserts the player's symbol on the board at the chosen position.
- check_win(player_symbol, game_board): Checks if the current move results in a win or draw.
- starting_menu(): Displays the welcome message and initial board. 
- reset_game(): Resets the game board for a new round.
- ask_replay(): Asks the players if they want to play again.
- show_result(player): Displays the result of the game (win, draw).

## How to Run
- Ensure you have Python installed on your system.
- Run the script using the command: python tic_tac_toe.py

#### Ursan Cristian