# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = mergedList = ListNode()

        while len(lists) > 1:
            merged = []
            i = 0

            while i < len(lists):
                firstList = lists[i]
                secondList = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoLists(firstList, secondList))
                i += 2
            lists = merged

        return lists[0] if lists else None


    def mergeTwoLists(self, list1, list2):
        curr = dummy = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        return dummy.next
