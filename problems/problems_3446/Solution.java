package problems.problems_3446;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[][] sortMatrix(int[][] grid) {
        int n = grid.length;
        for (int i = 0; i < 2 * n - 1; ++i) {
            int row = i < n ? i : 0, col = i < n ? 0 : i - n + 1;
            List<Integer> diagonal = new ArrayList<>();
            for (int r = row, c = col; r < n && c < n; r++, c++) {
                diagonal.add(grid[r][c]);
            }
            if (i < n) {
                Collections.sort(diagonal, Collections.reverseOrder());
            } else {
                Collections.sort(diagonal);
            }
            for (int v : diagonal) {
                grid[row][col] = v;
                row++;
                col++;
            }
        }
        return grid;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] grid = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(sortMatrix(grid));
    }
}
