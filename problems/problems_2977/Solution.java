package problems.problems_2977;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumCost(String source, String target, String[] original, String[] changed, int[] cost) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String source = jsonStringToString(inputJsonValues[0]);
		String target = jsonStringToString(inputJsonValues[1]);
		String[] original = jsonArrayToStringArray(inputJsonValues[2]);
		String[] changed = jsonArrayToStringArray(inputJsonValues[3]);
		int[] cost = jsonArrayToIntArray(inputJsonValues[4]);
        return JSON.toJSON(minimumCost(source, target, original, changed, cost));
    }
}
