# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, total):
        counter = 0

        def findPath(node, curTotal = 0):
            if node:
                curTotal += node.val
                if curTotal == total: counter += 1
            else:
                return

            findPath(node.left, curTotal)
            findPath(node.right, curTotal)

        findPath(root)

        # print(paths)
        # print([sum(path) for path in paths])

        # for path in paths:
        #     for i in range(len(path)):
        #         print(path[i:])
        #         if sum(path[i:]) == total: counter += 1

        print(counter)
        return counter

    # TLE
    # def pathSum(self, root, total):
    #     paths = []
    #
    #     def findPath(node, path = []):
    #         if node:
    #             path.append(node.val)
    #             paths.append(path[:])
    #         else:
    #             return
    #
    #         findPath(node.left, path[:])
    #         findPath(node.right, path[:])
    #         #if node.left: findPath(node.left, path[:])
    #         #if node.right: findPath(node.left, path[:])
    #
    #
    #
    #     findPath(root)
    #
    #     print(paths)
    #     print([sum(path) for path in paths])
    #
    #     counter = 0
    #
    #     for path in paths:
    #         for i in range(len(path)):
    #             print(path[i:])
    #             if sum(path[i:]) == total: counter += 1
    #
    #     return counter


    # def pathSum(self, root, sum):
    #     paths = []
    #
    #     def findPath(node, path = []):
    #         if node and node.val:
    #             path.append(node.val)
    #         else:
    #             paths.append(path[:])
    #             return
    #
    #         findPath(node.left, path[:])
    #         findPath(node.right, path[:])
    #         #if node.left: findPath(node.left, path[:])
    #         #if node.right: findPath(node.left, path[:])
    #
    #     findPath(root)
    #
    #     print(paths)


set([1, 2, 3])
