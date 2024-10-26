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
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int targetVal1 = Integer.parseInt(inputJsonValues[1]);
		TreeNode[] nodes = TreeNode.ArrayToTreeNodeWithTargets(inputJsonValues[0], targetVal1);
		TreeNode root = nodes[0], p = nodes[1];
        return JSON.toJSON(TreeNode.TreeNodeToArray(inorderSuccessor(root, p)));
    }
}
