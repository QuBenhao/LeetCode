package problems.problems_2225;

import com.alibaba.fastjson.JSON;
import qubhjava.BaseSolution;

import java.util.*;


public class Solution extends BaseSolution {
    public List<List<Integer>> findWinners(int[][] matches) {
        Map<Integer, Integer> cnts = new HashMap<>();
        for (int[] match : matches) {
            cnts.put(match[1], cnts.getOrDefault(match[1], 0) + 1);
            cnts.put(match[0], cnts.getOrDefault(match[0], 0));
        }
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(new ArrayList<>());
        ans.add(new ArrayList<>());
        cnts.forEach((k, v) -> {
            if (v < 2)
                ans.get(v).add(k);
        });
        Collections.sort(ans.get(0));
        Collections.sort(ans.get(1));
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[][] matches = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(findWinners(matches));
    }
}
