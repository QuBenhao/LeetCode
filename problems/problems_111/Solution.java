package problems.problems_111;

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
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (root.left == null && root.right == null) {
            return 1;
        }
        int ans = Integer.MAX_VALUE;
        if (root.left != null) {
            ans = Math.min(ans, minDepth(root.left) + 1);
        }
        if (root.right != null) {
            ans = Math.min(ans, minDepth(root.right) + 1);
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        TreeNode root = TreeNode.ArrayToTreeNode(values[0]);
        return JSON.toJSON(minDepth(root));
    }
}
