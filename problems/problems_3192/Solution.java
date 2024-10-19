package problems.problems_3192;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minOperations(int[] nums) {
        int ans = 0;
        for (int num: nums) {
            if (ans % 2 == num) {
                ans++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minOperations(nums));
    }
}
