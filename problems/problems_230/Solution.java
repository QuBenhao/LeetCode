package problems.problems_230;

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
    private void inorder(TreeNode root, List<Integer> res) {
        if (root == null) {
            return;
        }
        inorder(root.left, res);
        res.add(root.val);
        inorder(root.right, res);
    }

    public int kthSmallest(TreeNode root, int k) {
        List<Integer> res = new ArrayList<>();
        inorder(root, res);
        return res.get(k - 1);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(kthSmallest(root, k));
    }
}
