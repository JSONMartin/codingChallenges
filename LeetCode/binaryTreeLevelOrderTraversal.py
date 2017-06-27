"""
# https://leetcode.com/problems/binary-tree-level-order-traversal/#/description

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        
        q = [(root, 0)] # (node, level)
        results = []

        while len(q) > 0:
            curNode, curLevel = q.pop(0)

            try:
                results[curLevel] += [curNode.val]
            except:
                results.append([curNode.val])
            
            if curNode.left:
                q.append((curNode.left, curLevel + 1))
            if curNode.right:
                q.append((curNode.right, curLevel + 1))
        
        return results

###

