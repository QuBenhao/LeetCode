package problems.problems_79;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int[][] DIRECTIONS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private boolean backtrack(char[][] board, String word, int i, int j, int k) {
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || word.charAt(k) != board[i][j]) {
            return false;
        }
        if (k == word.length() - 1) {
            return true;
        }
        char tmp = board[i][j];
        board[i][j] = ' ';
        for (int[] direction : DIRECTIONS) {
            if (backtrack(board, word, i + direction[0], j + direction[1], k + 1)) {
                return true;
            }
        }
        board[i][j] = tmp;
        return false;
    }

    public boolean exist(char[][] board, String word) {
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (backtrack(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] board = jsonArrayToChar2DArray(inputJsonValues[0]);
		String word = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(exist(board, word));
    }
}
