package problems.problems_3619;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int[][] DIRECTIONS = {
        {0, 1},   // right
        {1, 0},   // down
        {0, -1},  // left
        {-1, 0}   // up
    };

    private int dfs(int[][] grid, boolean[][] visited, int x, int y, int k) {
        int cur = grid[x][y] % k;
        for (int[] dir : DIRECTIONS) {
            int newX = x + dir[0];
            int newY = y + dir[1];
            if (newX >= 0 && newX < grid.length && newY >= 0 && newY < grid[0].length &&
                !visited[newX][newY] && grid[newX][newY] != 0) {
                visited[newX][newY] = true;
                cur = (cur + dfs(grid, visited, newX, newY, k)) % k;
            }
        }
        return cur;
    }

    public int countIslands(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 0 && !visited[i][j]) {
                    visited[i][j] = true;
                    int sum = dfs(grid, visited, i, j, k);
                    if (sum == 0) {
                        ans++;
                    }
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] grid = jsonArrayToInt2DArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(countIslands(grid, k));
    }
}
