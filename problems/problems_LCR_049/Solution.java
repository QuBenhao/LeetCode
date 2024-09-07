package problems.problems_LCR_049;

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
    public int sumNumbers(TreeNode root) {
        ans = 0;
        dfs(root, 0);
        return ans;
    }

    private void dfs(TreeNode root, int sum) {
        if (root == null) {
            return;
        }
        sum = sum * 10 + root.val;
        if (root.left == null && root.right == null) {
            ans += sum;
            return;
        }
        dfs(root.left, sum);
        dfs(root.right, sum);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
        return JSON.toJSON(sumNumbers(root));
    }
}
