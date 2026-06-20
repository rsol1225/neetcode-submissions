class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Understanding:
        #Each row must contain the digits 1-9 without duplicates 
        #Each column must contain the digits 1-9 withot duplicates
        #Each square must contain the digits 1-9 without duplicates
        
        #only digits can violate constraints
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] ==".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
                #are there duplicates
                #if the board is empty
        
        return True
