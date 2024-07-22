package problems.problems_543;

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
    private int ans;
    private int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = dfs(node.left), right = dfs(node.right);
        ans = Math.max(ans, left + right);
        return Math.max(left, right) + 1;
    }
    public int diameterOfBinaryTree(TreeNode root) {
        ans = 0;
        dfs(root);
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
        return JSON.toJSON(diameterOfBinaryTree(root));
    }
}
