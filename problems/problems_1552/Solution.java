package problems.problems_1552;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxDistance(int[] position, int m) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] position = jsonArrayToIntArray(inputJsonValues[0]);
		int m = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxDistance(position, m));
    }
}
