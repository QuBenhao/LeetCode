package problems.problems_2943;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int m = Integer.parseInt(inputJsonValues[1]);
		int[] hBars = jsonArrayToIntArray(inputJsonValues[2]);
		int[] vBars = jsonArrayToIntArray(inputJsonValues[3]);
        return JSON.toJSON(maximizeSquareHoleArea(n, m, hBars, vBars));
    }
}
