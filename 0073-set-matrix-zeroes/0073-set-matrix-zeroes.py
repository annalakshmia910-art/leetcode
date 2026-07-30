class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r, c = len(matrix), len(matrix[0])
        fr = any(matrix[0][j] == 0 for j in range(c))
        fc = any(matrix[i][0] == 0 for i in range(r))

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if fr:
            matrix[0] = [0] * c
        if fc:
            for i in range(r):
                matrix[i][0] = 0
        