package problems.problems_1578;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;

public class Solution extends BaseSolution {
    public int minCost(String colors, int[] neededTime) {
        int ans = 0;
        int n = colors.length();
        for (int i = 0, j = 0; i < n - 1; i = j) {
            for (j = i + 1; j < n && colors.charAt(i) == colors.charAt(j); j++) {
                if (neededTime[i] < neededTime[j]) {
                    ans += neededTime[i];
                    i = j;
                } else {
                    ans += neededTime[j];
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String colors = jsonStringToString(inputJsonValues[0]);
        int[] neededTime = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minCost(colors, neededTime));
    }
}
