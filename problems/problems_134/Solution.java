package problems.problems_134;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        int total_tank = 0;
        int curr_tank = 0;
        int starting_station = 0;
        for (int i = 0; i < n; ++i) {
            total_tank += gas[i] - cost[i];
            curr_tank += gas[i] - cost[i];
            if (curr_tank < 0) {
                starting_station = i + 1;
                curr_tank = 0;
            }
        }
        return total_tank >= 0 ? starting_station : -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] gas = jsonArrayToIntArray(inputJsonValues[0]);
		int[] cost = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(canCompleteCircuit(gas, cost));
    }
}
