package problems.problems_LCR_050;

import java.util.HashMap;
import java.util.Map;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;
import qubhjava.models.TreeNode;

public class Solution extends BaseSolution {
    public int pathSum(TreeNode root, int targetSum) {
        Map<Long, Integer> map = new HashMap<>();
        map.put(0L, 1);
        return dfs(root, map, 0L, targetSum);
    }

    private int dfs(TreeNode node, Map<Long, Integer> counter, long cur, long targetSum) {
        if (node == null) {
            return 0;
        }
        cur += node.val;
        int ans = counter.getOrDefault(cur - targetSum, 0);
        counter.put(cur, counter.getOrDefault(cur, 0) + 1);
        ans += dfs(node.left, counter, cur, targetSum);
        ans += dfs(node.right, counter, cur, targetSum);
        counter.put(cur, counter.get(cur) - 1);
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        TreeNode root = TreeNode.ArrayToTreeNode(inputJsonValues[0]);
		int targetSum = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(pathSum(root, targetSum));
    }
}
