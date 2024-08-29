package problems.problems_3153;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long sumDigitDifferences(int[] nums) {
        int length = 0;
        for (int num = nums[0]; num > 0; num /= 10) {
            length++;
        }
        long[][] counter = new long[length][10];
        long ans = 0;
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            for (int j = 0; num > 0; j++, num /= 10) {
                ans += (long) i - counter[j][num % 10];
                counter[j][num % 10]++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(sumDigitDifferences(nums));
    }
}
