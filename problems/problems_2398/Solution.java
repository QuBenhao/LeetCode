package problems.problems_2398;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private boolean check(int[] chargeTimes, int[] runningCosts, long budget, int mid) {
        int n = chargeTimes.length;
        long sum = 0L;
        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!deque.isEmpty() && chargeTimes[deque.peekLast()] <= chargeTimes[i]) {
                deque.pollLast();
            }
            deque.offerLast(i);
            sum += runningCosts[i];
            if (i >= (deque.peekFirst() == null ? 0 : deque.peekFirst()) + mid) {
                deque.pollFirst();
            }
            if (i >= mid - 1) {
                if (sum * mid + chargeTimes[deque.peekFirst() == null ? 0 : deque.peekFirst()] <= budget) {
                    return true;
                }
                sum -= runningCosts[i - mid + 1];
            }
        }
        return false;
    }
    public int maximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        int left = 0, right = chargeTimes.length;
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (!check(chargeTimes, runningCosts, budget, mid)) {
                right = mid - 1;
            } else {
                left = mid;
            }
        }
        return left;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] chargeTimes = jsonArrayToIntArray(inputJsonValues[0]);
		int[] runningCosts = jsonArrayToIntArray(inputJsonValues[1]);
		long budget = Long.parseLong(inputJsonValues[2]);
        return JSON.toJSON(maximumRobots(chargeTimes, runningCosts, budget));
    }
}
