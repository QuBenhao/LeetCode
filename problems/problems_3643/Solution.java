package problems.problems_3643;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] grid = jsonArrayToInt2DArray(inputJsonValues[0]);
		int x = Integer.parseInt(inputJsonValues[1]);
		int y = Integer.parseInt(inputJsonValues[2]);
		int k = Integer.parseInt(inputJsonValues[3]);
        return JSON.toJSON(reverseSubmatrix(grid, x, y, k));
    }
}
