package problems.problems_1111;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] maxDepthAfterSplit(String seq) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String seq = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(maxDepthAfterSplit(seq));
    }
}
