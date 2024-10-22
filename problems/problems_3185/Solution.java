package problems.problems_3185;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long countCompleteDayPairs(int[] hours) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] hours = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(countCompleteDayPairs(hours));
    }
}
