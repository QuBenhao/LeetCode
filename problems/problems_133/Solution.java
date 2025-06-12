package problems.problems_133;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

import qubhjava.models.node.neighbors.Node;

public class Solution extends BaseSolution {
    public Node cloneGraph(Node node) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        Node node = Node.ArrayToNodeNeighbors(jsonArrayToInt2DArray(inputJsonValues[0]));
        return JSON.toJSON(Node.NodeNeighborsToArray(cloneGraph(node)));
    }
}
