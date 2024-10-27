package problems.problems_LCR_053;

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
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (p.right != null) {
            p = p.right;
            while (p.left != null) {
                p = p.left;
            }
            return p;
        }
        Stack<TreeNode> stack = new Stack<>();
        TreeNode pre = null;
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if (pre == p) {
                return root;
            }
            pre = root;
            root = root.right;
        }
        return null;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int targetVal1 = Integer.parseInt(inputJsonValues[1]);
		TreeNode[] nodes = TreeNode.ArrayToTreeNodeWithTargets(inputJsonValues[0], targetVal1);
		TreeNode root = nodes[0], p = nodes[1];
        return JSON.toJSON(TreeNode.TreeNodeToArray(inorderSuccessor(root, p)));
    }
}
