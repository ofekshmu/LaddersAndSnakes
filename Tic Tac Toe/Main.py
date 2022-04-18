import random
import numpy as np
import matplotlib.pyplot as plt

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

    return stats
         
def plot_Data(lst, sim_count, initial_board):
    line_1, line_2, line_3 = [], [], []
    n = len(lst)
    for d in lst:
        line_1.append(d[PLAYER1]/sim_count)
        line_2.append(d[PLAYER2]/sim_count)
        line_3.append(d[TIE]/sim_count)

    fig, ax = plt.subplots()

    ax.plot(line_1, color = 'green', label = 'Player 1 wins')
    ax.plot(line_2, color = 'red', label = 'Player 2 wins')
    ax.plot(line_3, color = 'blue', label = 'Ties')
    ax.legend(loc = 'upper left')
    
    fig.suptitle('Probability as a function of Board Size', fontsize=12)
    ax.set_xlabel("Board size")
    ax.set_ylabel("Probability")

    ax.set_ylim([0,1])
    x_lst = list(range(n))
    ax.set_xticks(x_lst)
    ax.set_xticklabels([x + initial_board for x in x_lst])
    plt.show()

if __name__ == "__main__":
    data_lst = []
    n_simulations = 5000
    initial_board = 3
    last_board = 15
    for size in range(initial_board, last_board + 1):
        data = simulate(n_simulations, size)
        data_lst.append(data)

    #data_lst.append(simulate(n_simulations=5000, boardSize=25))
    #data_lst.append(simulate(n_simulations=5000, boardSize=50))
    
    plot_Data(data_lst, n_simulations, initial_board)

    #simulate(n_simulations=5000000, boardSize=25)
    #simulate(n_simulations=5000000, boardSize=50)

    