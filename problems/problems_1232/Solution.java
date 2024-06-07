package problems.problems_1232;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean checkStraightLine(int[][] coordinates) {
        int xd = coordinates[1][0] - coordinates[0][0], yd = coordinates[1][1] - coordinates[0][1],
                c = coordinates[0][0] * coordinates[1][1] - coordinates[0][1] * coordinates[1][0];
        for (int i = 2; i < coordinates.length; i++) {
            if (coordinates[i][0] * yd - coordinates[i][1] * xd != c) {
                return false;
            }
        }
        return true;
    }

    @Override
    public Object solve(String[] values) {
        int[][] coordinates = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(checkStraightLine(coordinates));
    }
}
