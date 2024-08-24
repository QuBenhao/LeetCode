package problems.problems_138;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

import qubhjava.models.node.random.Node;

public class Solution extends BaseSolution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }
        Node cur = head;
        while (cur != null) {
            Node copyNode = new Node(cur.val);
            copyNode.next = cur.next;
            cur.next = copyNode;
            cur = copyNode.next;
        }
        cur = head;
        while (cur != null) {
            if (cur.random != null) {
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next;
        }
        cur = head;
        Node copyHead = head.next;
        while (cur != null) {
            Node copyNode = cur.next;
            cur.next = copyNode.next;
            copyNode.next = cur.next == null ? null : cur.next.next;
            cur = cur.next;
        }
        return copyHead;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        Node head = Node.JsonArrayToNodeRandom(inputJsonValues[0]);
        return JSON.toJSON(Node.NodeRandomToJsonArray(copyRandomList(head)));
    }
}
