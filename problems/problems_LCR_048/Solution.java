package problems.problems_LCR_048;

import com.alibaba.fastjson.JSON;

import java.util.*;

import qubhjava.BaseSolution;
import qubhjava.models.TreeNode;


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */
class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        preorder(root, sb);
        while (sb.charAt(sb.length() - 1) == '#' && sb.charAt(sb.length() - 2) == ',') {
            sb.delete(sb.length() - 2, sb.length());
        }
        while (sb.charAt(sb.length() - 1) == ',') {
            sb.deleteCharAt(sb.length() - 1);
        }
        return sb.toString();
    }

    private void preorder(TreeNode root, StringBuilder sb) {
        if (root == null) {
            sb.append("#,");
            return;
        }
        sb.append(root.val).append(",");
        preorder(root.left, sb);
        preorder(root.right, sb);
    }

    private int idx;

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.isEmpty()) {
            return null;
        }
        String[] nodes = data.split(",");
        idx = 0;
        return buildTree(nodes);
    }

    private TreeNode buildTree(String[] nodes) {
        if (idx >= nodes.length || nodes[idx].equals("#")) {
            idx++;
            return null;
        }
        TreeNode root = new TreeNode(Integer.parseInt(nodes[idx++]));
        root.left = buildTree(nodes);
        root.right = buildTree(nodes);
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
        Codec ser = new Codec();
        Codec der = new Codec();
        TreeNode ans = der.deserialize(ser.serialize(root));
        return JSON.toJSON(TreeNode.TreeNodeToArray(ans));
    }
}
