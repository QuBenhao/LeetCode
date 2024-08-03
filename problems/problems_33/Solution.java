package problems.problems_33;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int search(int[] nums, int target) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int target = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(search(nums, target));
    }
}
