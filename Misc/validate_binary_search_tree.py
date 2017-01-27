# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root, min=float('-inf'), max=float('inf')):
        if not root: return True
        else:
            return min < root.val < max and \
                   self.isValidBST(root.left, min, root.val) and \
                   self.isValidBST(root.right, root.val, max)


class SolutionTwo(object):
    def isValidBST(self, root):
        result = []

        def serializeTree(root, result):
            if root and root.left:
                serializeTree(root.left, result)
            if root != None and root.val != None:
                result.append(root.val)
            if root and root.right:
                serializeTree(root.right, result)
            return result

        result = serializeTree(root, result)

        for i in range(len(result) - 1):
            if result[i] >= result[i+1]: return False

        return True

### TESTS

two = TreeNode(2)



one = TreeNode(1)
three = TreeNode(3)

two.left = one
two.right = three

#res = Solution().isValidBST(two)

#test = TreeNode(1)
#res = Solution().isValidBST(test)



ten = TreeNode(10)
five = TreeNode(5)
fifteen = TreeNode(15)
six = TreeNode(6)
twenty = TreeNode(20)

ten.left = five
ten.right = fifteen
fifteen.left = six
fifteen.right = twenty

#res = Solution().isValidBST(ten)


zero = TreeNode(0)
negone = TreeNode(-1)

zero.right = negone
res = Solution().isValidBST(zero)

print(res)


