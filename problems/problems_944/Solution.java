package problems.problems_944;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minDeletionSize(String[] strs) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] strs = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(minDeletionSize(strs));
    }
}
