package problems.problems_3790;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minAllOneMultiple(int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int k = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(minAllOneMultiple(k));
    }
}
