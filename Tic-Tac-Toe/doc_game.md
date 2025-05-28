🔢 Sections Overview for **game.py**
---

|Sec. No.|              Name            |                       Purpose               |
|:------:|:-----------------------------|---------------------------------------------|
|   1    |Imports and Dependencies      |Brings in required modules and player classes|
|   2    |TicTacToe Class -             |Sets up the game board and winner tracking   |
|        |Initialization                |                                             |
|   3    |TicTacToe Class - Board       |Handles visual representation of the board   |
|        |Display Helpers               |                                             |
|   4    |TicTacToe Class - Game        |Core logic for making moves and checking for | 
|        |Mechanics                     |winners                                      |  
|   5    |TicTacToe Class - Utility     |Helper functions for empty squares and valid |
|        |Methods                       |moves                                        |      
|   6    |play() Function               |Runs the actual game loop and player turns   |
|   7    |if __name__ == '__main__'Block|Initializes players and starts the game      |
                                            
---
---                                            
# Section 1: Imports and Dependencies
```python
import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer
```
🔍 Line-by-line Explanation:
---
- **import math**: Brings in Python’s built-in math module, used for calculations
(like **math.floor**).

- **import time**: Used to add delays between turns (for a smoother user experience).

- **from player import ...**: Imports the three player types from the **player.py** 
file you created earlier.

> These imports make sure we can use the player classes, time delays, and mathematical
utilities later in the script.
        
---
---
# 🎲 Section 2: TicTacToe Class – Initialization
```python
class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
```
🔍 Line-by-line Breakdown:
---
**class TicTacToe():**
- This defines a new class named **TicTacToe**.

- It will contain all the data (like the board) and behavior (like making moves) needed for the game.
---
**def __init__(self):**
- This is the constructor method. It runs automatically when you create a new **TicTacToe** object.

