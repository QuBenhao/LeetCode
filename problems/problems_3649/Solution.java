package problems.problems_3649;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long perfectPairs(int[] nums) {
        int n = nums.length;
        int[] absNums = new int[n];
        for (int i = 0; i < n; i++) {
            absNums[i] = Math.abs(nums[i]);
        }
        Arrays.sort(absNums);
        long ans = 0;
        for (int l = 0, r = 1; r < n; ++r) {
            while (absNums[l] * 2 < absNums[r]) {
                l++;
            }
            ans += r - l;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(perfectPairs(nums));
    }
}
