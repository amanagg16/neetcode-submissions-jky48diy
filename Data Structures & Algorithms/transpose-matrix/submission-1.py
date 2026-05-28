class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])

        output = [[0 for _ in range(r)] for _ in range(c)]

        for i in range(r):
            for j in range(c):
                output[j][i] = matrix[i][j]

        return output