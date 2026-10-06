package problems.problems_1948;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static class TrieNode {
        Map<String, TrieNode> son = new HashMap<>();
        String name; // Folder name
        boolean deleted = false; // Deletion flag
    }

    public List<List<String>> deleteDuplicateFolder(List<List<String>> paths) {
        TrieNode root = new TrieNode();
        for (List<String> path : paths) {
            // Insert path into the trie; see 208. Implement Trie
            TrieNode cur = root;
            for (String s : path) {
                if (!cur.son.containsKey(s)) {
                    cur.son.put(s, new TrieNode());
                }
                cur = cur.son.get(s);
                cur.name = s;
            }
        }

        Map<String, TrieNode> exprToNode = new HashMap<>(); // Parenthesized subtree expression -> subtree root
        for (TrieNode son : root.son.values()) {
            genExpr(son, exprToNode);
        }

        List<List<String>> ans = new ArrayList<>();
        List<String> path = new ArrayList<>();
        for (TrieNode son : root.son.values()) {
            dfs(son, path, ans);
        }
        return ans;
    }

    private String genExpr(TrieNode node, Map<String, TrieNode> exprToNode) {
        if (node.son.isEmpty()) { // Leaf
            return node.name; // The expression is just the folder name
        }

        List<String> expr = new ArrayList<>();
        for (TrieNode son : node.son.values()) {
            // Wrap each subtree expression in parentheses
            expr.add("(" + genExpr(son, exprToNode) + ")");
        }
        Collections.sort(expr);

        String subTreeExpr = String.join("", expr); // Concatenate all subtree expressions in lexicographic order
        TrieNode n = exprToNode.get(subTreeExpr);
        if (n != null) { // An existing subTreeExpr in the map indicates duplicate folders
            n.deleted = true; // Mark the node recorded in the map for deletion
            node.deleted = true; // Mark the current node for deletion
        } else {
            exprToNode.put(subTreeExpr, node);
        }

        return node.name + subTreeExpr;
    }

    // Backtrack through the trie, visiting only undeleted nodes and recording their paths in the answer
    // Similar to 257. Binary Tree Paths
    private void dfs(TrieNode node, List<String> path, List<List<String>> ans) {
        if (node.deleted) {
            return;
        }
        path.add(node.name);
        ans.add(new ArrayList<>(path)); // Record the path
        for (TrieNode son : node.son.values()) {
            dfs(son, path, ans);
        }
        path.removeLast(); // Restore the previous state
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<String>> paths = jsonArrayToString2DList(inputJsonValues[0]);
        return JSON.toJSON(deleteDuplicateFolder(paths));
    }
}
