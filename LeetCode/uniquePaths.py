class Solution(object):
    def uniquePaths(self, rows, cols):
        END_POINT = (rows - 1, cols - 1)

        # Dynamic programming solution
        def findPath():
            dp = [[1 for x in range(cols)] for x in range(rows)]

            for row in range(1, rows):
                for col in range(1, cols):
                    dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
            
            return dp[-1][-1]

        return findPath()

        # Memoized Solution
        memo = {}
        def findPathMemoization(row, col):
            KEY = str(row) + "-" + str(col)
            if KEY in memo:
                return memo[KEY]

            totals = 0

            # Base Case
            if (row, col) == END_POINT:
                return 1

            if row + 1 < rows:
                totals += findPath(row + 1, col)
            if col + 1 < cols:
                totals += findPath(row, col + 1)
            
            memo[KEY] = totals
            return memo[KEY]
        
        return findPath(0, 0)




### SOLUTIONS
# res = Solution().uniquePaths(3, 7)
# res = Solution().uniquePaths(3, 3)
res = Solution().uniquePaths(23, 12)
print(res)