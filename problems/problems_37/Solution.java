package problems.problems_37;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int N = 9;
    public void solveSudoku(char[][] board) {
        int[] rows = new int[N];
        int[] cols = new int[N];
        int[] boxes = new int[N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                int v = 1 << (board[i][j] - '1');
                rows[i] |= v;
                cols[j] |= v;
                boxes[(i / 3) * 3 + (j / 3)] |= v;
            }
        }
        backtrack(board, rows, cols, boxes, 0, 0);
    }

    private boolean backtrack(char[][] board, int[] rows, int[] cols, int[] boxes, int i, int j) {
        if (i == N) {
            return true;
        }
        if (j == N) {
            return backtrack(board, rows, cols, boxes, i + 1, 0);
        }
        if (board[i][j] != '.') {
            return backtrack(board, rows, cols, boxes, i, j + 1);
        }
        for (int c = 0; c < N; ++c) {
            int v = 1 << c;
            int boxId = (i / 3) * 3 + (j / 3);
            if (((rows[i] & v) != 0) || ((cols[j] & v) != 0) || ((boxes[boxId] & v) != 0)) {
                continue;
            }
            char cr = (char)(c + '1');
            board[i][j] = cr;
            rows[i] |= v;
            cols[j] |= v;
            boxes[boxId] |= v;
            if (backtrack(board, rows, cols, boxes, i, j + 1)) {
                return true;
            }
            rows[i] &= ~v;
            cols[j] &= ~v;
            boxes[boxId] &= ~v;
        }
        board[i][j] = '.';
        return false;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] board = jsonArrayToChar2DArray(inputJsonValues[0]);
		solveSudoku(board);
        String[][] boardStr = new String[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                boardStr[i][j] = String.valueOf(board[i][j]);
            }
        }
        return JSON.toJSON(boardStr);
    }
}
