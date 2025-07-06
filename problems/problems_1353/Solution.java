package problems.problems_1353;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxEvents(int[][] events) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] events = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(maxEvents(events));
    }
}
