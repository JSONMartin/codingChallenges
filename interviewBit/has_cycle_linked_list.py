# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        cur = head
        if not head: return False
        
        if head.next and head.next.next: next = head.next.next
        else: next=head.next
        
        while next:
            #print("Cur.val:%d, next.val:%d" % (cur.val, next.val))
            if cur.val == next.val: return True
            
            if next.next and next.next.next: 
                cur = cur.next
                next = next.next.next
            else: 
                cur = cur.next
                next=next.next
        
        return False

"""
Solution to linked lists hasCycle using constant space
"""