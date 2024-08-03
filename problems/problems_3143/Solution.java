package problems.problems_3143;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxPointsInsideSquare(int[][] points, String s) {
        int[] idxMap = new int[26];
        Arrays.fill(idxMap, Integer.MAX_VALUE);
        int dist = Integer.MAX_VALUE;
        for (int i = 0; i < points.length; i++) {
            int idx = s.charAt(i) - 'a';
            int cur = Math.max(Math.abs(points[i][0]), Math.abs(points[i][1]));
            if (cur < idxMap[idx]) {
                dist = Math.min(dist, idxMap[idx]);
                idxMap[idx] = cur;
            } else {
                dist = Math.min(dist, cur);
            }
        }
        int ans = 0;
        for (int v: idxMap) {
            if (v < dist) {
                ans++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] points = jsonArrayToInt2DArray(inputJsonValues[0]);
		String s = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(maxPointsInsideSquare(points, s));
    }
}
