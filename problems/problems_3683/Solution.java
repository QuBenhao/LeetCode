package problems.problems_3683;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int earliestTime(int[][] tasks) {
        int mn = 201;
        for (int[] task: tasks) {
            mn = Math.min(mn, task[0] + task[1]);
        }
        return mn;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] tasks = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(earliestTime(tasks));
    }
}
