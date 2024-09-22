package problems.problems_1014;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxScoreSightseeingPair(int[] values) {
        int ans = 0, left = values[0];
        for (int i = 1; i < values.length; i++) {
            ans = Math.max(ans, left + values[i] - i);
            left = Math.max(left, values[i] + i);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] values = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxScoreSightseeingPair(values));
    }
}
