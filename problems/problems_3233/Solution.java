package problems.problems_3233;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int nonSpecialCount(int l, int r) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int l = Integer.parseInt(inputJsonValues[0]);
		int r = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(nonSpecialCount(l, r));
    }
}
