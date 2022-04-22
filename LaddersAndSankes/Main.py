import random

# None variable indicates no ladder or snake in this index
NONE = -1

def build_board():
    return [[NONE,80,NONE,NONE,NONE,75,NONE,NONE,88,NONE],
             [NONE,NONE,NONE,NONE,NONE,NONE,94,NONE,68,NONE],
             [NONE,NONE,98,NONE,NONE,NONE,53,NONE,NONE,91],
             [NONE,19,NONE,60,NONE,NONE,NONE,NONE,NONE,NONE],
             [NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,NONE,67],
             [NONE,NONE,NONE,NONE,NONE,25,NONE,NONE,11,NONE],
             [NONE,NONE,NONE,NONE,44,NONE,NONE,NONE,NONE,NONE],
             [42,NONE,NONE,NONE,NONE,NONE,NONE,84,NONE,NONE],
             [NONE,NONE,NONE,NONE,6,26,NONE,NONE,NONE,NONE],
             [NONE,38,NONE,NONE,NONE,NONE,14,31,NONE,NONE]]

def roll_dice():
    """
    Returns a number on a dice
    """
    return random.randint(1,6)

def check_sum(outcome, position):
    """
    @outcome - dice roll - a number in [1,6]
    @position - the players position [1,100]
    returns True if outcome equals to final position's sum of digits (until we get one digit number), False otherwise
    """
    sum_digits = position // 100 % 10 + position // 10 % 10  + position % 10
    if outcome == sum_digits:
        return True
    return False

def  get_board_value(board, position):
    """
    @board : game board
    @position : player position
    returns the value corresponding to the position of the player
    """
    ones = position % 10
    tens = position // 10 % 10
    # deciding columns - j
    if ((position - 1) // 10 % 10 ) % 2 == 0 : # even
        if ones == 0:
            j = 9
        else:
            j = ones - 1
    else: # odd
        if ones == 0:
            j = 0
        else:
            j = 10 - ones    
    # deciding rows - i   
    if ones == 0 :
        i = 9 - (tens - 1)
    else:
        i = 9 - tens
    
    return board[i][j]

def game_Loop(board):
    
    dice_counter = 0

    position = 1
    while( True ):
        dice_counter += 1 # dice_counter = dice_counter + 1
        outcome = roll_dice()
        position = position + outcome
        # Ending condition 
        
        if position > 100:
            extra_steps =  position - 100
            position = 100 - extra_steps

        if check_sum(outcome, position) :
            position = position // 2

        if position == 100:
            #print("Game Finished")
            return dice_counter
        
        value = get_board_value(board, position)
        if value != NONE :
            position = value

        #print(f"dice: {outcome}, position: {position}, value: {value}, cond: {check_sum(outcome, position)}")



if __name__ == "__main__":
    board = build_board()

    n_simulations = 5000
    sum = 0
    
    for i in range(n_simulations):
        dice_counter = game_Loop(board)
        sum += dice_counter
    
    print(f"The mean is {sum/n_simulations}")
