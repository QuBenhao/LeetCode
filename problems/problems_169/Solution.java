package problems.problems_169;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int majorityElement(int[] nums) {
        int ans = 0, cnt = 0;
        for (int num: nums) {
            if (cnt != 0 && ans != num) {
                cnt--;
            } else {
                ans = num;
                cnt++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(majorityElement(nums));
    }
}
