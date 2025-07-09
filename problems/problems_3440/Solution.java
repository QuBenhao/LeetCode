package problems.problems_3440;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxFreeTime(int eventTime, int[] startTime, int[] endTime) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int eventTime = Integer.parseInt(inputJsonValues[0]);
		int[] startTime = jsonArrayToIntArray(inputJsonValues[1]);
		int[] endTime = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(maxFreeTime(eventTime, startTime, endTime));
    }
}
