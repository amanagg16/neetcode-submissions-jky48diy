class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])

        output = []

        for j in range(c):
            output.append([])
            for i in range(r):
                output[j].append(matrix[i][j])
        return output