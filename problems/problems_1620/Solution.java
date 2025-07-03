package problems.problems_1620;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] bestCoordinate(int[][] towers, int radius) {
        int ans = 0;
        int ans_x = 0, ans_y = 0;
        radius *= radius;
        for (int x = 0; x <= 50; x++) {
            for (int y = 0; y <= 50; y++) {
                int sum = 0;
                for (int[] tower : towers) {
                    int dx = tower[0] - x;
                    int dy = tower[1] - y;
                    double dist = dx * dx + dy * dy;
                    if (dist <= radius) {
                        sum += Math.floor(tower[2] / (1 + Math.sqrt(dist)));
                    }
                }
                if (sum > ans) {
                    ans = sum;
                    ans_x = x;
                    ans_y = y;
                }
            }
        }
        return new int[]{ans_x, ans_y};
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] towers = jsonArrayToInt2DArray(inputJsonValues[0]);
		int radius = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(bestCoordinate(towers, radius));
    }
}
