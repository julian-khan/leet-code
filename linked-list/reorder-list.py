# https://leetcode.com/problems/reorder-list/

# O(n) time complexity, O(1) space complexity

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Find the middle of the list
        fast = slow = head

        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        
        #Ensure that the left and right halves of the linked-list end with a null pointer
        curr = slow.next
        slow.next = None
        prev = None

        # Reverse the right half of the list
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        right = prev
        left = head

        # Merge the lists
        while right:
            nextLeft, nextRight = left.next, right.next

            left.next = right
            right.next = nextLeft

            left, right = nextLeft, nextRight

        return head