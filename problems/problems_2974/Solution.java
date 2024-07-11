package problems.problems_2974;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] numberGame(int[] nums) {
        Arrays.sort(nums);
        int[] ans = new int[nums.length];
        for (int i = 1; i < nums.length; i += 2) {
            ans[i - 1] = nums[i];
            ans[i] = nums[i - 1];
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(numberGame(nums));
    }
}
