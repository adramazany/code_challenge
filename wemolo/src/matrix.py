class MatrixSolutions:
    # 1. Valid Sudoku
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": continue
                sq_idx = (r // 3) * 3 + (c // 3)
                if val in rows[r] or val in cols[c] or val in squares[sq_idx]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[sq_idx].add(val)
        return True

    # 2. Spiral Matrix
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix: res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]: res.append(row.pop(0))
        return res

    # 3. Rotate Image (In-place)
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
