## Quest Details
#From the wise words of famous physicist Richard Feynman, "What I cannot create, I do not understand."
#In order to better understand the tic tac toe score-sheets found in the evil one's lair, you must program the game of tic tac toe.

#he program you create will be a command line interface (CLI) for playing tic tac toe that is implemented as a single python script (tictactoe.py).
#The game must support 2 human players, X and Y, who take turns placing their tiles on a 3x3 grid.
#Each player's input must be collected from the console via standard input (typing into the terminal).
#The board should be displayed after each player makes a move by printing it to standard output.
#The format in which input is collected and how the board is displayed to the terminal is up to you.
#A player wins when they have placed 3 of their own tiles in a row horizontally, vertically, or diagonally.
#If a player wins, you should indicate who the winning player is and end the game.
#The game ends in a draw when there are no more valid moves to be made (ex. the board is full)
#If the game ends in a draw, you should indicate this to the players and end the game.
#Lastly, it's of utmost important that you make this command line tic tac toe game as pretty and as fun as possible!

#Hint:
#To collect input from the console you can use the built in `input` function
#move = input("enter your move")


#ESTABLISH VARIABLES AND FUNCTIONS
board = [["0", " "], ["1", " "], ["2", " "], ["3", " "], ["4", " "], ["5", " "], ["6", " "], ["7", " "], ["8", " "]]
winX = False
winY = False
#boardFull = False
gameOngoing = True
turnCount = 0
moveValidity = False

def printBoard():
    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\nGAME BOARD\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    for i in range(3):
        print("⏐" + board[i][1], end = "⏐")
    #print("\n")
    #for i in range(5):
        #print("⎯", end = "")
    print("\n")
    for i in range(3):
        print("⏐" + board[i+3][1], end = "⏐")
    #print("\n")
    #for i in range(5):
        #print("⎯", end = "")
    print("\n")
    for i in range(3):
        print("⏐" + board[i+6][1], end = "⏐")
    print("\n")


def printHelp():
    print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\nHELP MENU\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    for i in range(3):
        print("⏐" + board[i][0], end = "⏐")
    #print("\n")
    #for i in range(5):
        #print("⎯", end = "")
    print("\t\tType the number for the", end = "")
    print("\n\t\t\tposition you would like to")
    for i in range(3):
        print("⏐" + board[i+3][0], end = "⏐")
    #print("\n")
    #for i in range(5):
        #print("⎯", end = "")
    print("\t\tplace your game piece.", end = "")
    print("\n")
    for i in range(3):
        print("⏐" + board[i+6][0], end = "⏐")
    print("\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n")


def checkXWin():
    global winX
    global gameOngoing

    if board[0][1] == "X" and board[4][1] == "X" and board[8][1] == "X":#check diagonal win
        winX = True
    elif board[2][1] == "X" and board[4][1] == "X" and board[6][1] == "X":
        winX = True
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":#check horizontal win
        winX = True 
    elif board[3][1] == "X" and board[4][1] == "X" and board[5][1] == "X":
        winX = True
    elif board[6][1] == "X" and board[7][1] == "X" and board[8][1] == "X":
        winX = True
    elif board[0][1] == "X" and board[3][1] == "X" and board[6][1] == "X":#check vertical win
        winX = True
    elif board[1][1] == "X" and board[4][1] == "X" and board[7][1] == "X":
        winX = True
    elif board[2][1] == "X" and board[5][1] == "X" and board[8][1] == "X":
        winX = True
    
    #stop the game
    if winX == True:
        gameOngoing = False


def checkYWin():
    global winY
    global gameOngoing

    if board[0][1] == "Y" and board[4][1] == "Y" and board[8][1] == "Y":#check diagonal win
        winY = True
    elif board[2][1] == "Y" and board[4][1] == "Y" and board[6][1] == "Y":
        winY = True
    elif board[0][1] == "Y" and board[1][1] == "Y" and board[2][1] == "Y":#check horizontal win
        winY = True 
    elif board[3][1] == "Y" and board[4][1] == "Y" and board[5][1] == "Y":
        winY = True
    elif board[6][1] == "Y" and board[7][1] == "Y" and board[8][1] == "Y":
        winY = True
    elif board[0][1] == "Y" and board[3][1] == "Y" and board[6][1] == "Y":#check vertical win
        winY = True
    elif board[1][1] == "Y" and board[4][1] == "Y" and board[7][1] == "Y":
        winY = True
    elif board[2][1] == "Y" and board[5][1] == "Y" and board[8][1] == "Y":
        winY = True
    
    #stop the game
    if winY == True:
        gameOngoing = False

''' uneeded code haha I realized there was a better method
def checkFull():
    global boardFull
    for i in range(9):
        if board[i][1] != "X" or board[i][1] != "Y":
            boardFull = False
            break
        else:
            boardFull = True
'''


#GAME STARTING MESSAGE
print("\n\nYou are playing Tic-Tac-Toe!\nConnect three of your game pieces in a straight line to win!\nYou will alternate turns between players X and Y.\n\nType \"help\" to see the help menu or \"board\" to see the current playing board at any time.")
printHelp()

#GAME RUNNING LOOP
while gameOngoing == True:
    #stuff to check before turn starts
    turnCount += 1
    printBoard()
    checkXWin()
    checkYWin()
    moveValidity = False

    if gameOngoing == False or turnCount > 9:
        break

    #identify whose turn it is
    if turnCount % 2 != 0:
        print("It is Player X's move.")
    elif turnCount % 2 == 0:
        print("It is Player Y's move.")

    #ask for input until move is valid
    while moveValidity == False:

        #ask for move
        move = input("Enter your next move: ")
        
        #check content of input
        if move.strip().lower() == "help":
            printHelp()
        elif move.strip().lower() == "board":
            print("\nCurrent Game Board:")
            printBoard()
        elif move.strip() == "0" or move.strip() == "1" or move.strip() == "2" or move.strip() == "3" or move.strip() == "4" or move.strip() == "5" or move.strip() == "6" or move.strip() == "7" or move.strip() ==  "8":

            #force int once content is verified to be a valid entry
            newMove = int(move.strip())

            #check if space indicated is occupied
            if board[newMove][1] == "X" or board[newMove][1] == "Y":
                print("This space is already occupied. Please try again.")
            else:

                #add piece to board
                board[newMove].pop(1)
                if turnCount % 2 != 0:
                    board[newMove].append("X")
                    moveValidity = True
                elif turnCount % 2 == 0:
                    board[newMove].append("Y")
                    moveValidity = True
        else:
            print("Invalid entry. Please try again. Type \"help\" for more info and \"board\" to check the current playing board.")


#DISPLAY END MESSAGE
if winX == True:
    print("Congratulations Player X! You have won this match of Tic-Tac-Toe.")
elif winY == True:
    print("Congratulations Player Y! You have won this match of Tic-Tac-Toe.")
else:
    print("This game has no winner. Thank you for playing.")