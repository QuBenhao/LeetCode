package problems.problems_3871;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long countCommas(long n) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long n = Long.parseLong(inputJsonValues[0]);
        return JSON.toJSON(countCommas(n));
    }
}
