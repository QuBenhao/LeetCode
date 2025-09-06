package problems.problems_1022;

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
    public int sumRootToLeaf(TreeNode root) {
        return root == null ? 0 : dfs(root, 0);
    }

    private int dfs(TreeNode node, int cur) {
        cur <<= 1;
        cur += node.val;
        if (node.left == null && node.right == null) {
            return cur;
        }
        int ans = 0;
        if (node.left != null) {
            ans += dfs(node.left, cur);
        }
        if (node.right != null) {
            ans += dfs(node.right, cur);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
        return JSON.toJSON(sumRootToLeaf(root));
    }
}
