package problems.problems_2187;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumTime(int[] time, int totalTrips) {
        int minT = Integer.MAX_VALUE;
        int maxT = 0;
        for (int t : time) {
            minT = Math.min(minT, t);
            maxT = Math.max(maxT, t);
        }
        int avg = (totalTrips - 1) / time.length + 1;
        // Loop invariant: check(left) is always false
        long left = (long) minT * avg - 1;
        // Loop invariant: check(right) is always true
        long right = Math.min((long) maxT * avg, (long) minT * totalTrips);
        // The open interval (left, right) is nonempty
        while (left + 1 < right) {
            long mid = (left + right) >>> 1;
            if (check(mid, time, totalTrips)) {
                // Shrink the binary-search interval to (left, mid)
                right = mid;
            } else {
                // Shrink the binary-search interval to (mid, right)
                left = mid;
            }
        }
        // Now left equals right-1
        // check(left) = false and check(right) = true, so the answer is right
        return right; // The smallest value for which the predicate is true
    }

    private boolean check(long x, int[] time, int totalTrips) {
        long sum = 0;
        for (int t : time) {
            sum += x / t;
            if (sum >= totalTrips) {
                return true;
            }
        }
        return false;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] time = jsonArrayToIntArray(inputJsonValues[0]);
		int totalTrips = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minimumTime(time, totalTrips));
    }
}
