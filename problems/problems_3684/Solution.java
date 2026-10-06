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
            ans[i] = nums[uniques - 1 - i]; // The problem requires descending order
        }
        return ans;
    }

    // 26. Remove Duplicates from Sorted Array
    private int removeDuplicates(int[] nums) {
        int k = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) { // nums[i] is not a duplicate
                nums[k++] = nums[i]; // Keep nums[i]
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
