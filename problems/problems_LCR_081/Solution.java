package problems.problems_LCR_081;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] candidates = jsonArrayToIntArray(inputJsonValues[0]);
		int target = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(combinationSum(candidates, target));
    }
}
