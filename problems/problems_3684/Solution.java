package problems.problems_3684;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] maxKDistinct(int[] nums, int k) {
        Arrays.sort(nums);

        int uniques = removeDuplicates(nums);
        int size = Math.min(uniques, k);

        int[] ans = new int[size];
        for (int i = 0; i < size; i++) {
            ans[i] = nums[uniques - 1 - i]; // 题目要求从大到小
        }
        return ans;
    }

    // 26. 删除有序数组中的重复项
    private int removeDuplicates(int[] nums) {
        int k = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) { // nums[i] 不是重复项
                nums[k++] = nums[i]; // 保留 nums[i]
            }
        }
        return k;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxKDistinct(nums, k));
    }
}
