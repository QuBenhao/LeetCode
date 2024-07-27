package problems.problems_236;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import qubhjava.models.TreeNode;

public class Solution extends BaseSolution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) {
            return root;
        }
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) {
            return root;
        }
        return left == null ? right : left;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int targetVal1 = Integer.parseInt(inputJsonValues[1]);
		int targetVal2 = Integer.parseInt(inputJsonValues[2]);
		TreeNode[] nodes = TreeNode.ArrayToTreeNodeWithTargets(inputJsonValues[0], targetVal1, targetVal2);
		TreeNode root = nodes[0], p = nodes[1], q = nodes[2];
        return JSON.toJSON(TreeNode.TreeNodeToArray(lowestCommonAncestor(root, p, q)));
    }
}
