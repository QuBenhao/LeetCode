package problems.problems_633;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean judgeSquareSum(int c) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int c = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(judgeSquareSum(c));
    }
}
