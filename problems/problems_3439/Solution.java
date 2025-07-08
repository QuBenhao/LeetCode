package problems.problems_3439;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxFreeTime(int eventTime, int k, int[] startTime, int[] endTime) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int eventTime = Integer.parseInt(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int[] startTime = jsonArrayToIntArray(inputJsonValues[2]);
		int[] endTime = jsonArrayToIntArray(inputJsonValues[3]);
        return JSON.toJSON(maxFreeTime(eventTime, k, startTime, endTime));
    }
}
