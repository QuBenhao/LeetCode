package problems.problems_2398;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] chargeTimes = jsonArrayToIntArray(inputJsonValues[0]);
		int[] runningCosts = jsonArrayToIntArray(inputJsonValues[1]);
		long budget = Long.parseLong(inputJsonValues[2]);
        return JSON.toJSON(maximumRobots(chargeTimes, runningCosts, budget));
    }
}
