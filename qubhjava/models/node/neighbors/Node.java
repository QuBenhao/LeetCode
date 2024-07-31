package qubhjava.models.node.neighbors;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

// Definition for a Node.
public class Node {
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

    public static Node ArrayToNodeNeighbors(int[][] arr) {
        if (arr == null || arr.length == 0) {
            return null;
        }
        Node[] nodes = new Node[arr.length + 1];
        for (int i = 1; i < arr.length + 1; i++) {
            nodes[i] = new Node(i);
        }
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                nodes[i + 1].neighbors.add(nodes[arr[i][j]]);
            }
        }
        return nodes[1];
    }

    private static void dfs(Node node, Set<Integer> visited, List<int[]> ans) {
        if (ans.size() < node.val) {
            for (int i = ans.size(); i < node.val; i++) {
                ans.add(null);
            }
            ans.set(node.val - 1, new int[node.neighbors.size()]);
            for (int i = 0; i < node.neighbors.size(); i++) {
                ans.get(node.val - 1)[i] = node.neighbors.get(i).val;
            }
        } else {
            ans.set(node.val - 1, new int[node.neighbors.size()]);
            for (int i = 0; i < node.neighbors.size(); i++) {
                ans.get(node.val - 1)[i] = node.neighbors.get(i).val;
            }
        }
        for (Node neighbor : node.neighbors) {
            if (!visited.contains(neighbor.val)) {
                visited.add(neighbor.val);
                dfs(neighbor, visited, ans);
            }
        }
    }

    public static int[][] NodeNeighborsToArray(Node node) {
        List<int[]> ans = new ArrayList<>();
        if (node != null) {
            Set<Integer> visited = new HashSet<>();
            visited.add(node.val);
            dfs(node, visited, ans);
        }
        return ans.toArray(new int[0][]);
    }
}