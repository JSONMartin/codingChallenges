"""
# https://leetcode.com/problems/sum-of-left-leaves/#/description
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        def traverse(node, total = 0):
            if not node or node == None:
                return total

            if node.left:
                if node.left.left or node.left.left == None and node.left.right != None:
                    total = traverse(node.left, total)
                else:
                    total = traverse(node.left, total + node.left.val)
            if node.right:
                total = traverse(node.right, total)
            return total

        return traverse(root)