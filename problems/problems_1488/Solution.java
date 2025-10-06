package problems.problems_1488;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] avoidFlood(int[] rains) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] rains = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(avoidFlood(rains));
    }
}
