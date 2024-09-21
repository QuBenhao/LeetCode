package problems.problems_2374;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int edgeScore(int[] edges) {
        int ans = 0, n = edges.length;
        long[] counter = new long[n];
        for (int i = 0; i < n; i++) {
            counter[edges[i]] += i;
            if (counter[edges[i]] > counter[ans]) {
                ans = edges[i];
            } else if (counter[edges[i]] == counter[ans]) {
                ans = Math.min(ans, edges[i]);
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] edges = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(edgeScore(edges));
    }
}
