# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is not None and q is not None: #Both p and q are valid, so check each of them
            # Return the combination of checking all the left side and the combination of checking all of the right side
            return ( (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) )


        return False # One is empty, one is not, so return false