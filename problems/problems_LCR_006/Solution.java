package problems.problems_LCR_006;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] twoSum(int[] numbers, int target) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] numbers = jsonArrayToIntArray(inputJsonValues[0]);
		int target = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(twoSum(numbers, target));
    }
}
