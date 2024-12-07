package problems.problems_782;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int movesToChessboard(int[][] board) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] board = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(movesToChessboard(board));
    }
}
