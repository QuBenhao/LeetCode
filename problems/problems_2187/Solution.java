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
        // 循环不变量：check(left) 恒为 false
        long left = (long) minT * avg - 1;
        // 循环不变量：check(right) 恒为 true
        long right = Math.min((long) maxT * avg, (long) minT * totalTrips);
        // 开区间 (left, right) 不为空
        while (left + 1 < right) {
            long mid = (left + right) >>> 1;
            if (check(mid, time, totalTrips)) {
                // 缩小二分区间为 (left, mid)
                right = mid;
            } else {
                // 缩小二分区间为 (mid, right)
                left = mid;
            }
        }
        // 此时 left 等于 right-1
        // check(left) = false 且 check(right) = true，所以答案是 right
        return right; // 最小的 true
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
