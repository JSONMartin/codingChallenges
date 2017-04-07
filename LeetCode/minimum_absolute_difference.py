# https://leetcode.com/submissions/detail/98340498/
class Solution(object):
    # Beats 85.77% of submissions
    def getMinimumDifference(self, root):
        values, queue = [], [root]

        while len(queue) > 0:
            curNode = queue.pop()
            if curNode.left: queue.append(curNode.left)
            if curNode.right: queue.append(curNode.right)
            values.append(curNode.val)

        values.sort()
        differences = [abs(values[i + 1] - values[i]) for i in range(len(values) - 1)]

        return min(differences)





        # traverse left


# s = Solution()
# s.getMinimumDifference()
import json
json.dumps
