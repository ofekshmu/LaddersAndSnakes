from logging import exception
import random
import numpy as np
import matplotlib.pyplot as plt

PLAYER1 = 1
PLAYER2 = -1
TIE = 0

def buildBoard(size):
    """
    @size: board size
    returns a @loc_lst containing all avaliable pairs of indexes on the board
    and an empty board initialized with zeros.
    * initialize value has no meaning as long as its different from @PLAYER1 AND @PLAYER2
    """
    loc_lst = []

    for i in range(size):
        for j in range(size):
            loc_lst.append((i,j))

    empty_Board = np.zeros( (size, size), dtype=np.int32 )
    
    return loc_lst, empty_Board

def checkWin_V2(player, board, move: tuple):
    """
    Same as checkWin but all decisions are made with numpy.
    """
    (x, y) = move # current move made    
    
    # checking row
    if np.all(board[x,:] == board[x, 0]):
        return True
    
    # checking coloumn
    if np.all(board[:,y] == board[0, y]):
        return True

    if x == y:
        diag_1 = board.diagonal()
        if np.all(diag_1 == diag_1[0]):
            return True

    if x - 9 == y:
        diag_2 = np.fliplr(board).diagonal()
        if np.all(diag_2 == diag_2[0]):
            return True

    return False

def checkWin(player, board, move: tuple):
    """
    check the board for a win and return True if found and flase otherwise.
    win is checked only on the corresponding row/col in which player currently made a move.
    diagonal is checked only if a was made on the diagonal lines.
    """
    n = len(board)
    (x, y) = move # current move made
    found = True # flag for determining if a win streak was found
    # check row
    for j in range(n):
        if board[x, j] != player:
            found = False
            break
    result = np.all(board[x,:] == board[x, 0])
    if result != found:
        raise exception("error....")
    
    if found:
        return found
    
    found = True
    # check col
    for i in range(n):
        if board[i, y] != player:
            found = False
            break
    
    result = np.all(board[:,y] == board[0, y])
    if result != found:
        raise exception("error....")

    if found:
        return found
    
    # check diagonal bottomleft to topright
    if x == y:
        found = True
        for i in range(n):
            if board[i, i] != player:
                found = False
                break
        if found:
            return found
        
    # check diagonal topleft to bottomright
    if x - 9 ==  y:
        found = True
        for i in range(n):
            if board[9 - i, i] != player:
                found = False
                break
    
    return found               

def gameLoop(boardSize = 3):
    """
    Game loop, including all basic game features
    """
    loc_lst, board = buildBoard(boardSize)
    currentPlayer = PLAYER1 # can be changed, PLAYER1 starts playing
    
    while True:
        # generate a random index out of the avaliable number of pairs
        rand_index = random.randint(0,len(loc_lst)-1)
        # pop the pair 
        (i, j) = loc_lst.pop(rand_index)
        # mark the board on the corresponding location
        board[i, j] = currentPlayer

        if checkWin_V2(player=currentPlayer, board=board, move=(i,j)):
            return currentPlayer
        
        # once location list is empty, no more moves are avaliable - tie
        if len(loc_lst) == 0:
            return TIE

        # Swich players
        currentPlayer = PLAYER1 if currentPlayer == PLAYER2 else PLAYER2


def simulate(n_simulations = 5000, boardSize = 3):
    """
    Simulate data according to assignment description
    """
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
    """
    Plot a graph describing the probability to get a TIE/player1 win/player2 win
    as a function of the board size.
    """
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

    # match x axis
    ax.set_ylim([0,1])
    x_lst = list(range(n))
    ax.set_xticks(x_lst)
    ax.set_xticklabels([x + initial_board for x in x_lst])

    #plt.show()

def main():
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

# if __name__ == "__main__":
#     main()

    