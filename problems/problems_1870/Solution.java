package problems.problems_1870;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minSpeedOnTime(int[] dist, double hour) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] dist = jsonArrayToIntArray(inputJsonValues[0]);
		double hour = Double.parseDouble(inputJsonValues[1]);
        return JSON.toJSON(minSpeedOnTime(dist, hour));
    }
}
