package problems.problems_3025;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfPairs(int[][] points) {
        Arrays.sort(points, (a, b) -> {
            return a[0] != b[0] ? a[0] - b[0] : b[1] - a[1];
        });
        int ans = 0;
        for (int i = 0, n = points.length; i < n; ++i) {
            int maxY = -1;
            for (int j = i + 1; j < n; ++j) {
                if (points[i][1] >= points[j][1] && points[j][1] > maxY) {
                    maxY = points[j][1];
                    ++ans;
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] points = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(numberOfPairs(points));
    }
}
