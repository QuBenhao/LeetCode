package problems.problems_2210;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int diffToSign(int diff) {
        return diff > 0 ? 1 : (diff < 0 ? -1 : 0);
    }

    public int countHillValley(int[] nums) {
        int ans = 0;
        int n = nums.length;
        for (int i = 0, last = nums[0], lastDiff = 0; i < n; ++i) {
            while (i < n - 1 && nums[i] == nums[i+1]) {
                ++i;
            }
            int curDiff = diffToSign(nums[i] - last);
            if (lastDiff * curDiff < 0) {
                ans++;
            }
            last = nums[i];
            lastDiff = curDiff;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(countHillValley(nums));
    }
}
