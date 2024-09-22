package problems.problems_997;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findJudge(int n, int[][] trust) {
        int[] counter = new int[n + 1];
        for (int[] t : trust) {
            counter[t[0]]--;
            counter[t[1]]++;
        }
        for (int i = 1; i <= n; i++) {
            if (counter[i] == n - 1) {
                return i;
            }
        }
        return -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] trust = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(findJudge(n, trust));
    }
}
