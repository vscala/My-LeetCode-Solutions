class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Check rows and diagonals
        def valid(rows, board, i, j):
            if rows & (1 << j): return False
            for d in range(1, min(i, j)+1):
                if board[i-d][j-d] == "Q": return False
            for d in range(1, min(i, n-j-1)+1):
                if board[i-d][j+d] == "Q": return False
            return True
        
        # Backtrack over board
        def backtrack(board, rows, i):
            out = []
            if i == n: 
                return [["".join(x) for x in board]]
            for j in range(n):
                if valid(rows, board, i, j):
                    board[i][j] = 'Q'
                    rows ^= (1 << j)
                    out += backtrack(board, rows, i+1)
                    rows ^= (1 << j)
                    board[i][j] = '.'
            return out
        
        board = [["." for _ in range(n)] for __ in range(n)]
        return backtrack(board, 0, 0)