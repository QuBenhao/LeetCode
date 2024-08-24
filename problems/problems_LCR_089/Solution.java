package problems.problems_LCR_089;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int rob(int[] nums) {
        int dpNotRob = 0, dpRob = 0;
        for (int num : nums) {
            int temp = dpNotRob;
            dpNotRob = Math.max(dpNotRob, dpRob);
            dpRob = temp + num;
        }
        return Math.max(dpNotRob, dpRob);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(rob(nums));
    }
}
