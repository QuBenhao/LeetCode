package problems.problems_2071;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxTaskAssign(int[] tasks, int[] workers, int pills, int strength) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] tasks = jsonArrayToIntArray(inputJsonValues[0]);
		int[] workers = jsonArrayToIntArray(inputJsonValues[1]);
		int pills = Integer.parseInt(inputJsonValues[2]);
		int strength = Integer.parseInt(inputJsonValues[3]);
        return JSON.toJSON(maxTaskAssign(tasks, workers, pills, strength));
    }
}
