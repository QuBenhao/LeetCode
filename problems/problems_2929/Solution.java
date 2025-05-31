package problems.problems_2929;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long distributeCandies(int n, int limit) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int limit = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(distributeCandies(n, limit));
    }
}
