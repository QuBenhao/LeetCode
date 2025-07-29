package problems.problems_2419;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int longestSubarray(int[] nums) {
        int ans = 0, cur = 0, max = 0;
        for (int num : nums) {
            if (num > max) {
                ans = cur = 1;
                max = num;
            } else if (num == max) {
                ans = Math.max(++cur, ans);
            } else {
                cur = 0;
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
