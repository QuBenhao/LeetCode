package problems.problems_864;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int[][] DIRS = {
        {0, 1},  // right
        {1, 0},  // down
        {0, -1}, // left
        {-1, 0}  // up
    };

    public int shortestPathAllKeys(String[] grid) {
        int m = grid.length, n = grid[0].length();
        int goals = 0;
        Deque<int[]> queue = new ArrayDeque<>();
        boolean[][][] visited = new boolean[m][n][1 << 6];
        boolean[][] blocked = new boolean[m][n];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                char c = grid[i].charAt(j);
                if (c == '@') {
                    queue.offerLast(new int[]{i, j, 0});
                    visited[i][j][0] = true;
                } else if (c >= 'a' && c <= 'f') {
                    goals |= 1 << (c - 'a');
                } else if (c == '#') {
                    blocked[i][j] = true;
                }
            }
        }
        for (int steps = 0; !queue.isEmpty(); ++steps) {
            int size = queue.size();
            for (int i = 0; i < size; ++i) {
                int[] state = queue.pollFirst();
                int x = state[0], y = state[1], keys = state[2];
                if (keys == goals) {
                    return steps;
                }
                for (int[] dir : DIRS) {
                    int nx = x + dir[0], ny = y + dir[1];
                    if (nx < 0 || nx >= m || ny < 0 || ny >= n || blocked[nx][ny]) {
                        continue;
                    }
                    char c = grid[nx].charAt(ny);
                    if (c >= 'A' && c <= 'F' && ((keys >> (c - 'A')) & 1) == 0) {
                        continue;
                    }
                    int newKeys = keys;
                    if (c >= 'a' && c <= 'f') {
                        newKeys |= 1 << (c - 'a');
                        if (newKeys == goals) {
                            return steps + 1; // Found all keys
                        }
                    }
                    if (!visited[nx][ny][newKeys]) {
                        visited[nx][ny][newKeys] = true;
                        queue.offerLast(new int[]{nx, ny, newKeys});
                    }
                }
            }
        }
        return -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] grid = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(shortestPathAllKeys(grid));
    }
}
