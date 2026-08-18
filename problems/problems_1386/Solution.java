package problems.problems_1386;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] reservedSeats = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(maxNumberOfFamilies(n, reservedSeats));
    }
}
