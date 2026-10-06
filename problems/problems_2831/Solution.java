package problems.problems_2831;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int longestEqualSubarray(List<Integer> nums, int k) {
        int n = nums.size();
        List<Integer>[] posLists = new ArrayList[n + 1];
        Arrays.setAll(posLists, i -> new ArrayList<>());
        for (int i = 0; i < n; i++) {
            int x = nums.get(i);
            posLists[x].add(i - posLists[x].size());
        }

        int ans = 0;
        for (List<Integer> pos : posLists) {
            if (pos.size() <= ans) {
                continue; // Cannot increase ans
            }
            int left = 0;
            for (int right = 0; right < pos.size(); right++) {
                while (pos.get(right) - pos.get(left) > k) { // Too many elements would need to be deleted
                    left++;
                }
                ans = Math.max(ans, right - left + 1);
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        List<Integer> nums = jsonArrayToIntList(values[0]);
        int k = Integer.parseInt(values[1]);
        return JSON.toJSON(longestEqualSubarray(nums, k));
    }
}
