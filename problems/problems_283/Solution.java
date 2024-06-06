package problems.problems_283;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public void moveZeroes(int[] nums) {
        for (int left = 0, right = 0; right < nums.length; right++) {
            if (nums[right] != 0) {
                int tmp = nums[right];
                nums[right] = nums[left];
                nums[left++] = tmp;
            }
        }
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
        moveZeroes(nums);
        return JSON.toJSON(nums);
    }
}
