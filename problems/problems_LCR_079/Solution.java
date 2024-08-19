package problems.problems_LCR_079;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(ans, new LinkedList<>(), nums, 0);
        return ans;
    }

    private void backtrack(List<List<Integer>> ans, List<Integer> tmp, int[] nums, int idx) {
        if (idx == nums.length) {
            ans.add(new ArrayList<>(tmp));
            return;
        }
        backtrack(ans, tmp, nums, idx + 1);
        tmp.add(nums[idx]);
        backtrack(ans, tmp, nums, idx + 1);
        tmp.removeLast();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(subsets(nums));
    }
}
