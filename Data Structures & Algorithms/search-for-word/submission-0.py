class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, n = len(board), len(board[0]), len(word)


        def dfs(i, j, curr):
            if curr == n - 1:
                return True
            
            temp = board[i][j]
            board[i][j] = "#"
            curr += 1
            nei = [[i, j+1],[i, j-1],[i-1, j],[i+1, j]]

            for r, c in nei:
                if 0<=r<rows and 0<=c<cols and board[r][c] == word[curr] and dfs(r, c, curr):
                    return True
            
            board[i][j] = temp
            return False


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
            
        return False