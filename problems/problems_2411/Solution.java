package problems.problems_2411;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] smallestSubarrays(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        Arrays.fill(result, 1);
        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            for (int j = i - 1; j >= 0; --j) {
                if ((nums[j] | x) == nums[j]) {
                    break;
                }
                nums[j] |= x;
                result[j] = i - j + 1;
            }
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(smallestSubarrays(nums));
    }
}
