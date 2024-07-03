package problems.problems_1932;

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
    public TreeNode canMerge(List<TreeNode> trees) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<TreeNode> trees = jsonArrayToTreeNodeList(inputJsonValues[0]);
        return JSON.toJSON(TreeNode.TreeNodeToArray(canMerge(trees)));
    }
}
