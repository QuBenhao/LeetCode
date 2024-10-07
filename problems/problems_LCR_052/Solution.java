package problems.problems_LCR_052;

import java.util.ArrayList;
import java.util.List;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;
import qubhjava.models.TreeNode;

public class Solution extends BaseSolution {
    private void inorder(TreeNode node, List<Integer> vals) {
        if (node == null) {
            return;
        }
        inorder(node.left, vals);
        vals.add(node.val);
        inorder(node.right, vals);
    }

    public TreeNode increasingBST(TreeNode root) {
        List<Integer> vals = new ArrayList<>();
        inorder(root, vals);

        TreeNode dummyNode = new TreeNode(0);
        TreeNode currNode = dummyNode;
        for (int val : vals) {
            currNode.right = new TreeNode(val);
            currNode = currNode.right;
        }
        return dummyNode.right;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
        return JSON.toJSON(TreeNode.TreeNodeToArray(increasingBST(root)));
    }
}
