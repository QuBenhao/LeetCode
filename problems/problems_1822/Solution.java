package problems.problems_1822;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int arraySign(int[] nums) {
        int cnt = 0;
        for (int num: nums) {
            if (num == 0) {
                return 0;
            } else if (num < 0) {
                cnt++;
            }
        }
        return (cnt & 1) == 1 ? -1 : 1;
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(arraySign(nums));
    }
}
