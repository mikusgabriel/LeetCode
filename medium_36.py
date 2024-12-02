# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        hash_col = {}
        hash_square = {}
        for i in range(len(board)):
            hash_row = {}
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    #column
                    if j not in hash_col:
                        hash_col[j] = {board[i][j]: 1}
                    else:
                        if  board[i][j] in hash_col[j]:
                            return False
                        else:
                            hash_col[j][board[i][j]] = 1
                    
                    #rows
                    if board[i][j] not in hash_row:
                        hash_row[board[i][j]] = board[i][j]
                    else:
                        return False

                    #square
                    vertical_counter = i // 3
                    horizontal_counter = j // 3 
                    square_id = str(vertical_counter)+str(horizontal_counter)
                    if  square_id not in hash_square:
                        hash_square[square_id] =   {board[i][j]: 1}

                    else:
                        if  board[i][j] in hash_square[square_id]:
                            return False
                        else:
                            hash_square[square_id][board[i][j]] = 1
                    



        return True
