package problems.problems_1848;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;

public class Solution extends BaseSolution {
    public int getMinDistance(int[] nums, int target, int start) {
        int n = nums.length;
        int ans = n + 1;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == target) {
                ans = Math.min(ans, Math.abs(i - start));
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        int target = Integer.parseInt(inputJsonValues[1]);
        int start = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(getMinDistance(nums, target, start));
    }
}
