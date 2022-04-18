# Ladders and Snakes

This ReadMe file will explain any code implementations which is not trivial. it will not go over the instructions of the Assignment, these are written in hebrew in the attached PDF

## TASK 1 - Ladders and Snakes
  
- Board creation 
In order to make it simple, finding a ladder/snake while traveling the board, I decided to build it as follows:
each location which has not special trait (does not have a snake/ladder) will contain the value "-1" (defined by the variable NONE), all other values on the board represents such elements. A number on the board will indicate the next destination of the player. Their is easly seen indication if a snake or a ladder has been encountered, **but** by finding the location delta from before location change to after, one can reveal this information.

- Board location indexing
To keep it as simple as possible, Matrix was created identical to the one given on the assignment PDF, but one should notice the following:
1. location indexes start from 1 to 100, starting at the bottom left up until the top left.
2. indexes go from side to side; Left to right, right to left, left to right and so on...

for these reasons a function for converting the actual player position to **Matrix indexes** was created.

## TASK 2 - Tic Tac Toe

Data Base used to handle Game information:

List - The @loc_list is created in the buildBoard(...), initialized empty and returned containing all possible pairs (tuples) of rows and coloumns indexes. All pairs in this list indicate avaliable spots on the Tic Tac Toe board - avaliable spots are locations which no player had made a move on yet.

**Why?** By using a list to indicate all avaliable locations left, a more efficient generation of random numbers can be made - In order to pick a random location to play, a number is generated between 0 and the size of the location list -1 which is later used to pick a rando pair. This method enables a selection of avaliable locations on the board **with out making "mistakes"**, mistakes meaning - not picking a location which has been picked before.

numpy multi-demensional array (Matrix) - The Matrix will represent the Game board and its main application is to help determine winning conditions easily. By updating selected locations on the Matrix game board, a simple for loop can enable us determine if the current player won.

note: Winning cnditions are checked only on the row/col the current player has played on. Also, diagonal winning conditions are checked in the same circumstances.


