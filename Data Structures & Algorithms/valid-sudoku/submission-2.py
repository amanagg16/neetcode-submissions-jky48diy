from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}
        def col_based_board_num(j, start):
            board_num = -1
            if 0<=j<=2:
                board_num = start
            elif 3<=j<=5:
                board_num = start + 1
            else:
                board_num = start + 2
            
            return board_num
        def get_board_number(i, j):
            board_num = -1
            if 0<=i<=2:
                board_num = col_based_board_num(j, 0)
            elif 3<=i<=5:
                board_num = col_based_board_num(j, 3)
            else:
                board_num = col_based_board_num(j, 6)
            return board_num
        

        for i in range(9):
            for j in range(9):
                if board[i][j]!= ".":
                    r_num,c_num,b_num = "r_"+str(i)+str(board[i][j]), "c_"+str(j)+str(board[i][j]), "b_"+str(get_board_number(i,j))+str(board[i][j])
                    if r_num in seen or c_num in seen or b_num in seen:
                        return False
                    else:
                        seen[r_num] = True
                        seen[c_num] = True
                        seen[b_num] = True
            
        return True