package problems.problems_871;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int target = Integer.parseInt(inputJsonValues[0]);
		int startFuel = Integer.parseInt(inputJsonValues[1]);
		int[][] stations = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(minRefuelStops(target, startFuel, stations));
    }
}
