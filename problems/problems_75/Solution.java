package problems.problems_75;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    public void sortColors(int[] nums) {
        for (int i = 0, p0 = 0, p1 = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                swap(nums, p1, i);
                p1++;
            } else if (nums[i] == 0) {
                swap(nums, p0, i);
                if (p0 < p1) {
                    swap(nums, p1, i);
                }
                p0++;
                p1++;
            }
        }
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
		sortColors(nums);
        return JSON.toJSON(nums);
    }
}
