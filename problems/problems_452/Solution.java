package problems.problems_452;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, Comparator.comparingInt(a -> a[1]));
        int cur = points[0][1], ans = 1;
        for (int[] point: points) {
            if (point[0] > cur) {
                ans++;
                cur = point[1];
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[][] points = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(findMinArrowShots(points));
    }
}
