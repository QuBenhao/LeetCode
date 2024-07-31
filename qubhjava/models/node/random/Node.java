package qubhjava.models.node.random;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;

import java.util.HashMap;
import java.util.Map;

// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }

    public static Node JsonArrayToNodeRandom(String jsonString) {
        JSONArray jsonArray = JSON.parseArray(jsonString);
        if (jsonArray.isEmpty() || jsonArray.getFirst() == null) {
            return null;
        }
        Node[] nodes = new Node[jsonArray.size()];
        Node last = null;
        for (int i = nodes.length - 1; i >= 0; i--) {
            nodes[i] = new Node(jsonArray.getJSONArray(i).getIntValue(0));
            nodes[i].next = last;
            last = nodes[i];
        }
        for (int i = 0; i < nodes.length; i++) {
            if (jsonArray.getJSONArray(i).getInteger(1) != null) {
                nodes[i].random = nodes[jsonArray.getJSONArray(i).getIntValue(1)];
            }
        }
        return nodes[0];
    }

    public static JSONArray NodeRandomToJsonArray(Node node) {
        JSONArray jsonArray = new JSONArray();
        if (node == null) {
            return jsonArray;
        }
        Map<Node, Integer> idxMap = new HashMap<>();
        Node curr = node;
        int idx = 0;
        while (curr != null) {
            idxMap.put(curr, idx++);
            curr = curr.next;
        }
        curr = node;
        while (curr != null) {
            JSONArray nodeArray = new JSONArray();
            nodeArray.add(curr.val);
            if (curr.random != null) {
                nodeArray.add(idxMap.get(curr.random));
            } else {
                nodeArray.add(null);
            }
            jsonArray.add(nodeArray);
            curr = curr.next;
        }
        return jsonArray;
    }
}
