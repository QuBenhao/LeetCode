package problems.problems_45;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int jump(int[] nums) {
        int ans = 0;
        for (int cur = 0, nxt = 0, n = nums.length; nxt < n - 1; ans++) {
            int tmp = nxt;
            for (int i = cur; i <= nxt; i++) {
                tmp = Math.max(tmp, nums[i] + i);
            }
            cur = nxt + 1;
            nxt = tmp;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(jump(nums));
    }
}
