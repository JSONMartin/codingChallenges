# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        try:
            lastNode = head
            curNode = head.next

            while curNode:
                curNode.prev = lastNode
                lastNode = curNode
                curNode = curNode.next
            curNode = lastNode

            while n >= 1:
                if not hasattr(curNode, 'prev'): return head.next # In case number passed is the first
                curNode = curNode.prev
                n -= 1

            removed = curNode.next
            removed.prev.next = removed.next
            return head
        except Exception as E:
            return []

### TESTING ###

##### TEST NODES
testNode = ListNode(1)
testNode.next = ListNode(2)

res = Solution().removeNthFromEnd(testNode, 2)
#print(res.val)
print(res.val)