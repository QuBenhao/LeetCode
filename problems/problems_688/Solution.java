package problems.problems_688;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double knightProbability(int n, int k, int row, int column) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int row = Integer.parseInt(inputJsonValues[2]);
		int column = Integer.parseInt(inputJsonValues[3]);
        return JSON.toJSON(knightProbability(n, k, row, column));
    }
}
