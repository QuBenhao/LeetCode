package problems.problems_321;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private Deque<Integer> pickArray(int[] nums, int length) {
        int drop = nums.length - length;
        Deque<Integer> stack = new ArrayDeque<>();
        for (int num : nums) {
            while (drop > 0 && !stack.isEmpty() && stack.peekLast() < num) {
                stack.pollLast();
                drop--;
            }
            stack.addLast(num);
        }
        while (drop-- > 0) {
            stack.pollLast();
        }
        return stack;
    }

    private boolean isGreater(Iterable<Integer> it1, Iterable<Integer> it2) {
        Iterator<Integer> iter1 = it1.iterator();
        Iterator<Integer> iter2 = it2.iterator();
        while (iter1.hasNext() && iter2.hasNext()) {
            int num1 = iter1.next();
            int num2 = iter2.next();
            if (num1 != num2) {
                return num1 > num2;
            }
        }
        return iter1.hasNext() && !iter2.hasNext();
    }

    private List<Integer> merge(Deque<Integer> stack1, Deque<Integer> stack2) {
        List<Integer> merged = new ArrayList<>();
        while (!stack1.isEmpty() || !stack2.isEmpty()) {
            if (isGreater(stack1, stack2)) {
                merged.add(stack1.pollFirst());
            } else {
                merged.add(stack2.pollFirst());
            }
        }
        return merged;
    }

    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        int m = nums1.length;
        int n = nums2.length;
        if (m > n) {
            return maxNumber(nums2, nums1, k);
        }
        List<Integer> result = new ArrayList<>();
        for (int i = Math.max(0, k - n); i <= Math.min(m, k); i++) {
            Deque<Integer> stack1 = pickArray(nums1, i);
            Deque<Integer> stack2 = pickArray(nums2, k - i);
            List<Integer> merged = merge(stack1, stack2);
            if (isGreater(merged, result)) {
                result = merged;
            }
        }
        return result.stream().mapToInt(Integer::intValue).toArray();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] nums2 = jsonArrayToIntArray(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxNumber(nums1, nums2, k));
    }
}
