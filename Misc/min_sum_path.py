# https://leetcode.com/problems/minimum-path-sum/

# Recursive solution, calculates all possible paths

# class Solution(object):
#     def minPathSum(self, grid):
#         height, width = len(grid), len(grid[0])
#
#         if len(grid) == 1 and len(grid[0]) <= 1: return grid[0][0]
#
#         def traverse(row, col, total, paths):
#             total += grid[row][col]
#             if total >= paths['min']: return False
#
#             #print("Row: %d | Col:%d | Total:%d" % (row, col, total))
#             if row < height - 1:
#                 traverse(row + 1, col, total, paths)
#             if col < width - 1:
#                 traverse(row, col + 1, total, paths)
#
#             # Found the end point
#             if row == height - 1 and col == width - 1:
#                 #print("Total: %d" % total)
#                 paths['min'] = min(paths['min'], total)
#
#         paths = { 'min': 99999999 }
#         traverse(0, 0, 0, paths)
#         return paths['min']


class Solution(object):
    def minPathSum(self, grid):
        height, width = len(grid), len(grid[0])
        #print("height:%d, width:%d" % (height, width))

        if len(grid) == 1 and len(grid[0]) <= 1: return grid[0][0]

        def traverse(row = 0, col = 0, total = 0):
            #print("Row: %d | Col:%d | Total:%d" % (row, col, total))
            total += grid[row][col]


            if row == height - 1 and col == width - 1:
                #print("ENDING Total:%d" % total)
                return total #arrived at end
            else:
                down = grid[row + 1][col] if row < height - 1 else None
                right = grid[row][col + 1] if col < width - 1 else None

                if down != None and right != None:
                    if down <= right:
                        return traverse(row + 1, col, total)
                    else:
                        return traverse(row, col + 1, total)
                else:
                    if down != None and right == None:
                        return traverse(row + 1, col, total)
                    if down == None and right != None:
                        return traverse(row, col + 1, total)

        return traverse()




### tests
s = Solution()

# grid1 = [
#     [2, 4, 5, 6],
#     [3, 2, 5, 1],
#     [2, 4, 1, 3],
#     [1, 1, 3, 7]
# ]

# grid1 = [
#     [1, 2],
#     [1, 1]
# ]

# grid1 = [
#     [0, 1],
#     [1, 0]
# ]

#grid1 = [[9,1,4,8]]

#grid1 = [[1,2],[5,6],[1,1]]

grid1 = [[0,0],[0,0]]

#grid1 = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]

res = s.minPathSum(grid1)
print(res)