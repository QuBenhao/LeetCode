package problems.problems_575;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int distributeCandies(int[] candyType) {
        Set<Integer> set = new HashSet<>();
        for (int t: candyType) {
            set.add(t);
        }
        return Math.min(set.size(), candyType.length / 2);
    }

    @Override
    public Object solve(String[] values) {
        int[] candyType = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(distributeCandies(candyType));
    }
}
