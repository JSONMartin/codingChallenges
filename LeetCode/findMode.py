# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#from collections import Counter

class Solution(object):
    def findMode(self, root):
        seen = {}

        def traverse(node):
            if not node: return
            seen[node.val] = seen.get(node.val, 0) + 1
            traverse(node.left)
            traverse(node.right)
        
        try:
            traverse(root)
            frequency = sorted(seen.items(), key=lambda x: x[1], reverse=True)
            results = [frequency[0][0]]

            for f in frequency[1:]:
                if f[1] == frequency[0][1]: results.append(f[0])
                else: break

            return results
        except:
            return []
