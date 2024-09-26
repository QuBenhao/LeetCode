package problems.problems_2535;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int differenceOfSum(int[] nums) {
        int ans = 0;
        for (int num: nums) {
            ans += num;
            while (num > 0) {
                ans -= num % 10;
                num /= 10;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(differenceOfSum(nums));
    }
}
