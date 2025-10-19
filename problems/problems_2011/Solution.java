package problems.problems_2011;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int finalValueAfterOperations(String[] operations) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operations = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(finalValueAfterOperations(operations));
    }
}
