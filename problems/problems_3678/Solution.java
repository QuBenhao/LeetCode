package problems.problems_3678;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int smallestAbsent(int[] nums) {
        Set<Integer> used = new HashSet<>();
        int sm = 0, mx = 0;
        for (int num: nums) {
            used.add(num);
            sm += num;
            mx = Math.max(num, mx);
        }
        int avg = (int)Math.ceil((double)(sm + 1) / nums.length);
        for (int i = Math.max(1, avg); i <= mx + 1; ++i) {
            if (!used.contains(i)) {
                return i;
            }
        }
        return 1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(smallestAbsent(nums));
    }
}
