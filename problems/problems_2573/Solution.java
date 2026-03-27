package problems.problems_2573;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String findTheString(int[][] lcp) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] lcp = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(findTheString(lcp));
    }
}
