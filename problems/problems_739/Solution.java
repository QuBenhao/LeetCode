package problems.problems_739;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] dailyTemperatures(int[] temperatures) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] temperatures = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(dailyTemperatures(temperatures));
    }
}
