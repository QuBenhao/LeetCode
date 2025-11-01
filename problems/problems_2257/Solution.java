package problems.problems_2257;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int m = Integer.parseInt(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
		int[][] guards = jsonArrayToInt2DArray(inputJsonValues[2]);
		int[][] walls = jsonArrayToInt2DArray(inputJsonValues[3]);
        return JSON.toJSON(countUnguarded(m, n, guards, walls));
    }
}
