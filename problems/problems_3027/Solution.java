package problems.problems_3027;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfPairs(int[][] points) {
        Arrays.sort(points, (a, b) -> { return a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]; });
        int ans = 0;
        int n = points.length;
        for (int i = 0; i < n; ++i) {
            int y1 = points[i][1];
            int maxY = Integer.MIN_VALUE;
            for (int j = i + 1; j < n; ++j) {
                int y2 = points[j][1];
                if (y1 >= y2 && y2 > maxY) {
                    maxY = y2;
                    ++ans;
                    if (maxY == y1) {
                        break;
                    } 
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
