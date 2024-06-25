package demo.demo_1;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] twoSum(int[] nums, int target) {

    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
		int target = Integer.parseInt(values[1]);
        return JSON.toJSON(twoSum(nums, target));
    }
}
