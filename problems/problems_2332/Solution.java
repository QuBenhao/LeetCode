package problems.problems_2332;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int latestTimeCatchTheBus(int[] buses, int[] passengers, int capacity) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] buses = jsonArrayToIntArray(inputJsonValues[0]);
		int[] passengers = jsonArrayToIntArray(inputJsonValues[1]);
		int capacity = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(latestTimeCatchTheBus(buses, passengers, capacity));
    }
}
