package problems.problems_3186;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maximumTotalDamage(int[] power) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] power = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maximumTotalDamage(power));
    }
}
