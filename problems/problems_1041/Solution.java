package problems.problems_1041;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isRobotBounded(String instructions) {
        int x = 0, y = 0, d = 0;
        int[][] dirs = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
        for (int i = 0; i < instructions.length(); i++) {
            switch (instructions.charAt(i)) {
                case 'L':
                    d = (d + 1) % 4;
                    break;
                case 'R':
                    d = (d + 3) % 4;
                    break;
                default:
                    x += dirs[d][0];
                    y += dirs[d][1];
            }
        }
        return (x == 0 && y == 0) || d != 0;
    }

    @Override
    public Object solve(String[] values) {
        String instructions = values[0];
        return JSON.toJSON(isRobotBounded(instructions));
    }
}
