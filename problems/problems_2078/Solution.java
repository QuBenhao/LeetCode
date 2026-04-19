package problems.problems_2078;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxDistance(int[] colors) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] colors = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxDistance(colors));
    }
}
