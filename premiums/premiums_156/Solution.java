package premiums.premiums_156;

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
    public TreeNode upsideDownBinaryTree(TreeNode root) {
        TreeNode node = null, left = root, right = null;
        while (left != null) {
            TreeNode newLeft = left.left, newRight = left.right;
            left.left = right;
            left.right = node;
            node = left;
            left = newLeft;
            right = newRight;
        }
        return node;
    }

    @Override
    public Object solve(String[] values) {
        TreeNode root = TreeNode.ArrayToTreeNode(values[0]);
        return JSON.toJSON(TreeNode.TreeNodeToArray(upsideDownBinaryTree(root)));
    }
}
