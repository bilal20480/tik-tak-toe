Tic Tac Toe - Best of 3 (Tkinter)
This is a Tic Tac Toe game built with Python using the tkinter library, featuring a best-of-3 match format. Players can enter their names, and the game alternates turns between two players. The game ends when one player wins 2 out of 3 rounds. The winner of each round is highlighted with a green color, and a final screen appears to display the overall winner or if there was a tie, with the option to exit the game.

Features
Best of 3: Players compete in a best-of-3 format.

Dynamic Player Names: Players can enter their own names before the game starts.

Random Symbol Assignment: Players are randomly assigned either "X" or "O".

Round Winner Highlights: Winning moves are highlighted in green.

Draw Detection: If all the cells are filled and no winner is determined, it's a draw.

Golden Chance: In case of a tie, the player who wins the golden chance is displayed as the winner.

Final Result Screen: Displays the overall winner of the game in a full-screen mode with an exit option.

Requirements
Python 3.x

Tkinter (comes pre-installed with Python)

Game Flow
Start Screen: Players input their names to start the game.

Game UI: The game board is a 3x3 grid where players alternate turns by clicking on empty cells.

Round Over: After each round, a winner is announced (if there is one). The board is reset, and the game continues.

Final Result: Once a player wins 2 out of 3 rounds, a final screen will show the overall winner.

Screenshots

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Tkinter for GUI development.

Python's random module for random symbol assignment.
