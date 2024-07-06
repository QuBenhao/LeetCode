package problems.problems_1958;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean checkMove(char[][] board, int rMove, int cMove, char color) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] board = jsonArrayToChar2DArray(inputJsonValues[0]);
		int rMove = Integer.parseInt(inputJsonValues[1]);
		int cMove = Integer.parseInt(inputJsonValues[2]);
		char color = FIXME(inputJsonValues[3])
        return JSON.toJSON(checkMove(board, rMove, cMove, color));
    }
}
