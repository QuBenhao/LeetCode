package problems.problems_572;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import qubhjava.models.TreeNode;

public class Solution extends BaseSolution {
    private boolean dfs(TreeNode root, TreeNode subRoot, boolean mustMatch) {
        if (root == null || subRoot == null) {
            return root == subRoot;
        }
        if (root.val == subRoot.val && dfs(root.left, subRoot.left, true) && dfs(root.right, subRoot.right, true)) {
            return true;
        }
        if (mustMatch) {
            return false;
        }
        return dfs(root.left, subRoot) || dfs(root.right, subRoot);
    }
    private boolean dfs(TreeNode root, TreeNode subRoot) {
        return dfs(root, subRoot, false);
    }
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        return dfs(root, subRoot);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
		TreeNode subRoot = TreeNode.ArrayToTreeNode(inputJsonValues[1]);
        return JSON.toJSON(isSubtree(root, subRoot));
    }
}
