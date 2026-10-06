package problems.problems_1932;

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
    // Leaf degrees in the forest, indexed by leaf value
    public int[] du = new int[50005];
    // Map root values to root nodes
    public TreeNode[] nodeValToNode = new TreeNode[50005];
    // Queue for topological sorting
    public Queue<TreeNode> queue = new LinkedList<>();
    // Number of trees in the forest
    public int n;
    // Number of merges, or trees removed from the forest
    public int sub = 0;
    // Whether the merged tree satisfies the BST property
    public boolean isOK = true;
    public TreeNode canMerge(List<TreeNode> trees) {
        n = trees.size();
        for (int i = 0; i < n; i++) {
            TreeNode treeNode = trees.get(i);
            nodeValToNode[treeNode.val] = treeNode;
            // Increment degrees of leaves under this root
            dfs(treeNode , true);
        }
        queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            TreeNode treeNode = trees.get(i);
            // Enqueue roots with degree 0
            if(du[treeNode.val] == 0) {
                queue.add(treeNode);
            }
        }
        // A valid merged BST is possible only if exactly one root has degree 0
        // More than one such root cannot be merged into a single tree
        // A degree-0 root cannot attach to another tree and must remain a root, so multiple such roots are invalid
        // No degree-0 root means a cycle, which cannot form a valid BST
        // For example: 1 -> 2, 2 -> 3, 3 -> 1, where a -> b means tree a has a leaf with root b's value
        // After merging roots 1 and 2 under root 1, merging root 3 introduces a leaf equal to root 1
        // This violates the BST rule: every value in a node's left subtree is smaller, and every value in its right subtree is larger
        if(queue.size() != 1) return null;
        // Save the root of the fully merged tree as the answer
        TreeNode ans = queue.peek();
        while (!queue.isEmpty()) {
            TreeNode treeNode = queue.poll();
            // Decrement degrees of leaves under this root
            dfsSub(treeNode);
            // All merges are complete; exit
            if(sub == n - 1) break;
        }
        // Topological sorting finished before all trees were merged
        if(sub != n - 1) return null;
        // Check whether the merged tree meets the requirements
        check(ans);
        if(!isOK) return null;
        // Requirements satisfied
        return ans;
    }

    // Topological sorting: increment leaf degrees, except for a root that is also a leaf; its degree is decremented only by other trees' leaves before it can be enqueued at degree 0
    public void dfs(TreeNode treeNode , boolean isRoot) {
        if(treeNode.left == null && treeNode.right == null) {
            if(!isRoot) du[treeNode.val]++;
            return;
        }
        if(treeNode.left != null) dfs(treeNode.left , false);
        if(treeNode.right != null) dfs(treeNode.right , false);
    }

    // Topological sorting: decrement leaf degrees; if one reaches 0 and matches a root value, merge that tree and enqueue its root
    public void dfsSub(TreeNode treeNode) {
        if(treeNode.left == null && treeNode.right == null) {
            du[treeNode.val]--;
            if(du[treeNode.val] == 0 && nodeValToNode[treeNode.val] != null) {
                // Merge trees
                treeNode.left = nodeValToNode[treeNode.val].left;
                treeNode.right = nodeValToNode[treeNode.val].right;
                // Degree is now 0; enqueue it
                queue.add(treeNode);
                // Decrease the forest's tree count
                sub++;
            }
            return;
        }
        if(treeNode.left != null) dfsSub(treeNode.left);
        if(treeNode.right != null) dfsSub(treeNode.right);
    }

    // Check the merged subtree's BST property and return {minimum, maximum}
    public int[] check(TreeNode treeNode) {
        // Already invalid; the returned value does not matter
        if (!isOK) return new int[2];
        int[] minAndMax = new int[2];
        // Initial value
        minAndMax[0] = treeNode.val;  // Minimum value
        minAndMax[1] = treeNode.val;  // Maximum value
        if (treeNode.left != null) {
            int[] left = check(treeNode.left);
            // Update
            minAndMax[0] = Math.min(minAndMax[0], left[0]);
            minAndMax[1] = Math.max(minAndMax[1], left[1]);
            // Invalid if the node's value is no greater than the left subtree's maximum
            if (treeNode.val <= left[1]) isOK = false;
        }
        if (treeNode.right != null) {
            int[] right = check(treeNode.right);
            // Update
            minAndMax[0] = Math.min(minAndMax[0], right[0]);
            minAndMax[1] = Math.max(minAndMax[1], right[1]);
            // Invalid if the node's value is no smaller than the right subtree's minimum
            if (treeNode.val >= right[0]) isOK = false;
        }
        return minAndMax;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<TreeNode> trees = jsonArrayToTreeNodeList(inputJsonValues[0]);
        return JSON.toJSON(TreeNode.TreeNodeToArray(canMerge(trees)));
    }
}
