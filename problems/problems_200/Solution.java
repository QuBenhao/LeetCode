package problems.problems_200;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int[][] DIRECTIONS = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    public int numIslands(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    ans++;
                    dfs(grid, i, j);
                }
            }
        }
        return ans;
    }

    private void dfs(char[][] grid, int x, int y) {
        int m = grid.length, n = grid[0].length;
        grid[x][y] = '0';
        for (int[] dir: DIRECTIONS) {
            int nx = x + dir[0], ny = y + dir[1];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == '1') {
                dfs(grid, nx, ny);
            }
        }
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] grid = jsonArrayToChar2DArray(inputJsonValues[0]);
        return JSON.toJSON(numIslands(grid));
    }
}
