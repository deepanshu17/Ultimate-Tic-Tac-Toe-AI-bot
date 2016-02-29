import random
import copy
class Player60:
    def __init__(self):
        # initialization
        return

    def move(self, temp_board, temp_block, old_move, flag):
        print "+++++++++++++++++++++++++++++++++++++++"

        print old_move
        print flag
        allowed_blocks = get_free_and_valid_blocks(old_move, temp_block)
    
        cells = get_allowed_cells(allowed_blocks, temp_board)
        #print len(cells)
        print cells
        best_score = float('-inf')
        best_move = cells[0]
        board_copy = copy.deepcopy(temp_board)

        for cell in cells:
            future_board = minimax(board_copy, cell, flag, temp_block)
            score = get_score(future_board)
            if score > best_score:
                best_score = score
                best_move = cell
            break 

        print "+++++++++++++++++++++++++++++++++++++++"
        print best_move
        print 
        return best_move

def get_score(board):
    #print_board(board)
    return 10

def minimax(board, move, flag, board_stat):
    board = max_move(board, move, flag)
    board_stat = update_board_stat(board, board_stat, move)
    print_board(board)
    return board
    opp_flag = 'x' if flag == 'o' else 'o'
    allowed_blocks = get_free_and_valid_blocks(move, board_stat)
    cells = get_allowed_cells(allowed_blocks, board)
    print "************************"
    print allowed_blocks
    print "************************"
    board = min_move(board, move, opp_flag)
    return board

def max_move(board, move, flag):
    x = move[0]
    y = move[1]
    board[x][y] = flag
    #print_board(board)
    return board


def min_move(board, move, flag):
    x = move[0]
    y = move[1]
    board[x][y] = flag
    #print_board(board)
    return board

def update_board_stat(board, board_stat, move):
    # update board stat 
    print move
    block_number = get_block_number(move)
    print block_number
    block = get_block(block_number, board)
    print_block(block)
    #print_board_stat(board_stat)
    return board_stat

def get_block_number(move):
    x = move[0]
    y = move[1]
    if x < 3 and y < 3:
        return 0
    elif x < 3 and (y>=3 and y<6):
        return 1
    elif x < 3 and (y>=6 and y<9):
        return 2

    elif x < 6 and y < 3:
        return 3
    elif x < 6 and (y>=3 and y<6):
        return 4
    elif x < 6 and (y>=6 and y<9):
        return 5

    elif x < 9 and y < 3:
        return 6
    elif x < 9 and (y>=3 and y<6):
        return 7
    elif x < 9 and (y>=6 and y<9):
        return 8

                 

def print_board_stat(bs):
    print "=========== Block Status ========="
    for i in range(0, 9, 3): 
        print bs[i] + " " + bs[i+1] + " " + bs[i+2] 
    print "=================================="
    print


def print_board(gb):
    print '=========== Board ====================='
    for i in range(9):
        if i > 0 and i % 3 == 0:
                print
        for j in range(9):
                if j > 0 and j % 3 == 0:
                        print " " + gb[i][j],
                else:
                        print gb[i][j],

        print
    print "========================================"

def print_block_by_number(block_number, board):
    x = (block_number / 3) * 3
    y = (block_number % 3) * 3
    print "================BLOCK================="
    for i in range(3):
        print board[x+i][y] + " " + board[x+i][y+1] + " " + board[x+i][y+2]
    print "================BLOCK================="

def print_block(block):
    print "================BLOCK================="    
    for i in range(3):
        print block[i*3] + " " + block[i*3+1] + " " + block[i*3+2]
    print "======================================"

def is_allowed_block(block_number, temp_block):
    return temp_board[block_number] == '-'

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
    # first-move
    if old_move[0] < 0 and old_move[1] < 0:
        return [i for i in range(9)]

    x = old_move[0] % 3 # vertical
    y = old_move[1] % 3 # horizontal
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

def get_allowed_cells(blocks, board):
    print blocks
    allowed_cells = []
    for block in blocks:
        block_stat = get_block(block, board)
        for i in range(3):
            for j in range(3):
                if is_empty_cell((i,j), block_stat):
                    #print "Got the move " + str(i) + ", " + str(j)
                    allowed_cells.append((i + (block/3)*3, j + (block%3)*3))

    return allowed_cells
