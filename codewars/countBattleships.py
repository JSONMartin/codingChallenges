class Solution(object):
    def countBattleships(self, board):
        board = [list(b) for b in board]
        rows, cols = len(board), len(board[0])
        shipCount = 0

        isShip = lambda row, col: board[row][col] == 'X'
        def markShip(row, col):
            if board[row][col] == 'X': board[row][col] = '!'
            if row - 1 > 0 and isShip(row - 1, col): markShip(row - 1, col)
            if row + 1 < rows and isShip(row + 1, col): markShip(row + 1, col)
            if col - 1 > 0 and isShip(row, col - 1): markShip(row, col - 1)
            if col + 1 < cols and isShip(row, col + 1): markShip(row, col + 1)

        for row in range(rows):
            for col in range(cols):
                if isShip(row, col):
                    markShip(row, col)
                    shipCount += 1

        return shipCount




######
#Solution
b = ["X..X","...X","...X"]
#
Solution().countBattleships(b)