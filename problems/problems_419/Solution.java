package problems.problems_419;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countBattleships(char[][] board) {
        int ans = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == 'X' && (i == 0 || board[i - 1][j] != 'X') && (j == 0 || board[i][j - 1] != 'X')) {
                    ans++;
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        char[][] board = jsonArrayToChar2DArray(values[0]);
        return JSON.toJSON(countBattleships(board));
    }
}
