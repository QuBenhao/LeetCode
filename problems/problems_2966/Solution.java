package problems.problems_2966;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[][] divideArray(int[] nums, int k) {
        int[][] ans = new int[nums.length/3][3];
        Arrays.sort(nums);
        for (int idx = 0, i = 0; i < nums.length; i += 3, idx++) {
            if (nums[i+2] - nums[i] > k) {
                return new int[0][0];
            }
            System.arraycopy(nums, i, ans[idx], 0, 3);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(divideArray(nums, k));
    }
}
