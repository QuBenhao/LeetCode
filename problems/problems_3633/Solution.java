package problems.problems_3633;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] landStartTime = jsonArrayToIntArray(inputJsonValues[0]);
		int[] landDuration = jsonArrayToIntArray(inputJsonValues[1]);
		int[] waterStartTime = jsonArrayToIntArray(inputJsonValues[2]);
		int[] waterDuration = jsonArrayToIntArray(inputJsonValues[3]);
        return JSON.toJSON(earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration));
    }
}
