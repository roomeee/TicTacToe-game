# TicTacToe-game
This piece of code is an implementation of a Tic-Tac-Toe game using the Tkinter library in Python. The game allows two players to take turns and aims to determine a winner or a tie.
Here's a breakdown of how the code works:

The game is played on a 3x3 grid represented by buttons. Each button represents a cell on the Tic-Tac-Toe board.

When a player clicks on a button, the next_turn function is called. It checks if the clicked button is empty and if there is no winner yet.

If the conditions are met, the button's text is updated with the current player's symbol (X or O).

After updating the button, the check_winner function is called to determine if the current move resulted in a win or a tie.

The check_winner function examines the buttons' texts in various combinations (rows, columns, diagonals) to check for a winning condition. If a winning condition is found, the corresponding buttons are highlighted with a purple background color.

If there is a winner, the label is updated to display the winning player's name. If the game is tied, a tie message is displayed.

The new_game function is triggered when the "reset" button is clicked. It resets the game state by randomly selecting a player to start and resetting the button texts and background colors. The label is updated to display the new player's turn.

The code uses the Tkinter library to create the graphical user interface. It creates a window with a title and various widgets, such as labels and buttons, to represent the game elements.

The window.mainloop() function is called to start the Tkinter event loop, which allows the program to respond to user interactions.

Overall, the code provides the functionality to play a game of Tic-Tac-Toe with a graphical interface. It handles player moves, checks for wins or ties, and allows for resetting the game to play again.





