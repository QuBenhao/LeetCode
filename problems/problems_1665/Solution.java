package problems.problems_1665;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumEffort(int[][] tasks) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] tasks = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(minimumEffort(tasks));
    }
}
