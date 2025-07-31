package problems.problems_436;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findRightInterval(int[][] intervals) {
        int n = intervals.length;
        int[] result = new int[n];
        Map<Integer, Integer> startIndexMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            startIndexMap.put(intervals[i][0], i);
        }
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        for (int i = 0; i < n; i++) {
            int left = 0, right = n;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (intervals[mid][0] < intervals[i][1]) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            result[startIndexMap.get(intervals[i][0])] = left < n ? startIndexMap.get(intervals[left][0]) : -1;
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] intervals = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(findRightInterval(intervals));
    }
}
