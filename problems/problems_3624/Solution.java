package problems.problems_3624;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] popcountDepth(long[] nums, long[][] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long[] nums = FIXME(inputJsonValues[0])
		long[][] queries = FIXME(inputJsonValues[1])
        return JSON.toJSON(popcountDepth(nums, queries));
    }
}
