package problems.problems_2141;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maxRunTime(int n, int[] batteries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[] batteries = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(maxRunTime(n, batteries));
    }
}
