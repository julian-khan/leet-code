# https://leetcode.com/problems/copy-list-with-random-pointer/

#Time complexity O(n), space complexity O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        origToCopied = {}

        curr = head
        while curr:
            origToCopied[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        curr = head
        while curr:
            origToCopied[curr].next = origToCopied.get(curr.next, None)
            origToCopied[curr].random = origToCopied.get(curr.random, None)
            curr = curr.next
        
        return origToCopied[head]