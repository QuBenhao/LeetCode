package problems.problems_1922;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countGoodNumbers(long n) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long n = Long.parseLong(inputJsonValues[0]);
        return JSON.toJSON(countGoodNumbers(n));
    }
}
