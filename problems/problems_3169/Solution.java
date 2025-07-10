package problems.problems_3169;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countDays(int days, int[][] meetings) {
        Arrays.sort(meetings, Comparator.comparingInt(a -> a[0]));
        int ans = 0;
        int cur = 0;
        for (int[] meeting : meetings) {
            if (meeting[0] > cur) {
                ans += meeting[0] - cur - 1;
            }
            cur = Math.max(cur, meeting[1]);
        }
        return ans + days - cur;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int days = Integer.parseInt(inputJsonValues[0]);
		int[][] meetings = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(countDays(days, meetings));
    }
}
