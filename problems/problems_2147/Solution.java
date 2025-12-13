package problems.problems_2147;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfWays(String corridor) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String corridor = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(numberOfWays(corridor));
    }
}
