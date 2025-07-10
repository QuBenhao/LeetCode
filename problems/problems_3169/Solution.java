package problems.problems_3169;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countDays(int days, int[][] meetings) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int days = Integer.parseInt(inputJsonValues[0]);
		int[][] meetings = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(countDays(days, meetings));
    }
}
