package problems.problems_2274;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxConsecutive(int bottom, int top, int[] special) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int bottom = Integer.parseInt(inputJsonValues[0]);
		int top = Integer.parseInt(inputJsonValues[1]);
		int[] special = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(maxConsecutive(bottom, top, special));
    }
}
