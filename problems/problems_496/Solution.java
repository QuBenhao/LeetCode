package problems.problems_496;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int[] ans = new int[n];
        Map<Integer, Integer> map = new HashMap<>(n);
        for (int i = 0; i < n; ++i) {
            map.put(nums1[i], i);
            ans[i] = -1;
        }
        Stack<Integer> stack = new Stack<>();
        for (int num : nums2) {
            while (!stack.isEmpty() && stack.peek() < num) {
                int top = stack.pop();
                if (map.containsKey(top)) {
                    ans[map.get(top)] = num;
                }
            }
            stack.push(num);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] nums2 = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(nextGreaterElement(nums1, nums2));
    }
}
