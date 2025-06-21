package problems.problems_2385;

import com.alibaba.fastjson.JSON;
import java.util.*;

import javafx.util.Pair;
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

    private Pair<Integer, Boolean> dfs(TreeNode node, int start) {
        if (node == null) return new Pair<>(0, false);
        Pair<Integer, Boolean> left = dfs(node.left, start);
        Pair<Integer, Boolean> right = dfs(node.right, start);
        if (node.val == start) {
            ans = Math.max(ans, Math.max(left.getKey(), right.getKey()));
            return new Pair<>(0, true);
        }
        int d = 1;
        boolean found = left.getValue() || right.getValue();
        if (found) {
            ans = Math.max(ans, left.getKey() + right.getKey() + 1);
            if (left.getValue()) {
                d += left.getKey();
            } else {
                d += right.getKey();
            }
        } else {
            d += Math.max(left.getKey(), right.getKey());
        }
        return new Pair<>(d, found);
    }

    public int amountOfTime(TreeNode root, int start) {
        ans = 0;
        dfs(root, start);
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
		int start = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(amountOfTime(root, start));
    }
}
