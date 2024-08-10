package problems.problems_55;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canJump(int[] nums) {
        int maxDis = 0, n = nums.length;
        for (int i = 0; i < n; i++) {
            maxDis = Math.max(maxDis, i + nums[i]);
            if (maxDis >= n - 1) {
                return true;
            }
            if (i >= maxDis) {
                return false;
            }
        }
        return false;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(canJump(nums));
    }
}
