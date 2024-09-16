package problems.problems_815;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numBusesToDestination(int[][] routes, int source, int target) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] routes = jsonArrayToInt2DArray(inputJsonValues[0]);
		int source = Integer.parseInt(inputJsonValues[1]);
		int target = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(numBusesToDestination(routes, source, target));
    }
}
