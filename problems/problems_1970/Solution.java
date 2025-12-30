package problems.problems_1970;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int latestDayToCross(int row, int col, int[][] cells) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int row = Integer.parseInt(inputJsonValues[0]);
		int col = Integer.parseInt(inputJsonValues[1]);
		int[][] cells = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(latestDayToCross(row, col, cells));
    }
}
