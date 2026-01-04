package problems.problems_3801;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minMergeCost(int[][] lists) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] lists = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(minMergeCost(lists));
    }
}
