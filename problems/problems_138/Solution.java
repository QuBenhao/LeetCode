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
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        Node head = Node.JsonArrayToNodeRandom(inputJsonValues[0]);
        return JSON.toJSON(Node.NodeRandomToJsonArray(copyRandomList(head)));
    }
}
