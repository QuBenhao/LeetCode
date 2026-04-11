package problems.problems_3740;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class Solution extends BaseSolution {
    public int minimumDistance(int[] nums) {
        int ans = Integer.MAX_VALUE;
        Map<Integer, List<Integer>> record = new HashMap<>();
        for (int k = 0; k < nums.length; k++) {
            int num = nums[k];
            record.computeIfAbsent(num, x -> new ArrayList<>()).add(k);
            if (record.get(num).size() > 2) {
                int i = record.get(num).get(record.get(num).size() - 3);
                ans = Math.min(ans, (k - i) * 2);
            }
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minimumDistance(nums));
    }
}
