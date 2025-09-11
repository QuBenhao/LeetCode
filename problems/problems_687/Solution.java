package problems.problems_687;

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
    int ans;
    public int longestUnivaluePath(TreeNode root) {
        ans = 0;
        dfs(root);
        return ans;
    }

    private int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int curAns = 0, cur = 0, left = dfs(node.left), right = dfs(node.right);
        if (node.left != null && node.left.val == node.val) {
            curAns = left + 1;
            cur += left + 1;
        }
        if (node.right != null && node.right.val == node.val) {
            curAns = Math.max(curAns, right + 1);
            cur += right + 1;
        }
        ans = Math.max(ans, cur);
        return curAns;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
        return JSON.toJSON(longestUnivaluePath(root));
    }
}
