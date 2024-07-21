package problems.problems_1186;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumSum(int[] arr) {
        int ans = Integer.MIN_VALUE / 2, dp0 = ans, dp1 = ans;
        for (int num: arr) {
            dp1 = Math.max(dp1 + num, dp0);
            dp0 = Math.max(dp0 + num, num);
            ans = Math.max(ans, Math.max(dp0, dp1));
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maximumSum(arr));
    }
}
