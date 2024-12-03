package problems.problems_2056;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countCombinations(String[] pieces, int[][] positions) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] pieces = jsonArrayToStringArray(inputJsonValues[0]);
		int[][] positions = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(countCombinations(pieces, positions));
    }
}
