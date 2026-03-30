from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}
        def get_board_number(i, j):
            board_num = -1
            if 0<=i<=2:
                if 0<=j<=2:
                    board_num = 0
                elif 3<=j<=5:
                    board_num = 1
                else:
                    board_num = 2
            elif 3<=i<=5:
                if 0<=j<=2:
                    board_num = 3
                elif 3<=j<=5:
                    board_num = 4
                else:
                    board_num = 5
            else:
                if 0<=j<=2:
                    board_num = 6
                elif 3<=j<=5:
                    board_num = 7
                else:
                    board_num = 8

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