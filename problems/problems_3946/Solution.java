package problems.problems_3946;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumSaleItems(int[][] items, int budget) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] items = jsonArrayToInt2DArray(inputJsonValues[0]);
		int budget = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maximumSaleItems(items, budget));
    }
}
