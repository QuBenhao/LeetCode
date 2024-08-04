package problems.problems_2808;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumSeconds(List<Integer> nums) {
        int n = nums.size();
        Map<Integer, List<Integer>> idxMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            if (!idxMap.containsKey(nums.get(i))) {
                idxMap.put(nums.get(i), new ArrayList<>());
            }
            idxMap.get(nums.get(i)).add(i);
        }
        int ans = n;
        for (List<Integer> idxList : idxMap.values()) {
            int cur = idxList.getFirst() + n - idxList.getLast();
            for (int i = 1; i < idxList.size(); i++) {
                cur = Math.max(cur, idxList.get(i) - idxList.get(i - 1));
            }
            ans = Math.min(ans, cur);
        }
        return ans / 2;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Integer> nums = jsonArrayToIntList(inputJsonValues[0]);
        return JSON.toJSON(minimumSeconds(nums));
    }
}
