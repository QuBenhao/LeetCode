package problems.problems_2016;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumDifference(int[] nums) {
        int ans = -1;
        int min = nums[0];
        for (int num: nums) {
            if (num > min) {
                ans = Math.max(ans, num - min);
            } else {
                min = num;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maximumDifference(nums));
    }
}
