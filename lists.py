#LISTS (31PTS TOTAL)
#In these exercises you should should use functions as needed.  All functions should have comments to describe their purpose.
import random

# PROBLEM 1 (Using List Comprehensions - 6pts)
# Use the list comprehension method to do the following:
# a) Make a list of numbers from 1 to 100
# b) Make a list of even numbers from 20 to 40
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)


a_list = [x for x in range(101)]
print(a_list)

b_list = [x for x in range(20, 41) if x % 2 == 0]
print(b_list)

c_list = [x ** 2 for x in range(101)]
print(c_list)

#PROBLEM 2 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.


answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]


def ball_8():
    input("Ask me anything: ")
    place = random.randrange(20)
    answer = answer_list.pop(place)
    print(answer)


ball_8()


# PROBLEM 3 (Shuffle - 5pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order.
# don't use the shuffle method, use pop maybe?


def cards():
    suits = ["Heart", "Diamond", "Club", "Spade"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = []
    shuffled_deck = []
    deck_length = 0

    for val in values:
        for suit in suits:
            deck.append(val + suit)
            deck_length += 1
    print(deck)
    print(deck_length)

    while deck_length > 0:
        shuffled_deck.append(deck.pop(random.randrange(deck_length)))
        deck_length -= 1
    print(shuffled_deck)


cards()


# PROBLEM 4 (Tic-Tac-Toe - 15pts)
# Write a Tic-Tac-Toe program that allows two people to play the game against each other.
# In turn, ask each player which row and column they want to play.
# Make sure that the program checks if that row/column combination is empty.
# When a player has won, end the game.
# When the whole board is full and there is no winner, announce a draw.
# This is a fairly long program to write (60 lines or so).
# It will definitely help to use some functions.
# I recommend that you create a function display_board() that gets the board
# as parameter and displays it,
# a function get_row_column() that asks for a row or a column (depending on a parameter)
# and checks whether the user entered a legal value,
# and a function winner() that gets the board as argument and checks if there is a winner.
# Keep track of who the current player is using a global variable player that you can
# pass to a function as an argument if the function needs it.
# I also use a function opponent(), that takes the player as argument and returns
# the opponent. I use that to switch players after each move.

# The main program will be something along the lines of (in pseudo-code):
# display board
game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
Done = False
turns = 0
player = "x"


def display_board(board):
    for row in board:
        for column in row:
            print(column, end = " ")
        print()


def opponent(number_turns):
    if number_turns % 2 == 0:
        player = "x"
    else:
        player = "o"
    return player


def get_row_column(current_player):
    row = int(input("Pick a row")) - 1
    column = int(input("Pick a column")) - 1
    game_board[row][column] = current_player


def winner():
    if game_board[0][0] == game_board[0][1] == game_board[0][2] == player:
        print("The winner is", player)
        return True
    elif game_board[1][0] == game_board[1][1] == game_board[1][2] == player:
        print("The winner is", player)
        return True
    elif game_board[2][0] == game_board[2][1] == game_board[2][2] == player:
        print("The winner is", player)
    elif game_board[0][0] == game_board[1][0] == game_board[2][0] == player:
        print("The winner is", player)
        return True
    elif game_board[0][1] == game_board[1][1] == game_board[2][1] == player:
        print("The winner is", player)
        return True
    elif game_board[0][2] == game_board[1][2] == game_board[2][2] == player:
        print("The winner is", player)
    elif game_board[0][0] == game_board[1][1] == game_board[2][2] == player:
        print("The winner is", player)
        return True
    elif game_board[0][2] == game_board[1][1] == game_board[2][0] == player:
        print("The winner is", player)
        return True


def draw():
    for row in game_board:
        if " " in row:
            break
    else:
        print("draw")


while not Done:
    turns += 1
    display_board(game_board)
    opponent(turns)
    get_row_column(player)
    winner()
    draw()

    '''   
    row = int(input("Pick a row")) - 1
    column = int(input("Pick a column")) - 1
    turns += 1
    print("Os go first followed by Xs")
    if board[row, column] == " ":
        if turns % 2 == 0:
            board.append("x", [row, column])
        else:
            board.append("o", [row, column])
    elif
    elif board == " ":
        print("pick again")
        continue
    else:
        print("Cat's Game")
        break
    for row in board:
        for column in row:
            print(board[column, row], end=" ")
    '''
#   ask for row
#   ask for column
#       if row/column already occupied:
#           display error
#   place player marker in row/col
#   display board
#   check for winner:
#       announce winner
#       break
#   check board full:
#       announce draw
#       break
#   switch player





# CHALLENGE PROBLEM 5 (MAY DO AS SUBSTITUTE FOR PROBLEM 4, NO ADDITIONAL CREDIT)
# Create a program that is a simplified version of the game “Battleship.”
# The computer creates (in memory) a grid that is 4 cells wide and 3 cells high.
# The rows of the grid are numbered 1 to 3, and the columns of the grid are labeled A to D.
# The computer hides a battleship in three random cells in the grid.
# Each battleship occupies exactly one cell.
# Battleships are not allowed to touch each other horizontally or vertically.
# Make sure that the program places the battleships randomly, so not pre-configured.
# The computer asks the player to “shoot” at cells of the grid.
# The player does so by entering the column letter and row number of the cell
# which she wants to shoot at (e.g., "D3").
# If the cell which the player shoots at contains nothing, the computer responds with “Miss!”
#  If the cell contains a battleship, the computer responds with “You sunk my battleship!”
# and removes the battleship from the cell (i.e., a second shot at the same cell is a miss).
# As soon as the player hits the last battleship, the computer responds with displaying
# how many shots the player needed to shoot down all three battleships, and the program ends.
# To help with debugging the game, at the start the computer should display the grid with
# O's marking empty cells and X's marking cells with battleships.
# Hint: If you have troubles with this exercise, start by using a board which has the
# battleships already placed.
# Once the rest of the code works, add a function that places the battleships at random,
# at first without checking if they are touching one another.
# Once that works, add code that disallows battleships touching each other.
