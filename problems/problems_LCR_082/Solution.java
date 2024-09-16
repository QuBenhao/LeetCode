package problems.problems_LCR_082;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(0, target, candidates, path, res);
        return res;
    }

    private void backtrack(int start, int target, int[] candidates, List<Integer> path, List<List<Integer>> res) {
        if (target == 0) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }
            if (candidates[i] <= target) {
                path.add(candidates[i]);
                backtrack(i + 1, target - candidates[i], candidates, path, res);
                path.removeLast();
            } else {
                break;
            }
        }
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] candidates = jsonArrayToIntArray(inputJsonValues[0]);
		int target = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(combinationSum2(candidates, target));
    }
}
