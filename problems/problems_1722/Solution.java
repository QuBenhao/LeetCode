package problems.problems_1722;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] source = jsonArrayToIntArray(inputJsonValues[0]);
		int[] target = jsonArrayToIntArray(inputJsonValues[1]);
		int[][] allowedSwaps = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(minimumHammingDistance(source, target, allowedSwaps));
    }
}
