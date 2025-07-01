package problems.problems_3331;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private void dfs(int[] parent, String s, int node, int[] ans, Map<Integer, List<Integer>> tree, int[] mapping) {
        int idx = s.charAt(node) - 'a';
        int before = mapping[idx];
        mapping[idx] = node;
        if (tree.containsKey(node)) {
            for (int child : tree.get(node)) {
                dfs(parent, s, child, ans, tree, mapping);
            }
        }
        mapping[idx] = before;
        if (before != -1) {
            ans[before] += ans[node];
        } else if (parent[node] != -1) {
            ans[parent[node]] += ans[node];
        }
    }

    public int[] findSubtreeSizes(int[] parent, String s) {
        int n = parent.length;
        Map<Integer, List<Integer>> tree = new HashMap<>(n);
        for (int i = 1; i < n; i++) {
            tree.computeIfAbsent(parent[i], k -> new ArrayList<>()).add(i);
        }
        int[] ans = new int[n];
        Arrays.fill(ans, 1);
        int[] mapping = new int[26];
        Arrays.fill(mapping, -1);
        dfs(parent, s, 0, ans, tree, mapping);
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] parent = jsonArrayToIntArray(inputJsonValues[0]);
		String s = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(findSubtreeSizes(parent, s));
    }
}
