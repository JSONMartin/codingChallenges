# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Solution with two pointers, no extra space
    def detectCycle(self, head):
        try:
            a, b = head.next, head.next.next
            # Walk A and B pointers until they meet. B goes twice as fast as A.
            while a != b:
                a = a.next
                b = b.next.next
            
            # Count from the start to when the pointers meet
            start = head
            while start != a:
                start = start.next
                a = a.next
            
            return a
        except:
            return None

    # Solution with One pointer, extra space
    def detectCycleExtraSpace(self, head):
        visited = {}

        curNode = head
        try:
            while curNode.next:
                if curNode.next in visited:
                    return curNode.next
                else:
                    visited[curNode] = True
                    curNode = curNode.next
        except:
            return None
            