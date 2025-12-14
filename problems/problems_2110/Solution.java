package problems.problems_2110;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long getDescentPeriods(int[] prices) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] prices = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(getDescentPeriods(prices));
    }
}
