package problems.problems_LCP_61;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int temperatureTrend(int[] temperatureA, int[] temperatureB) {
        int ans = 0;
        for (int i = 1, cur = 0; i < temperatureA.length; i++) {
            int d1 = temperatureA[i] - temperatureA[i - 1], d2 = temperatureB[i] - temperatureB[i - 1];
            if (d1 * d2 > 0 || (d1 == 0 && d2 == 0)) {
                cur++;
                ans = Math.max(ans, cur);
            } else {
                cur = 0;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[] temperatureA = jsonArrayToIntArray(values[0]);
		int[] temperatureB = jsonArrayToIntArray(values[1]);
        return JSON.toJSON(temperatureTrend(temperatureA, temperatureB));
    }
}
