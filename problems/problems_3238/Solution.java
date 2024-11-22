package problems.problems_3238;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int winningPlayerCount(int n, int[][] pick) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] pick = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(winningPlayerCount(n, pick));
    }
}
