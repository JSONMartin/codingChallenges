"""
# https://leetcode.com/problems/binary-tree-preorder-traversal/#/description
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # Iterative solution
    def preorderTraversal(self, root):
        visited = []
        queue = [root] if root and root != None else []
        
        while len(queue) > 0:
            node = queue.pop()
            visited.append(node.val)
            if node.right: queue.append(node.right)
            if node.left: queue.append(node.left)

        return visited

    # Recursive solution
    def preorderTraversalRecursive(self, root):
        visited = []

        def traverse(node):
            if not node: return
            visited.append(node.val)
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)

        traverse(root)
        return visited
        