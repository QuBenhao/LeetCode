package problems.problems_3038;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxOperations(int[] nums) {
        for (int i = 2, s = nums[0] + nums[1]; i < nums.length - 1; i += 2) {
            if (nums[i] + nums[i + 1] != s) {
                return i / 2;
            }
        }
        return nums.length / 2;
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(maxOperations(nums));
    }
}