- Inside it:

    - **self.board = self.make_board()** creates the board.

    - **self.current_winner = None** keeps track of the winner (initially there's no winner).
---
**@staticmethod**
- This means **make_board()** doesn’t need to use **self** (i.e., it doesn’t access any instance data).

- It’s a helper function tied to the class logically, but not to a specific object.
---
**def make_board():**
- Returns a list of 9 spaces: **[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']**

- This represents an empty 3x3 Tic-Tac-Toe board using a flat list of 9 cells.

> Think of the board like this (initially):
```python
|   |   |   |
|   |   |   |
|   |   |   |
```
- Each space can later be filled with **'X'** or **'O'** as players make moves.
---
---
# 🧾 Section 3: Board Display Helpers
```python
def print_board(self):
    for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

@staticmethod
def print_board_nums():
    number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    for row in number_board:
        print('| ' + ' | '.join(row) + ' |')
```
🔍 Line-by-line Breakdown:
---
**🧱 print_board(self)**
- This method displays the current game board with Xs and Os (or blanks) where moves have been made.

> Let's break it:
```python
for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
```
- This turns the flat 9-element list into 3 rows:
    - Row 0: self.board[0:3]

    - Row 1: self.board[3:6]

    - Row 2: self.board[6:9]

> So the comprehension builds:
```python
[
  [' ', ' ', ' '],  # Row 1
  [' ', ' ', ' '],  # Row 2
  [' ', ' ', ' ']   # Row 3
]
```
> Then:
```python
print('| ' + ' | '.join(row) + ' |')
```
- Joins each row’s cells with " | " and adds border lines.

- Example Output
```python
|   |   |   |
|   |   |   |
|   |   |   |
```
---
**🔢 @staticmethod def print_board_nums():**
- This prints the board positions (0–8) to help the human player know which number to input for their move.

- Inside:
```python
number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
```
- Builds a 3x3 matrix with the numbers 0–8 as strings:
```python
[
  ['0', '1', '2'],
  ['3', '4', '5'],
  ['6', '7', '8']
]
```
- Then:
```python
print('| ' + ' | '.join(row) + ' |')
```
- Same as before, but now prints square numbers.
> Example Output
```python
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |
```
---
These two functions help the user see both:
- What the board looks like

- Where they can play next
---
---
# 🎯 Section 4: Making Moves & Checking for a Winner
```python
def make_move(self, square, letter):
    if self.board[square] == ' ':
        self.board[square] = letter
        if self.winner(square, letter):
            self.current_winner = letter
        return True
    return False
```
🎯 **make_move()**
- This function places a move on the board and checks if it caused a win.
---
🔍 Line-by-line Breakdown:
---
```python
if self.board[square] == ' ':
```
- Checks if the selected square is empty. Only valid moves allowed
```python
self.board[square] = letter
```
- Places the letter ('X' or 'O') in that square.
```python
if self.winner(square, letter):
    self.current_winner = letter
```
- After the move, it checks: Did this move win the game?

- If yes, it updates **current_winner**.
```python
return True
```
- If the move was made successfully, return **True**.
```python
return False
```
- If the square was already taken, return **False**.
---
🏆 **winner()** Function
> This is the most logic-heavy part of the game board:
```python
def winner(self, square, letter):
    row_ind = math.floor(square / 3)
    row = self.board[row_ind*3:(row_ind+1)*3]
    if all([s == letter for s in row]):
        return True
```
> Checks 3 things:
---
1. **Row Check**
```python
row_ind = math.floor(square / 3)
row = self.board[row_ind*3:(row_ind+1)*3]
```
- Finds the row index (0, 1, 2)

- Gets that row from the board.
```python
if all([s == letter for s in row]):
    return True
```
- If every item in the row is the same letter, it's a win
---
2. **Column Check**
```python
col_ind = square % 3
column = [self.board[col_ind + i*3] for i in range(3)]
if all([s == letter for s in column]):
    return True
```
- Uses modulo to get column index.

- Grabs items in that column (e.g., 0, 3, 6 for the first column).
---
3. **Diagonal Check**
```python
if square % 2 == 0:
```
- Diagonals only involve even-numbered squares: 0, 2, 4, 6, 8.
```python
diagonal1 = [self.board[i] for i in [0, 4, 8]]
if all([s == letter for s in diagonal1]):
    return True

diagonal2 = [self.board[i] for i in [2, 4, 6]]
if all([s == letter for s in diagonal2]):
    return True
```
- Checks both diagonals for a win.
```python
return False
```
- If no win is found in any direction, return False.
---
> That completes the move logic and winner check!
---
---
# 🛠️ Section 5: Helper Functions
> These utility methods help the game logic stay clean and readable.

**✅ empty_squares(self)**
```python
def empty_squares(self):
    return ' ' in self.board
```
- Purpose: Checks if there are any available moves left.

- Returns **True** if at least one **' '** (empty square) exists on the board.
---
**🔢 num_empty_squares(self)**
```python
def num_empty_squares(self):
    return self.board.count(' ')
```
- Purpose: Counts how many **empty squares** are still left.

- Useful for both game logic and for evaluating scores in the Minimax algorithm.
---
**📋 available_moves(self)**
```python
def available_moves(self):
    return [i for i, x in enumerate(self.board) if x == " "]
```
- Purpose: Returns a list of **valid move positions**.

- Uses **enumerate** to loop through the board with indices.

- Only adds the index to the list if the square is **' '** (empty).
---
🧠 Why These Helpers Matter
---
> These functions:

- Keep the game loop clean (e.g., **while game.empty_squares():** )

- Help the AI (especially Minimax) determine valid states to simulate

- Reduce code duplication
---
---
# 🎮 Section 6: Game Loop & Execution
> This part includes the main function **play()** and the script execution block at the bottom.
---
**🔁 def play(game, x_player, o_player, print_game=True)**
- This function contains the main game loop.
---
**✅ if print_game: game.print_board_nums()**
- Shows a number-labeled board at the start so the human player knows which number corresponds to which position.
---
**🎯 Game Loop Begins**
```python
letter = 'X'
while game.empty_squares():
```
- Sets the starting player to **'X'**.

- Loops while there are moves left.
---
**🎲 Player Takes Turn**
```python
if letter == 'O':
    square = o_player.get_move(game)
else:
    square = x_player.get_move(game)
```
- Depending on whose turn it is, the correct player's **get_move()** function is called.

- Could be a human or AI, depending on what was passed in.
---
**✅ Make Move**
```python
if game.make_move(square, letter):
```
- If the selected move is valid (the square is empty), make the move.
---
**🖨️ Display Move (Optional)**
```python
if print_game:
    print(letter + ' makes a move to square {}'.format(square))
    game.print_board()
    print('')
```
- Shows which square was played and updates the visual board.
---
**🏆 Win Condition Check**
```python
if game.current_winner:
    if print_game:
        print(letter + ' wins!')
    return letter
```
- If the current player wins after this move, print a win message and end the game.
---
**🔄 Switch Player**
```python
letter = 'O' if letter == 'X' else 'X'
```
- Alternates between **'X' and 'O'**.
---
**🕒 Add Delay**
```python
time.sleep(.8)
```
- Adds a short pause so moves aren’t instant — improves user experience.
---
**😐 Tie Condition**
```python
if print_game:
    print('It\'s a tie!')
```
- After exiting the loop, if no one has won, it's a tie.
---
---
# 🚀 Section 7: if __name__ == '__main__':
```python
if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
```
- This is the entry point for the script.

- Creates:

    - A smart AI player as **'X'**

    - A human player as **'O'**

    - A **TicTacToe** game instance

- Then calls **play()** to start the game!
---
🧠 Key Takeaways
---
- The game loop coordinates everything: board display, move input, turn-taking, and win/tie checking.

- Clean separation of logic makes it easier to test or extend later (e.g., making a GUI or networked version).
---
---
## That wraps up the full walkthrough of game.py!
---


