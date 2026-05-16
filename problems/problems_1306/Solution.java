package problems.problems_1306;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canReach(int[] arr, int start) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
		int start = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(canReach(arr, start));
    }
}
