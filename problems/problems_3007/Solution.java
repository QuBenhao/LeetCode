package problems.problems_3007;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long findMaximumNumber(long k, int x) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long k = Long.parseLong(inputJsonValues[0]);
		int x = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(findMaximumNumber(k, x));
    }
}
