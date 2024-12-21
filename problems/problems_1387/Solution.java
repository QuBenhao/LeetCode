package problems.problems_1387;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int getKth(int lo, int hi, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int lo = Integer.parseInt(inputJsonValues[0]);
		int hi = Integer.parseInt(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(getKth(lo, hi, k));
    }
}
