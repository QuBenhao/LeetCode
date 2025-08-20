package problems.problems_652;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import qubhjava.models.TreeNode;

public class Solution extends BaseSolution {
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        Map<String, TreeNode> ansCache = new HashMap<>();
        Set<String> cache = new HashSet<>();
        dfs(root, cache, ansCache);

        return new ArrayList<>(ansCache.values());
    }

    private String dfs(TreeNode node, Set<String> cache, Map<String, TreeNode> ansCache) {
        if (node == null) {
            return "#";
        }
        String left = dfs(node.left, cache, ansCache);
        String right = dfs(node.right, cache, ansCache);
        String curr = node.val + "," + left + "," + right;

        if (cache.contains(curr) && !ansCache.containsKey(curr)) {
            ansCache.put(curr, node);
        }
        cache.add(curr);
        return curr;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
        return JSON.toJSON(TreeNode.TreeNodeListToJsonArray(findDuplicateSubtrees(root)));
    }
}
