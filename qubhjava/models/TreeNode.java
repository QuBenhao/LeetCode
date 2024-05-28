package qubhjava.models;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Queue;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;

    public TreeNode() {}
    public TreeNode(int val) { this.val = val; }
    public TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public static TreeNode ArrayToTreeNode(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        if (jsonArray.isEmpty()) {
            return null;
        }
        if (jsonArray.get(0) == null) {
            return null;
        }
        TreeNode root = new TreeNode(jsonArray.getIntValue(0));
        int isLeft = 1;
        Queue<TreeNode> queue = new ArrayDeque<>();
        TreeNode currNode = root;
        for (int i = 1; i < jsonArray.size(); i++) {
            TreeNode node;
            if (jsonArray.get(i) == null) {
                node = null;
            } else {
                node = new TreeNode(jsonArray.getIntValue(i));
            }
            queue.offer(node);
            assert currNode != null;
            if (isLeft == 1) {
                currNode.left = node;
            } else {
                currNode.right = node;
                currNode = queue.poll();
            }
            isLeft ^= 1;
        }
        return root;
    }

    public JSONArray TreeNodeToArray() {
        JSONArray jsonArray = new JSONArray();
        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.offer(this);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node != null) {
                jsonArray.add(node.val);
                queue.offer(node.left);
                queue.offer(node.right);
            } else {
                jsonArray.add(null);
            }
        }
        while (!jsonArray.isEmpty() && jsonArray.get(jsonArray.size() - 1) == null) {
            jsonArray.remove(jsonArray.size() - 1);
        }
        return jsonArray;
    }
}
