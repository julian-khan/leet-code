# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        frontPointer = backPointer = head

        counter = 0
        for i in range(n):
            frontPointer = frontPointer.next
            counter += 1

        if not frontPointer and counter == n:
            return head.next
        if not frontPointer:
            return None
        if not frontPointer.next and n == counter + 1:
            return head.next

        
        while frontPointer:

            if not frontPointer.next:
                backPointer.next = backPointer.next.next
                break

            frontPointer = frontPointer.next
            backPointer = backPointer.next
        
        return head