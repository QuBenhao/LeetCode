package problems.problems_3355;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isZeroArray(int[] nums, int[][] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int[][] queries = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(isZeroArray(nums, queries));
    }
}
