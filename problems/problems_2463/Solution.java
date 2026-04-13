package problems.problems_2463;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Integer> robot = jsonArrayToIntList(inputJsonValues[0]);
		int[][] factory = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(minimumTotalDistance(robot, factory));
    }
}
