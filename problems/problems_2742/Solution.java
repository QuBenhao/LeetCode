package problems.problems_2742;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int paintWalls(int[] cost, int[] time) {

    }

    @Override
    public Object solve(String[] values) {
        int[] cost = jsonArrayToIntArray(values[0]);
		int[] time = jsonArrayToIntArray(values[1]);
        return JSON.toJSON(paintWalls(cost, time));
    }
}
