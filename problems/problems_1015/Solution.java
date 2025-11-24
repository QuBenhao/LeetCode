package problems.problems_1015;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int smallestRepunitDivByK(int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int k = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(smallestRepunitDivByK(k));
    }
}
