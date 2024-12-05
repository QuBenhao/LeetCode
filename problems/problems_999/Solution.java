package problems.problems_999;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numRookCaptures(char[][] board) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] board = jsonArrayToChar2DArray(inputJsonValues[0]);
        return JSON.toJSON(numRookCaptures(board));
    }
}
