package problems.problems_2294;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int partitionArray(int[] nums, int k) {
        Arrays.sort(nums);
        int cur = nums[0];
        int ans = 1;
        for (int num: nums) {
            if (num - cur > k) {
                cur = num;
                ans++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(partitionArray(nums, k));
    }
}
