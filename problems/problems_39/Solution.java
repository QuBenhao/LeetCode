package problems.problems_39;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private void dfs(int[] candidates, int target, int index, List<Integer> path, List<List<Integer>> res) {
        if (target == 0) {
            res.add(new ArrayList<>(path));
            return;
        }
        if (index == candidates.length) {
            return;
        }
        if (candidates[index] <= target) {
            path.add(candidates[index]);
            dfs(candidates, target - candidates[index], index, path, res);
            path.removeLast();
        }
        dfs(candidates, target, index + 1, path, res);
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(candidates, target, 0, new ArrayList<>(), res);
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] candidates = jsonArrayToIntArray(inputJsonValues[0]);
		int target = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(combinationSum(candidates, target));
    }
}
