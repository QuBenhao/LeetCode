package problems.problems_3296;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minNumberOfSeconds(int mountainHeight, int[] workerTimes) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int mountainHeight = Integer.parseInt(inputJsonValues[0]);
		int[] workerTimes = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minNumberOfSeconds(mountainHeight, workerTimes));
    }
}
