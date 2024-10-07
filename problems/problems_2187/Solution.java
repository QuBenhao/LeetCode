package problems.problems_2187;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumTime(int[] time, int totalTrips) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] time = jsonArrayToIntArray(inputJsonValues[0]);
		int totalTrips = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minimumTime(time, totalTrips));
    }
}
