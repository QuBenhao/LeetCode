package problems.problems_3354;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countValidSelections(int[] nums) {
        int total = 0;
        for (int x : nums) {
            total += x;
        }

        int ans = 0;
        int pre = 0;
        for (int x : nums) {
            if (x > 0) {
                pre += x;
            } else if (pre * 2 == total) {
                ans += 2;
            } else if (Math.abs(pre * 2 - total) == 1) {
                ans++;
            }
        }
        return ans;    
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(countValidSelections(nums));
    }
}
