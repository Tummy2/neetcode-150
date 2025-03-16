from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        def checkRow(row):
            d = defaultdict(int)
            for cell in row:
                if cell in d and cell != ".":
                    return False
                d[cell] += 1
            return True

        def checkCol(col):
            d = defaultdict(int)
            for cell in col:
                if cell in d and cell != ".":
                    return False
                d[cell] += 1
            return True

        def checkBox(rowStart, rowStop, colStart, colStop):
            d = defaultdict(int)
            for i in range(rowStart, rowStop + 1):
                for j in range(colStart, colStop + 1):
                    if board[i][j] in d and board[i][j] != ".":
                        return False
                    d[board[i][j]] += 1
            return True

        for i in range(len(board)):
            if not checkRow(board[i]):
                return False

        for i in range(len(board)):
            col = []
            for j in range(len(board)):
                col.append(board[j][i])
            if not checkCol(col):
                return False

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                if not checkBox(i, i+2, j, j+2):
                    return False

        return True

test = Solution()

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
# Output: true
print(test.isValidSudoku(board))

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
# Output: false
print(test.isValidSudoku(board))

# Time: O(N^2)
# Space: O(N)
