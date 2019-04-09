 #3.6.3


# define variables
#------------------------------------
endGame = False    #bool
player = "X"     #String
spacing = ""
board = [
        ["_","_","_"],
        ["_","_","_"],
        ["_","_","_"]]
n = 1

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
    print("\n") 

# check if x and y are both 
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

        if x>=0 and x<3 and y>=0 and y<3: 
            if b[y][x] == "_":
                return True
            else:
                print("\t\t\tERROR: That spot it taken")
                return False
        else:
            print("\t\t\tERROR: Input must be and integer between 0 and 2")
            return False
    else:
        print("\t\t\tERROR: Input must be and integer between 0 and 2")
        return False

def switchPlayer(p,s):
    if p == "X": 
        p = "O"
        s = "\t\t\t\t\t\t\t\t"
    else:
        p = "X"
        s = ""
    return (p,s)

# brute force method
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

def isWinner(board, player):
    for r in board:
        for c in r:
            print(c)



# loop through 10 turns
#--------------------------------
# print board
printBoard(board)
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
            print(" Player " + player + " has won")
        elif n == 9:
            endGame = True
            print("DRAW") 
    
    # end turn over
    # switch player for next turn and increment turn number 
    (player,spacing) = switchPlayer(player,spacing)
    n = n+1
    


