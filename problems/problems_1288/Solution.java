package problems.problems_1288;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int removeCoveredIntervals(int[][] intervals) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] intervals = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(removeCoveredIntervals(intervals));
    }
}
