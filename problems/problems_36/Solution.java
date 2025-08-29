package problems.problems_36;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isValidSudoku(char[][] board) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] board = jsonArrayToChar2DArray(inputJsonValues[0]);
        return JSON.toJSON(isValidSudoku(board));
    }
}
