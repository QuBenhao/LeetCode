package problems.problems_2766;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> relocateMarbles(int[] nums, int[] moveFrom, int[] moveTo) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int[] moveFrom = jsonArrayToIntArray(inputJsonValues[1]);
		int[] moveTo = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(relocateMarbles(nums, moveFrom, moveTo));
    }
}
