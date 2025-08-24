package problems.problems_1493;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int longestSubarray(int[] nums) {
        boolean isAllOnes = true;
        for (int num : nums) {
            if (num != 1) {
                isAllOnes = false;
                break;
            }
        }
        int n = nums.length;
        if (isAllOnes) return n - 1;
        int ans = 0, last = 0, cur = 0;
        for (int i = 0; i <= n; ++i) {
            if (i == n || nums[i] != 1) {
                ans = Math.max(ans, last + cur);
                last = cur;
                cur = 0;
            } else {
                ++cur;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(longestSubarray(nums));
    }
}
