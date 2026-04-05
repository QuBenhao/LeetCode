package problems.problems_874;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int robotSim(int[] commands, int[][] obstacles) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] commands = jsonArrayToIntArray(inputJsonValues[0]);
		int[][] obstacles = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(robotSim(commands, obstacles));
    }
}
