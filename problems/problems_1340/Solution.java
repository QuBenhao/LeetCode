package problems.problems_1340;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxJumps(int[] arr, int d) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
		int d = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxJumps(arr, d));
    }
}
