"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""

import math

class Solution(object):
    def isSymmetric(self, root):
        def traverse(left, right):
            if left and right:
                return left.val == right.val and traverse(left.left, right.right) and traverse(left.right, right.left)
            else:
                return left == right
        return traverse(root, root)