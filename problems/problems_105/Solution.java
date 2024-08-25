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
        if (preorder.length == 0) {
            return null;
        }
        int rooVal = preorder[0];
        TreeNode root = new TreeNode(rooVal);
        int index = 0;
        for (int i = 0; i < inorder.length; i++) {
            if (inorder[i] == rooVal) {
                index = i;
                break;
            }
        }
        int[] leftPreorder = Arrays.copyOfRange(preorder, 1, index + 1);
        int[] rightPreorder = Arrays.copyOfRange(preorder, index + 1, preorder.length);
        int[] leftInorder = Arrays.copyOfRange(inorder, 0, index);
        int[] rightInorder = Arrays.copyOfRange(inorder, index + 1, inorder.length);
        root.left = buildTree(leftPreorder, leftInorder);
        root.right = buildTree(rightPreorder, rightInorder);
        return root;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] preorder = jsonArrayToIntArray(inputJsonValues[0]);
		int[] inorder = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(TreeNode.TreeNodeToArray(buildTree(preorder, inorder)));
    }
}
