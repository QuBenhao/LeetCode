package problems.problems_215;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findKthLargest(int[] nums, int k) {
        Random random = new Random();
        int pivot = nums[random.nextInt(nums.length)];
        List<Integer> left = new ArrayList<>(), right = new ArrayList<>(), equals = new ArrayList<>();
        for (int num: nums) {
            if (num > pivot) {
                right.add(num);
            } else if (num < pivot) {
                left.add(num);
            } else {
                equals.add(num);
            }
        }
        if (k <= right.size()) {
            return findKthLargest(right.stream().mapToInt(Integer::intValue).toArray(), k);
        } else if (k <= right.size() + equals.size()) {
            return pivot;
        } else {
            return findKthLargest(left.stream().mapToInt(Integer::intValue).toArray(), k - right.size() - equals.size());
        }
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(findKthLargest(nums, k));
    }
}
