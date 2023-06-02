# https://leetcode.com/problems/valid-sudoku/

# Approach 1 with integer hashing
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        colMap = {i : [] for i in range(COLS)}
        sectionMap = {}

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == '.':
                    continue
                if board[i].count(board[i][j]) > 1:
                    return False
                if board[i][j] in colMap[j]:
                    return False
                colMap[j].append(board[i][j])

                sectionCode = (i//3, j//3)
                print(sectionCode)
                sectionMap[sectionCode] = sectionMap.get(sectionCode, [])
                if board[i][j] in sectionMap[sectionCode]:
                    return False
                else:
                    sectionMap[sectionCode].append(board[i][j])

        return True

# approach two with string hashing
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        seen = {}

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == '.':
                    continue

                rowString = 'r' + str(i) + board[i][j]
                if rowString in seen:
                    return False
                else:
                    seen[rowString] = None
                
                colString = 'c' + str(j) + board[i][j]
                if colString in seen:
                    return False
                else:
                    seen[colString] = None
                
                sectionString = 's' + str(i//3) + str(j//3) + board[i][j]
                if sectionString in seen:
                    return False
                seen[sectionString] = None
        
        return True