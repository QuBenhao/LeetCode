package problems.problems_3127;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canMakeSquare(char[][] grid) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] grid = jsonArrayToChar2DArray(inputJsonValues[0]);
        return JSON.toJSON(canMakeSquare(grid));
    }
}
