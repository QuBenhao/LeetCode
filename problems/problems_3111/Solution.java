package problems.problems_3111;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minRectanglesToCoverPoints(int[][] points, int w) {
        Arrays.sort(points, Comparator.comparingInt(a -> a[0]));
        int ans = 0;
        for (int idx = 0; idx < points.length; ) {
            ans++;
            int cur = points[idx][0] + w;
            while (idx < points.length && points[idx][0] <= cur) {
                idx++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] points = jsonArrayToInt2DArray(inputJsonValues[0]);
		int w = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minRectanglesToCoverPoints(points, w));
    }
}
