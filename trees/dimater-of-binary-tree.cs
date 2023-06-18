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
    private int result = 0;

    public int DiameterOfBinaryTree(TreeNode root) {
        if(root == null) return 0;

        DfsMaxEdgePath(root);
        return result;
    }

    private int DfsMaxEdgePath(TreeNode root) {
        if (root == null) return -1;

        int leftMaxEdges = 1 + DfsMaxEdgePath(root.left);
        int rightMaxEdges = 1 + DfsMaxEdgePath(root.right);
        result = Math.Max(result, leftMaxEdges + rightMaxEdges);

        return Math.Max(leftMaxEdges, rightMaxEdges);
    }
}