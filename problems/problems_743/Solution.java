package problems.problems_743;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int networkDelayTime(int[][] times, int n, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] times = jsonArrayToInt2DArray(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(networkDelayTime(times, n, k));
    }
}
