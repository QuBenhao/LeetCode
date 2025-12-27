package problems.problems_2402;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int mostBooked(int n, int[][] meetings) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] meetings = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(mostBooked(n, meetings));
    }
}
