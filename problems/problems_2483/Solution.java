package problems.problems_2483;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int bestClosingTime(String customers) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String customers = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(bestClosingTime(customers));
    }
}
