package problems.problems_3809;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] bestTower(int[][] towers, int[] center, int radius) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] towers = jsonArrayToInt2DArray(inputJsonValues[0]);
		int[] center = jsonArrayToIntArray(inputJsonValues[1]);
		int radius = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(bestTower(towers, center, radius));
    }
}
