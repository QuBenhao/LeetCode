package problems.problems_3487;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxSum(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        int s = 0, max = -101;
        for (int num: nums) {
            if (seen.contains(num)) {
                continue;
            }
            seen.add(num);
            if (num > 0) {
                s += num;
            }
            max = Math.max(max, num);
        }
        return max > 0 ? s : max;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxSum(nums));
    }
}
