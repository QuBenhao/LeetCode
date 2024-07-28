package qubhjava.models.node.next;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

// Definition for a Node.
public class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {
    }

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
    
    public static Node ArrayToTreeNodeNext(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        if (jsonArray.isEmpty() || jsonArray.getFirst() == null) {
            return null;
        }
        Node root = new Node(jsonArray.getIntValue(0));
        int isLeft = 1;
        Queue<Node> queue = new ArrayDeque<>();
        Node currNode = root;
        for (int i = 1; i < jsonArray.size(); i++) {
            Node node;
            if (jsonArray.get(i) == null) {
                node = null;
            } else {
                node = new Node(jsonArray.getIntValue(i));
            }
            if (isLeft != 1) {
                if (node != null) {
                    assert currNode != null;
                    currNode.right = node;
                    queue.offer(node);
                }
                currNode = queue.poll();
            } else {
                if (node != null) {
                    assert currNode != null;
                    currNode.left = node;
                    queue.offer(node);
                }
            }
            isLeft ^= 1;
        }
        return root;
    }

    public static JSONArray TreeNodeNextToArray(Node root) {
        JSONArray jsonArray = new JSONArray();
        if (root == null) {
            return jsonArray;
        }
        Node head = root;
        while (head != null) {
            Node cur = head, nextHead = null;
            while (cur != null) {
                if (nextHead == null) {
                    nextHead = cur.left != null ? cur.left : cur.right;
                }
                jsonArray.add(cur.val);
                cur = cur.next;
            }
            jsonArray.add(null);
            head = nextHead;
        }
        return jsonArray;
    }
};