import random
import numpy as np

PLAYER1 = 1
PLAYER2 = -1
TIE = 0

def gen_random():
    pass

def buildBoard(size):
    loc_lst = []
    for i in range(size):
        for j in range(size):
            loc_lst.append((i,j))

    return loc_lst, np.zeros( (size, size), dtype=np.int32 )

def checkWin(player, board, move: tuple):
    n = len(board)
    (x, y) = move
    found = True
    # check row
    for j in range(n):
        if board[x, j] != player:
            found = False
            break
    if found:
        return found
    
    found = True
    # check col
    for i in range(n):
        if board[i, y] != player:
            found = False
            break
    if found:
        return found
    
    # check diagonal
    if x == y:
        found = True
        for i in range(n):
            if board[i, i] != player:
                found = False
                break
    return found               

def gameLoop(boardSize = 3):
    
    loc_lst, board = buildBoard(boardSize)
    currentPlayer = PLAYER1
    
    while True:
        rand_index = random.randint(0,len(loc_lst)-1)
        (i, j) = loc_lst.pop(rand_index)
        board[i, j] = currentPlayer
        #print(board)
        if checkWin(player=currentPlayer, board=board, move=(i,j)):
            return currentPlayer
        
        if len(loc_lst) == 0:
            return TIE

        # Swich players
        currentPlayer = PLAYER1 if currentPlayer == PLAYER2 else PLAYER2


def simulate(n_simulations = 5000, boardSize = 3):
    stats = {PLAYER1: 0, PLAYER2: 0, TIE: 0}

    for i in range(n_simulations):
        result = gameLoop(boardSize)
        stats[result] += 1
    
    print(f"""~~~ Simulation results ~~~
simulations count: {n_simulations}, board size: {boardSize}
\tPlayer1 won {stats[PLAYER1]} times
\tPlayer2 won {stats[PLAYER2]} times
\tTie has accured {stats[TIE]} times\n""")
         

if __name__ == "__main__":
    for size in range(3,16):
        simulate(n_simulations=5000, boardSize=size)
    
    simulate(n_simulations=5000, boardSize=25)
    simulate(n_simulations=5000, boardSize=50)
    
    #simulate(n_simulations=5000000, boardSize=25)
    #simulate(n_simulations=5000000, boardSize=50)

    