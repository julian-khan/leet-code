// https://leetcode.com/problems/diameter-of-binary-tree/

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
    public int DiameterOfBinaryTree(TreeNode root) {
        if(root == null) return 0;

        int leftMax = DfsMaxEdgePath(root.left);
        int rightMax = DfsMaxEdgePath(root.right);

        var recursiveLeft = DiameterOfBinaryTree(root.left);
        var recursiveRight = DiameterOfBinaryTree(root.right);

        return Math.Max(leftMax + rightMax, Math.Max(recursiveLeft, recursiveRight));
    }

    private int DfsMaxEdgePath(TreeNode root) {
        if (root == null) return 0;

        int longestEdge = Math.Max(DfsMaxEdgePath(root.left), DfsMaxEdgePath(root.right));
        return 1 + longestEdge;
    }
}