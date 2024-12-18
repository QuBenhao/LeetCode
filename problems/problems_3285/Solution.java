package problems.problems_3285;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> stableMountains(int[] height, int threshold) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] height = jsonArrayToIntArray(inputJsonValues[0]);
		int threshold = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(stableMountains(height, threshold));
    }
}
