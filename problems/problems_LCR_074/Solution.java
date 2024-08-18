package problems.problems_LCR_074;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[][] merge(int[][] intervals) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] intervals = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(merge(intervals));
    }
}
