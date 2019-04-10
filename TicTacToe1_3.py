#------------------------------------
# Basic Terminal Tic Tac Toe
#------------------------------------
# This program allows two players to play tic tac toe in the terminal

# define variables
#------------------------------------
endGame = False             #boolean for checking if the game should end
player = "X"                #String to represent who's turn it is "X" or "O"
spacing = ""                #spacing variable to help make the output pretty
board = [                   
        ["_","_","_"],
        ["_","_","_"],
        ["_","_","_"]]      #2D array representing the board
n = 1                       #turn number

# define functions
#------------------------------------
# print board
def printBoard(b):
    print("\n")
    for r in b:
        print("\t\t\t\t", end = "||    ")
        for c in r:
            print(c, end = " ")
        print("   ||")

# check if x and y (coordinates from user) are  
#      integers 
#      between 0 and 2 
#      spot is not already taken
# if true for all return True
# if false for any print error and return False
def isValid(x, y, b):
    # check if integer 
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        
        # check if between 0 and 2 inclusive 
        if x>=0 and x<3 and y>=0 and y<3: 
            if b[y][x] == "_":
                return True
            else:
                print("\t\t\tERROR: That spot, it taken")
                return False
        else:
            print("\t\t\tERROR: Input must be and integer between 0 and 2")
            return False
    else:
        print("\t\t\tERROR: Input must be and integer between 0 and 2")
        return False

# switch from current player to other player and change spacing for output
def switchPlayer(p,s):
    if p == "X": 
        p = "O"
        s = "\t\t\t\t\t\t\t\t"
    else:
        p = "X"
        s = ""
    return (p,s)

# brute force method for checking if someone has won
def isWinnerBruteForce(b, p):
    #check 8 condition 3 rows, 3 columns and 2 diagonals
    w = [p == b[0][0] == b[0][1] == b[0][2],  
    p == b[1][0] == b[1][1] == b[1][2],  
    p == b[2][0] == b[2][1] == b[2][2],  
    p == b[0][0] == b[1][0] == b[2][0],  
    p == b[0][1] == b[1][1] == b[2][1],  
    p == b[0][2] == b[1][2] == b[2][2], 
    p == b[0][0] == b[1][1] == b[2][2],  
    p == b[0][2] == b[1][1] == b[2][2]]
    return any(w)

# GAME
#--------------------------------
# print board
printBoard(board)
# loop through turns untill endGame = True
while not endGame:
    
    # begin turn and print turn number
    print("\n\t\t\t--------- Staring Turn " + str(n) + " ---------")
    
    # request position from player until a valid position is given
    valid = False
    while not valid: 
        # request position from player
        x = input(spacing + "Player " + player + "\n" + spacing + "  >>Enter Column: ")
        y = input(spacing + "  >>Enter Row: ") 

        # check if position is valid
        # if valid assign possition to board if not request input again  
        if isValid(x, y, board) == True:
            board[int(y)][int(x)] = player # assign value to board
            valid = True
    
    printBoard(board)

    # check if player has won
    if n >= 5:
        if isWinnerBruteForce(board, player):
            endGame = True
            print("\n\t\t\t--------- GAME OVER ---------")
            print("\n\t\t\t Player " + player + " has won")

        elif n == 9:
            endGame = True
            print("\n\t\t\t--------- GAME OVER ---------")
            print("\n\t\t\t            Draw")
    
    # end turn over
    # switch player for next turn and increment turn number 
    (player,spacing) = switchPlayer(player,spacing)
    n = n+1
    

