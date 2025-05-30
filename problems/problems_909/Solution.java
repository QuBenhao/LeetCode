package problems.problems_909;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int snakesAndLadders(int[][] board) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] board = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(snakesAndLadders(board));
    }
}
