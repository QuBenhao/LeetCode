package problems.problems_1706;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findBall(int[][] grid) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] grid = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(findBall(grid));
    }
}
