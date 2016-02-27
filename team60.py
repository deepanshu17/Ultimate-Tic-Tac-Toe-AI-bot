import random
class Player60:
    def __init__(self):
        # initialization
        return

    def move(self, temp_board, temp_block, old_move, flag):
        print "+++++++++++++++++++++++++++++++++++++++"

        print old_move
        print flag
        allowed_blocks = get_free_and_valid_blocks(old_move, temp_block)
        print allowed_blocks
    
        block_number = allowed_blocks[0]
        block = get_block(block_number, temp_board)
        cell = get_allowed_cells(block_number, block)
        print cell
        print "+++++++++++++++++++++++++++++++++++++++"
        return cell

def print_block_by_number(block_number, board):
    x = (block_number / 3) * 3
    y = (block_number % 3) * 3
    print "================BLOCK================="

    for i in range(3):
        print board[x+i][y] + " " + board[x+i][y+1] + " " + board[x+i][y+2]

    print "================BLOCK================="

def is_allowed_block(block_number, temp_block):
    return temp_board[block_number] == '-'

def print_block(block):
    print "================BLOCK================="
    
    for i in range(3):
        print block[i*3] + " " + block[i*3+1] + " " + block[i*3+2]

    print "======================================"


def get_block(block_number, board):
    block = []
    x = (block_number / 3) * 3
    y = (block_number % 3) * 3
    
    for i in range(3):
        for j in range(3):
            block.append(board[x+i][y+j])
    
    #print_block(block)
    return block

def get_free_and_valid_blocks(old_move, game_stat):
    valid_blocks = get_valid_blocks(old_move)
    #print "**********************"
    #print valid_blocks
    #print game_stat
    #print "**********************"
    free_and_valid_blocks = []

    for block in valid_blocks:
        if game_stat[block] == '-':
            free_and_valid_blocks.append(block)

    if len(free_and_valid_blocks) == 0:
        for block_pos in range(9):
            if game_stat[block_pos] == '-':
                free_and_valid_blocks.append(block_pos)

    return free_and_valid_blocks
     

def get_valid_blocks(old_move):
    x = old_move[0] % 3 # verticle
    y = old_move[1] % 3 # horizontal
    # first-move
    if x < 0 and y < 0:
        return [i for i in range(10)]
    # upper
    if x == 0 and y == 0:
        # left
        return [1, 3]
    elif x == 0 and y == 1:
        # middle
        return [0, 2]
    elif x == 0 and y == 2:
        # right
        return [1, 5]
    
    # middle
    elif x == 1 and y == 0:
        # left
        return [0, 6]
    elif x == 1 and y == 1:
        # middle
        return [4]
    elif x == 1 and y == 2:
        # right
        return [2, 8]
    
    # lower
    elif x == 2 and y == 0:
        # left
        return [3, 7]
    elif x == 2 and y == 1:
        # middle
        return [6, 8]
    elif x == 2 and y == 2:
        # right
        return [5, 7]

def is_empty_cell(cell, block):
    index = (cell[0]*3) + cell[1]
    return block[index] == '-'


def get_allowed_cells(block_number, block):
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if is_empty_cell((x,y), block):
            print "Got the move " + str(x) + ", " + str(y)
            break
    return (x + (block_number/3)*3, y + (block_number%3)*3)
