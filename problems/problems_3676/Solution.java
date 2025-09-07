package problems.problems_3676;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;

public class Solution extends BaseSolution {
    public long bowlSubarrays(int[] nums) {
        int n = nums.length;
        int[] leftGreater = new int[n], rightGreater = new int[n];
        Arrays.fill(leftGreater, -1);
        Arrays.fill(rightGreater, -1);
        Deque<Integer> st = new ArrayDeque();
        for (int i = 0; i < n; ++i) {
            while (!st.isEmpty() && nums[st.peekLast()] < nums[i]) {
                rightGreater[st.pollLast()] = i;
            }
            if (!st.isEmpty()) {
                leftGreater[i] = st.peekLast();
            }
            st.addLast(i);
        }
        Set<Long> s = new HashSet<>();
        for (int i = 0; i < n; ++i) {
            if (leftGreater[i] != -1 && rightGreater[i] != -1) {
                s.add(1L * leftGreater[i] * n + rightGreater[i]);
            }
        }
        return s.size();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(bowlSubarrays(nums));
    }
}
