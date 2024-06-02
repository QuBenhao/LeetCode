package problems.problems_226;

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
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return root;
        }
        TreeNode tmpRight = invertTree(root.left);
        root.left = invertTree(root.right);
        root.right = tmpRight;
        return root;
    }

    @Override
    public Object solve(String[] values) {
        TreeNode root = TreeNode.ArrayToTreeNode(values[0]);
        return JSON.toJSON(TreeNode.TreeNodeToArray(invertTree(root)));
    }
}
