package problems.problems_3461;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean hasSameDigits(String s) {
        int n = s.length();
        int[] nums = new int[n];
        for (int i = 0; i < n; ++i) {
            nums[i] = s.charAt(i) - '0';
        }
        for (; n > 2; --n) {
            for (int i = 0; i < n - 1; ++i) {
                nums[i] = (nums[i] + nums[i + 1]) % 10;
            }
        }
        return nums[0] == nums[1];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(hasSameDigits(s));
    }
}
