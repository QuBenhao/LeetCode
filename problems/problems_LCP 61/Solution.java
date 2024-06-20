package problems.problems_LCP 61;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int temperatureTrend(int[] temperatureA, int[] temperatureB) {

    }

    @Override
    public Object solve(String[] values) {
        int[] temperatureA = jsonArrayToIntArray(values[0]);
		int[] temperatureB = jsonArrayToIntArray(values[1]);
        return JSON.toJSON(temperatureTrend(temperatureA, temperatureB));
    }
}
