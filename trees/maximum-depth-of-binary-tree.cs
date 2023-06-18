# https://leetcode.com/problems/maximum-depth-of-binary-tree/

//Time complexity O(n);
//Space complexity O(n) (In the worst-case, a binary tree resembles a linked list and therefore its
//maximum depth can be O(n)).

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int MaxDepth(TreeNode root) {
        return DfsCounter(root);
    
    }

    private int DfsCounter(TreeNode root, int counter = 0) {
        if (root == null) return counter;
        
        return Math.Max(DfsCounter(root.left, counter + 1), DfsCounter(root.right, counter + 1));
    }
}