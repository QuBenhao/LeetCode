package problems.problems_1096;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<String> braceExpansionII(String expression) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String expression = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(braceExpansionII(expression));
    }
}
