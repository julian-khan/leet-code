# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

#Time complexity O(n), space complexity O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        backPointer = dummy = ListNode(0, head)
        frontPointer = head

        for i in range(n):
            frontPointer = frontPointer.next

        while frontPointer:
            frontPointer = frontPointer.next
            backPointer = backPointer.next

        backPointer.next = backPointer.next.next

        return dummy.next