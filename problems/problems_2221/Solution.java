package problems.problems_2221;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int triangularSum(int[] nums) {
        int n = nums.length;
        for (int i = n - 1; i > 0; --i) {
            for (int j = 0; j < i; ++j) {
                nums[j] = (nums[j] + nums[j + 1]) % 10;
            }
        }
        return nums[0];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(triangularSum(nums));
    }
}
