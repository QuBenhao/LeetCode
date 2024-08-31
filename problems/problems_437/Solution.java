package problems.problems_437;

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
    public int pathSum(TreeNode root, int targetSum) {
        Map<Long, Integer> counter = new HashMap<>();
        counter.put(0L, 1);
        return dfs(root, counter, 0, targetSum);
    }

    private int dfs(TreeNode node, Map<Long, Integer> counter, long curSum, int targetSum) {
        if (node == null) {
            return 0;
        }
        curSum += node.val;
        int res = counter.getOrDefault(curSum - targetSum, 0);
        counter.put(curSum, counter.getOrDefault(curSum, 0) + 1);
        res += dfs(node.left, counter, curSum, targetSum) + dfs(node.right, counter, curSum, targetSum);
        counter.put(curSum, counter.get(curSum) - 1);
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
		int targetSum = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(pathSum(root, targetSum));
    }
}
