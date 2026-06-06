package problems.problems_2196;

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
    public TreeNode createBinaryTree(int[][] descriptions) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] descriptions = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(TreeNode.TreeNodeToArray(createBinaryTree(descriptions)));
    }
}
