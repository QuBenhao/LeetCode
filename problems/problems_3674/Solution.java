package problems.problems_3674;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minOperations(int[] nums) {
        for (int num: nums) {
            if (num != nums[0]) {
                return 1;
            }
        }
        return 0;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minOperations(nums));
    }
}
