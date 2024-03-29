// https://leetcode.com/problems/reverse-nodes-in-k-group/

//Time complexity of O(n), space complexity of O(1)

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ReverseKGroup(ListNode head, int k) {
        var dummy = new ListNode();
        dummy.next = head;
        
        var prevGroup = dummy;
        var nextGroup = dummy;

        while(true)
        {
            var kthNode = getKth(prevGroup, k);
            
            if (kthNode == null) break;

            nextGroup = kthNode.next;

            var prev = nextGroup;
            var curr = prevGroup.next;

            while(curr != nextGroup)
            {
                var next = curr.next;
                curr.next = prev;
                prev = curr;
                curr = next;
            }

            var temp = prevGroup.next;
            prevGroup.next = kthNode;
            prevGroup = temp;
        }
        return dummy.next;
        
    }

    private ListNode getKth(ListNode prevNode, int k) 
    {
        ListNode curr = prevNode;

        while (curr != null && k > 0)
        {
            curr = curr.next;
            k -= 1;
        }
        return curr;
    }
}