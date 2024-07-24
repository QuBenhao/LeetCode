package qubhjava.models;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;

import java.util.*;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;

    public TreeNode() {
    }

    public TreeNode(int val) {
        this.val = val;
    }

    public TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public static TreeNode ArrayToTreeNode(String jsonString) {
        return ArrayToTreeNodeWithTargets(jsonString)[0];
    }

    public static TreeNode[] ArrayToTreeNodeWithTargets(String jsonString, int... targets) {
        TreeNode[] ans = new TreeNode[targets.length + 1];
        Arrays.fill(ans, null);
        JSONArray jsonArray = JSON.parseArray(jsonString);
        if (jsonArray.isEmpty() || jsonArray.getFirst() == null) {
            return ans;
        }
        TreeNode root = new TreeNode(jsonArray.getIntValue(0));
        int isLeft = 1;
        Queue<TreeNode> queue = new ArrayDeque<>();
        TreeNode currNode = root;
        ans[0] = root;
        for (int i = 0; i < targets.length; i++) {
            if (root.val == targets[i]) {
                ans[i + 1] = root;
            }
        }
        for (int i = 1; i < jsonArray.size(); i++) {
            TreeNode node;
            if (jsonArray.get(i) == null) {
                node = null;
            } else {
                node = new TreeNode(jsonArray.getIntValue(i));
                for (int j = 0; j < targets.length; j++) {
                    if (node.val == targets[j]) {
                        ans[j + 1] = node;
                    }
                }
            }
            if (isLeft == 1) {
                if (node != null) {
                    assert currNode != null;
                    currNode.left = node;
                    queue.offer(node);
                }
            } else {
                if (node != null) {
                    assert currNode != null;
                    currNode.right = node;
                    queue.offer(node);
                }
                currNode = queue.poll();
            }
            isLeft ^= 1;
        }
        return ans;
    }

    public static JSONArray TreeNodeToArray(TreeNode root) {
        JSONArray jsonArray = new JSONArray();
        List<TreeNode> list = new ArrayList<>();
        list.add(root);
        for (int idx = 0; idx < list.size(); idx++) {
            TreeNode node = list.get(idx);
            if (node != null) {
                jsonArray.add(node.val);
                list.add(node.left);
                list.add(node.right);
            } else {
                jsonArray.add(null);
            }
        }
        while (!jsonArray.isEmpty() && jsonArray.getLast() == null) {
            jsonArray.removeLast();
        }
        return jsonArray;
    }
}
