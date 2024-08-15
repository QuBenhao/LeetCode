package problems.problems_3117;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumValueSum(int[] nums, int[] andValues) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int[] andValues = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minimumValueSum(nums, andValues));
    }
}
