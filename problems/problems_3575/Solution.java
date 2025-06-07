package problems.problems_3575;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int goodSubtreeSum(int[] vals, int[] par) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] vals = jsonArrayToIntArray(inputJsonValues[0]);
		int[] par = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(goodSubtreeSum(vals, par));
    }
}
