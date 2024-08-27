package problems.problems_LCR_008;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minSubArrayLen(int target, int[] nums) {
        Deque<Integer> queue = new ArrayDeque<>();
        int sum = 0;
        int n = nums.length;
        int ans = n + 1;
        for (int num: nums) {
            queue.addLast(num);
            sum += num;
            while (sum >= target) {
                ans = Math.min(ans, queue.size());
                Integer first = queue.pollFirst();
                sum -= first == null ? 0 : first;
            }
        }
        return ans == n + 1 ? 0 : ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int target = Integer.parseInt(inputJsonValues[0]);
		int[] nums = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minSubArrayLen(target, nums));
    }
}
