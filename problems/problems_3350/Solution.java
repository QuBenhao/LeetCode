package problems.problems_3350;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxIncreasingSubarrays(List<Integer> nums) {
        int n = nums.size();
        int ans = 0, last = 0, cur = 1;
        for (int i = 1; i <= n; ++i) {
            if (i == n || nums.get(i - 1) >= nums.get(i)) {
                ans = Math.max(ans, Math.min(last, cur));
                ans = Math.max(ans, cur / 2);
                last = cur;
                cur = 1;
                continue;
            }
            ++cur;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Integer> nums = jsonArrayToIntList(inputJsonValues[0]);
        return JSON.toJSON(maxIncreasingSubarrays(nums));
    }
}
