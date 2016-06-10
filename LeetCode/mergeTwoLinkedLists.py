class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        current = head
        while current:
            if not l1:
                current.next = l2
                break
            if not l2:
                current.next = l1
                break
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        return head.next


s = Solution()

# h1 = ListNode(5)
# #print(h1.val)
# h1.next = (ListNode(8))
# h1.next.next = (ListNode(9))
# h1.next.next.next = (ListNode(15))
#
# h2 = ListNode(3)
# #print(h1.val)
# h2.next = (ListNode(4))
# h2.next.next = (ListNode(7))

s = Solution()

h1 = ListNode(-9)
#print(h1.val)
h1.next = (ListNode(-7))
h1.next.next = (ListNode(-3))
h1.next.next.next = (ListNode(-3))

h2 = ListNode(-7)
#print(h1.val)
h2.next = (ListNode(-7))
h2.next.next = (ListNode(-6))


#s.mergeTwoLists(h1, h2)


head = s.mergeTwoLists(h1, h2)
while head:
    print head.val
    head = head.next