'''Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the 
nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.
Implement a function isValidSudoku that checks whether a 9 × 9 grid is a valid sudoku puzzle.
For the purpose of this question, assume that there will be only one unique solution.
'''

def isValidSudoku(board):
    #initialize three lists to store the numbers in the rows, columns, and boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    #iterate through the board
    for i in range(9):
        #iterate through the board
        for j in range(9):
            #store the value of the board at the current position
            val = board[i][j]
            #if the value is a dot, continue to the next iteration
            if val == '.':
                continue
            #store the value of the board at the current position
            if val in rows[i]:
                return False
            #add the value to the rows
            rows[i].add(val)
            #store the value of the board at the current position
            if val in cols[j]:
                return False
            #add the value to the columns
            cols[j].add(val)
            #store the value of the board at the current position
            box_index = (i // 3) * 3 + j // 3
            #store the value of the board at the current position
            if val in boxes[box_index]:
                return False
            #add the value to the boxes
            boxes[box_index].add(val)

    return True