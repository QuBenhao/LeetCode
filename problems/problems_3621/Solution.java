package problems.problems_3621;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long popcountDepth(long n, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long n = Long.parseLong(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(popcountDepth(n, k));
    }
}
