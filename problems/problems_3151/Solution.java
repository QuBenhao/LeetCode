package problems.problems_3151;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isArraySpecial(int[] nums) {
        int last = nums[0] & 1;
        for (int i = 1; i < nums.length; i++) {
            if ((nums[i] & 1) == last) {
                return false;
            }
            last ^= 1;
        }
        return true;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(isArraySpecial(nums));
    }
}
