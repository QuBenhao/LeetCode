package problems.problems_79;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean exist(char[][] board, String word) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] board = jsonArrayToChar2DArray(inputJsonValues[0]);
		String word = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(exist(board, word));
    }
}
