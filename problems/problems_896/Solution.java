package problems.problems_896;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isMonotonic(int[] nums) {
        boolean inc = false, dec = false;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] < nums[i + 1]) {
                if (dec) {
                    return false;
                }
                inc = true;
            } else if (nums[i] > nums[i + 1]) {
                if (inc) {
                    return false;
                }
                dec = true;
            }
        }
        return true;
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(isMonotonic(nums));
    }
}
