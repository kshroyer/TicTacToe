This is a tic tac toe game for two players in the terminal.  Wrote as a code example for an application.  Its not the fanciest or the most efficient, but here it is.
--------------------------------------------------------------
OVERALL STRUCTURE
--------------------------------------------------------------
    
    clear board
    
    TURN1
        1: who’s turn is it? X or Y 
        2: prompt player to take turn
        3: What spot was chosen?
        4: is that spot valid (not chosen already)?
                YES —> move on
                NO —> errer return to prompt (2)
        update board representation
        
        has any one won? 
            YES —> declare winner + end game
            NO —> move on to next turn
    TURN 2 
    
    TURN 3 
    TURN 4 ……

I’m a learning scientist, I study informal learning and design process, so I just wanted to reflect a little on my process of constructing the code.
First off I wrote out a version of the list above.  What are all the elements of the game that need to be represented and how do they relate to each other.

RULES: The rules of tic tac toe are operationalized as follows
* the game has two players (X and O)
* the mage has a 3 by 3 board
* the game is made up of turns
* the 2 players alternate turns
* each turn, the active player choses 1 spot on the board
* that tile must be blank
* a player wins when they have 3 spots in a row on the board

REPRESENTATION
* the game has 9 positions that need to be represented.
* each position can be blank, player 1, or player 2

TURN
* show the current board
* player choses position
* if the player has three in a row - they win game ends
* if no one has three in a row and there are spots on the board left it is the next players turn else its a draw and the game ends

--------------------------------------------------------------
Phase 1: 
--------------------------------------------------------------

Q1: how do i request values from the user?
The first thing i wanted to figure out was how to request values from the user.  It’s been a while since I have python and my go to syntax is always Java.   Found the input function and some syntax.  Played with how it worked in terminal and started my program with that.  I had not yet figured out how i was going to represent the position choice but now had a way to request input regardless of what it was.

Q2: Ok, how do I advance through turns?
Was thinking a while loop will be useful later when i’m checking for win state, for now I just created a for loop that looped through 10 times.  This will allow me to test some turns without having to deal with checking win state yet.  Had to look up syntax for for loop, so rusty.

Q3: Cool, so I can loop through 10 turns and request some kind of position from the user, now how do switch players each turn?
I’m sure there are many ways to do this.  The first thing that came to mind was to have a variable that contained the current player, then to switch this each time by asking if it was player 1 and changing to player 2 if it was and back to player 1 if it was not.  Added a print statement to check that the variable was switching each time.  I used strings Player 1 and Player 2 then later switched to X and O
“re-discover” that python is dynamically typed.  Was trying to define variable types and type cast.  We don’t do that here.
Excellent, so now I can loop through 10 turns, ask the user for input, and switch players each turn. 

Q4:  How do I represent the board?
There are so many data structures with different affordances.  I’m no expert.  I chose to use a 2D array largely because it was cognitively efficient for me (not the most efficient in terms of memory). 
Alrighty, now we can loop through 10 turns, players alternate, i ask the player for a coordinate on the board, then store that player’s character (X or O) in the 2D board array.

Q5: How do I display the board
Now i want to display the board some how.  As much for me for troubleshooting as for the players.  I briefly hunt for a function that will print a pretty formatted 2D array.  Didn’t see anything so created nested for loops to print out each position.

Q6:  How do I assign a value to the board?
At this point I decide that an easy way to proceed given this data structure is to have the users put in x and y coordinates.  I figured I would figure out a better method of choosing position later but have not gotten to it yet.  I forgot that you can’t initialize things in python so i build a 2D array with “_” to represent blank spots. Added some code to assign the player to the coordinate chosen.
  
Q7:  How do I make sure a spot is not taken

Q8 how do i make visually easier to see what’s happening
Q9 how might i check to make sure spot is not taken and warn
Q10 how might i check that value is integer [0-2]

--------------------------------------------------------------
Phase 2: putting stuff in functions
--------------------------------------------------------------
Next phase was some cleaning up of what already was working.  I had not put anything into functions, everything was in one big code block.  So I went through in chunks making different pieces into functions.  This was based on the abstraction of the major moves that make up the game outlined above.  So printing the board, changing players, and checking if position is valid.  I might have made a place holder for checking the win state at this point as well.
Spent some time at this point making the output easier to read and messing with line spacing and tabbing over some of the text, making the board look like board.  It was really hard to see who’s turn it was so i formatted the output so that the board was in the middle of the terminal, player 1 on the left and player 2 on the right.
Phase 3: adding win state checker

Q1: What if the user input is not an integer

Q2: Brute force board checker

Q3: What if there is a draw?

--------------------------------------------------------------
SOME REFLECTIONS
--------------------------------------------------------------

So what is interesting to me is that i had some conception of how to set up the program but things came up as I was building and prototyping that i would not have thought of and i had to problem solve in the moment.  I feel like i need more of a plan when i’m doing mechanical kind of work because the wasting or materials or time to use equipment necessitate less mistake making. So one example is the output, i coudl have told you making functions is cleaner, but i just didn’t do it at the beginning untill it seemed necessary. I could have predicted that i would need to and started that way.  Maybe i would have if i had made an active decison but i didn’t.
