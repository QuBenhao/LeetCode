package problems.problems_474;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findMaxForm(String[] strs, int m, int n) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] strs = jsonArrayToStringArray(inputJsonValues[0]);
		int m = Integer.parseInt(inputJsonValues[1]);
		int n = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(findMaxForm(strs, m, n));
    }
}
