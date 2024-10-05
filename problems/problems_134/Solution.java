package problems.problems_134;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int canCompleteCircuit(int[] gas, int[] cost) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] gas = jsonArrayToIntArray(inputJsonValues[0]);
		int[] cost = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(canCompleteCircuit(gas, cost));
    }
}
