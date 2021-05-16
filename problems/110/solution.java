class Solution {
    public boolean isBalanced(TreeNode root) {
        int r = depth(root,0);
        if(r==-1)
            return false;
        return true;
    }

    private int depth(TreeNode node, int d){
        if(node == null)
            return d;
        d += 1;
        int left = depth(node.left, d);
        if(left == -1)
            return left;
        int right = depth(node.right, d);
        if(right == -1)
            return right;
        if(Math.abs(left-right)>1)
            return -1;
        return Math.max(left,right);
    }
}


/**
 * Definition for a binary tree node.
 */
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
