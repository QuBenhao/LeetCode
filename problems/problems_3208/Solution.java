package problems.problems_3208;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfAlternatingGroups(int[] colors, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] colors = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(numberOfAlternatingGroups(colors, k));
    }
}
