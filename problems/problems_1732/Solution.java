package problems.problems_1732;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int largestAltitude(int[] gain) {
        int ans = 0;
        int cur = 0;
        for (int g : gain) {
            cur += g;
            ans = Math.max(ans, cur);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] gain = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(largestAltitude(gain));
    }
}
