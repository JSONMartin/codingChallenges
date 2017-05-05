# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/#/description

"""
Total Accepted: 103515
Total Submissions: 356301
Difficulty: Medium
Contributor: LeetCode
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

Subscribe to see which companies asked this question.
"""
import sys
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # O(n) runtime (1 pass through array), O(1) space
    def deleteDuplicates(self, head):
        dummy = ListNode('dummy')
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.next and current.next.val == current.next.next.val:
                unique = current.next
                while unique and unique.val == current.next.val:
                    unique = unique.next
                current.next = unique
            else:
                current = current.next
        
        return dummy.next
    
    # O(n) runtime (2 passes through array), O(n) space
    def deleteDuplicatesDict(self, head):
        counter = {}
        
        # Count items in list
        current = head
        while current:
            counter[current.val] = counter.get(current.val, 0) + 1
            current = current.next
        
        # Create new list, only adding those that have a count of 1
        current = head
        
        dummy = ListNode('dummy')
        currentReturn = dummy

        while current:
            if counter[current.val] == 1:
                currentReturn.next = ListNode(current.val)
                currentReturn = currentReturn.next
            current = current.next

        dummy = dummy.next
        return dummy



### TESTS
singleTest = ListNode(1)
#doubleTest = ListNode(1); doubleTest.next = ListNode(1)
doubleTest = ListNode(1); doubleTest.next = ListNode(2)
tripleTest = ListNode(1); tripleTest.next = ListNode(2); tripleTest.next.next = ListNode(2)
quadTest = ListNode(1); quadTest.next = ListNode(2); quadTest.next.next = ListNode(3); quadTest.next.next.next = ListNode(3)

#res = Solution().deleteDuplicates(doubleTest)
#res = Solution().deleteDuplicates(tripleTest)
res = Solution().deleteDuplicates(quadTest)
print(res)
print(vars(res))