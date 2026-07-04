class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def checkRows(r):
            seen = set()
            for c in range(COLS):
                if board[r][c] == '.': continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
            return True
        
        for r in range(ROWS):
            if not checkRows(r):
                return False

        def checkCol(c):
            seen = set()
            for r in range(ROWS):
                if board[r][c] == '.': continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
            return True

        for c in range(COLS):
            if not checkCol(c):
                return False

        def checkSquare(r,c):
            seen = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j] == '.': continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True

        for r in range(0, ROWS, 3):
            for c in range(0, COLS, 3):
                if not checkSquare(r,c):
                    return False

        return True
