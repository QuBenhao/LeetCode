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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
		TreeNode subRoot = TreeNode.ArrayToTreeNode(inputJsonValues[1]);
        return JSON.toJSON(isSubtree(root, subRoot));
    }
}
