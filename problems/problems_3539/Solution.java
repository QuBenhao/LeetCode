package problems.problems_3539;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int magicalSum(int m, int k, int[] nums) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int m = Integer.parseInt(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int[] nums = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(magicalSum(m, k, nums));
    }
}
