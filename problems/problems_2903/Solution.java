package problems.problems_2903;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findIndices(int[] nums, int indexDifference, int valueDifference) {

    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
		int indexDifference = Integer.parseInt(values[1]);
		int valueDifference = Integer.parseInt(values[2]);
        return JSON.toJSON(findIndices(nums, indexDifference, valueDifference));
    }
}
