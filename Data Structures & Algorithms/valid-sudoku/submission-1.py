# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for row in range(9):
#             seen = set()
#             for col in range(9):
#                 if board[row][col] == ".":
#                     continue
#                 elif board[row][col] in seen:
#                     return False
#                 else:
#                     seen.add(board[row][col])

#         for col in range(9):
#             seen = set()
#             for row in range(9):
#                 if board[row][col] == ".":
#                     continue
#                 elif board[row][col] in seen:
#                     return False
#                 else:
#                     seen.add(board[row][col])


#         for square in range(9):
#             seen = set()
#             for i in range(3):
#                 for j in range(3):
#                     row = (square // 3) * 3 + i
#                     col = (square % 3) * 3 + j
#                     if board[row][col] == ".":
#                         continue
#                     elif board[row][col] in seen:
#                         return False
#                     else:
#                         seen.add(board[row][col])

#         return True

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif (board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[row//3, col//3]):
                    return False
                else:
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    squares[row//3, col//3].add(board[row][col])

        return True