package problems.problems_LCR_090;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int rob(int[] nums) {
        int n = nums.length;
        int dpRob = nums[0], dpNotRob = nums[0];
        for (int i = 2; i < n - 1; i++) {
            int temp = dpRob;
            dpRob = dpNotRob + nums[i];
            dpNotRob = Math.max(dpNotRob, temp);
        }
        int res = Math.max(dpRob, dpNotRob);
        dpRob = 0;
        dpNotRob = 0;
        for (int i = 1; i < n; i++) {
            int temp = dpRob;
            dpRob = dpNotRob + nums[i];
            dpNotRob = Math.max(dpNotRob, temp);
        }
        return Math.max(res, Math.max(dpRob, dpNotRob));
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(rob(nums));
    }
}
