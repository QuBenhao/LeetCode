package problems.problems_1139;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int largest1BorderedSquare(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] preRow = new int[m][n + 1], preCol = new int[m + 1][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                preRow[i][j + 1] = preRow[i][j] + grid[i][j];
                preCol[i + 1][j] = preCol[i][j] + grid[i][j];
            }
        }
        for (int d = Math.min(m, n); d > 0; d--) {
            for (int i = 0; i + d <= m; i++) {
                for (int j = 0; j + d <= n; j++) {
                    if (preRow[i][j + d] - preRow[i][j] == d && preRow[i + d - 1][j + d] - preRow[i + d - 1][j] == d
                            && preCol[i + d][j] - preCol[i][j] == d && preCol[i + d][j + d - 1] - preCol[i][j + d - 1] == d) {
                        return d * d;
                    }
                }
            }
        }
        return 0;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] grid = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(largest1BorderedSquare(grid));
    }
}
