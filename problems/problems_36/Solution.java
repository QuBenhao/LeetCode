package problems.problems_36;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int N = 9;
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < N; i++) {
            int r = 0, c = 0, b = 0;
            for (int j = 0; j < N; j++) {
                if (board[i][j] != '.') {
                    int v = 1 << (board[i][j] - '1');
                    if ((r & v) != 0) return false;
                    r |= v;
                }
                if (board[j][i] != '.') {
                    int v = 1 << (board[j][i] - '1');
                    if ((c & v) != 0) return false;
                    c |= v;
                }
                int bi = (i / 3) * 3 + j / 3;
                int bj = (i % 3) * 3 + j % 3;
                if (board[bi][bj] != '.') {
                    int v = 1 << (board[bi][bj] - '1');
                    if ((b & v) != 0) return false;
                    b |= v;
                }
            }
        }
        return true;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] board = jsonArrayToChar2DArray(inputJsonValues[0]);
        return JSON.toJSON(isValidSudoku(board));
    }
}
