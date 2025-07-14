package problems.problems_662;

import com.alibaba.fastjson.JSON;
import java.util.*;
import javafx.util.Pair;
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
    public int widthOfBinaryTree(TreeNode root) {
        int ans = 0;
        if (root == null) {
            return ans;
        }
        ArrayDeque<Pair<Integer, TreeNode>> q = new ArrayDeque<>();
        q.offer(new Pair<>(0, root));
        int base = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            ans = Math.max(ans, q.peekLast().getKey() - q.peekFirst().getKey() + 1);
            for (int i = 0; i < size; ++i) {
                Pair<Integer, TreeNode> pair = q.poll();
                int index = pair.getKey() - base;
                TreeNode node = pair.getValue();
                if (node.left != null) {
                    q.offer(new Pair<>(2 * index - (1 << base), node.left));
                }
                if (node.right != null) {
                    q.offer(new Pair<>(2 * index + 1 - (1 << base), node.right));
                }
            }
            ++base;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
        return JSON.toJSON(widthOfBinaryTree(root));
    }
}
