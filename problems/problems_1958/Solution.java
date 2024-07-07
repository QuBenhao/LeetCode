package problems.problems_1958;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean checkMove(char[][] board, int rMove, int cMove, char color) {
        int[][] directions = new int[][]{{0, 1}, {1, 1}, {1, 0}, {-1, 1}, {0, -1}, {-1, -1}, {-1, 0}, {1, -1}};
        int m = board.length, n = board[0].length;
        for (int[] dir: directions) {
            int x = rMove + dir[0], y = cMove + dir[1];
            if (x < 0 || x >= m || y < 0 || y >= n || board[x][y] == '.' || board[x][y] == color) {
                continue;
            }
            while (x >= 0 && x < m && y >= 0 && y < n && board[x][y] != '.') {
                if (board[x][y] == color) {
                    return true;
                }
                x += dir[0];
                y += dir[1];
            }
        }
        return false;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] board = jsonArrayToChar2DArray(inputJsonValues[0]);
		int rMove = Integer.parseInt(inputJsonValues[1]);
		int cMove = Integer.parseInt(inputJsonValues[2]);
		char color = inputJsonValues[3].charAt(1);
        return JSON.toJSON(checkMove(board, rMove, cMove, color));
    }
}
