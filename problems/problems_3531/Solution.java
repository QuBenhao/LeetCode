package problems.problems_3531;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countCoveredBuildings(int n, int[][] buildings) {
        int[][] boundX = new int[n + 1][2], boundY = new int[n + 1][2];
        for (int i = 0; i <= n; i++) {
            boundX[i][0] = n + 1;
            boundX[i][1] = -1;
            boundY[i][0] = n + 1;
            boundY[i][1] = -1;
        }
        for (int[] building : buildings) {
            int x = building[0], y = building[1];
            boundX[x][0] = Math.min(boundX[x][0], y);
            boundX[x][1] = Math.max(boundX[x][1], y);
            boundY[y][0] = Math.min(boundY[y][0], x);
            boundY[y][1] = Math.max(boundY[y][1], x);
        }
        int ans = 0;
        for (int[] building: buildings) {
            int x = building[0], y = building[1];
            if (boundX[x][0] < y && boundX[x][1] > y &&
                boundY[y][0] < x && boundY[y][1] > x) {
                ans++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] buildings = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(countCoveredBuildings(n, buildings));
    }
}
