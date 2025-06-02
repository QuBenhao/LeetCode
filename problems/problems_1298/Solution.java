package problems.problems_1298;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxCandies(int[] status, int[] candies, int[][] keys, int[][] containedBoxes, int[] initialBoxes) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] status = jsonArrayToIntArray(inputJsonValues[0]);
		int[] candies = jsonArrayToIntArray(inputJsonValues[1]);
		int[][] keys = jsonArrayToInt2DArray(inputJsonValues[2]);
		int[][] containedBoxes = jsonArrayToInt2DArray(inputJsonValues[3]);
		int[] initialBoxes = jsonArrayToIntArray(inputJsonValues[4]);
        return JSON.toJSON(maxCandies(status, candies, keys, containedBoxes, initialBoxes));
    }
}
