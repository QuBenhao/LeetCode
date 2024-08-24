package problems.problems_105;

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
    public TreeNode buildTree(int[] preorder, int[] inorder) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] preorder = jsonArrayToIntArray(inputJsonValues[0]);
		int[] inorder = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(TreeNode.TreeNodeToArray(buildTree(preorder, inorder)));
    }
}
