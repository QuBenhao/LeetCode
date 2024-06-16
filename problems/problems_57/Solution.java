package problems.problems_57;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> ans = new ArrayList<>();
        int left = newInterval[0], right = newInterval[1];
        for (int[] interval: intervals) {
            int a = interval[0], b = interval[1];
            if (b < left || a > right) {
                if (a > right) {
                    ans.add(new int[]{left, right});
                    left = right = 0x3f3f3f;
                }
                ans.add(new int[]{a, b});
            } else {
                left = Math.min(left, a);
                right = Math.max(right, b);
            }
        }
        if (left != 0x3f3f3f && (ans.size() == 0 || ans.get(ans.size() - 1)[1] < left)) {
            ans.add(new int[]{left, right});
        }
        return ans.toArray(new int[0][0]);
    }

    @Override
    public Object solve(String[] values) {
        int[][] intervals = jsonArrayToInt2DArray(values[0]);
		int[] newInterval = jsonArrayToIntArray(values[1]);
        return JSON.toJSON(insert(intervals, newInterval));
    }
}
