package problems.problems_LCR_046;

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
    public List<Integer> rightSideView(TreeNode root) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
        return JSON.toJSON(rightSideView(root));
    }
}
