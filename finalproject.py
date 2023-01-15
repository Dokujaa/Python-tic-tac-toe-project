#This is my final project for tic tac toe
#Creator: Srikar Krothapalli



import random
import time
class TicBoard:
    def __init__(self, board):
        self.board = board

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']


    def getBoardCopy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in self.board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '


    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree( i):
                return False
        return True

    def isWinner(self, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        bo = self.board
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


    def makeMove(self, letter, move):
        self.board[move] = letter

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'player1'
        else:
            return 'player2'



class Player:
    def __init__(self, board):
        self.board = board

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def getPlayer1Move(self):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.board.isSpaceFree(int(move)):
            print('What is the move for player 1? (1-9)')
            move = input()
        return int(move)


    def getPlayer2Move(self):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.board.isSpaceFree(int(move)):
            print('What is the move for player 2? (1-9)')
            move = input()
        return int(move)


print('Welcome to Tic Tac Toe!')
print('The objective of the game is to get 3 in a row diagonally, verically, or horizontally')
print('You must decide to be either player 1 or player 2')
print()
print('''These are the spaces and their corresponding numbers for reference
   |   |
 7 | 8 | 9
   |   |
-----------
   |   |
 4 | 5 | 6
   |   | 
-----------
   |   |
 1 | 2 | 3
   |   |
''')


while True:
    # Initializes the board and player.
    theBoard = TicBoard([' '] * 10)
    moveset = Player(theBoard)

    # Gets the players' chosen letter.
    player1, player2 = theBoard.inputPlayerLetter()
    # Chooses which player gets to go first, randomly.

    turn = theBoard.whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player1':
            # Player 1's turn.
            theBoard.drawBoard()
            print('It is your turn ' + turn + ".", end=" ")
            move = moveset.getPlayer1Move()
            theBoard.makeMove(player1, move)
            time.sleep(0.25)

            if theBoard.isWinner(player1):
                theBoard.drawBoard()
                print('Hooray! Player 1 has won the game!')
                gameIsPlaying = False
            else:
                if theBoard.isBoardFull():
                    theBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player2'

        else:
            # Player 2's turn.
            theBoard.drawBoard()
            print('It is your turn ' + turn + ".", end=" ")
            move = moveset.getPlayer2Move()
            theBoard.makeMove(player2, move)
            time.sleep(0.25)

            if theBoard.isWinner(player2):
                theBoard.drawBoard()
                print('Player 2 has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if theBoard.isBoardFull():
                    theBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player1'

    if not moveset.playAgain():
        break

