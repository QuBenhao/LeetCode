package problems.problems_3785;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minSwaps(int[] nums, int[] forbidden) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int[] forbidden = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minSwaps(nums, forbidden));
    }
}
