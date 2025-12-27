package problems.problems_Interview_16__06;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int smallestDifference(int[] a, int[] b) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] a = jsonArrayToIntArray(inputJsonValues[0]);
		int[] b = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(smallestDifference(a, b));
    }
}
