package problems.problems_2234;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maximumBeauty(int[] flowers, long newFlowers, int target, int full, int partial) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] flowers = jsonArrayToIntArray(inputJsonValues[0]);
		long newFlowers = Long.parseLong(inputJsonValues[1]);
		int target = Integer.parseInt(inputJsonValues[2]);
		int full = Integer.parseInt(inputJsonValues[3]);
		int partial = Integer.parseInt(inputJsonValues[4]);
        return JSON.toJSON(maximumBeauty(flowers, newFlowers, target, full, partial));
    }
}
