package problems.problems_3086;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumMoves(int[] nums, int k, int maxChanges) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int maxChanges = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(minimumMoves(nums, k, maxChanges));
    }
}
