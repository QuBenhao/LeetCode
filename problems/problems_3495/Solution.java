package problems.problems_3495;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minOperations(int[][] queries) {
        long ans = 0;
        for (int[] query: queries) {
            int mx = (33 - Integer.numberOfLeadingZeros(query[1])) / 2;
            long sm = preSum(query[1]) - preSum(query[0] - 1);
            ans += helper(sm, mx);
        }
        return ans;
    }

    private long helper(long sum, long max) {
        return max > sum - max ? max : (sum + 1) / 2;
    }

    private long preSum(int num) {
        if (num == 0) {
            return 0;
        }
        int b = (33 - Integer.numberOfLeadingZeros(num)) / 2;
        int last = (1 << (2 * (b - 1))) - 1;
        return preSum(last) + 1L * b * (num - last);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] queries = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(minOperations(queries));
    }
}
