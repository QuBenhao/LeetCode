package problems.problems_2961;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int fastPowMod(int base, int exp, int mod) {
        int res = 1;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (int) ((long) res * base % mod);
            }
            base = (int) ((long) base * base % mod);
            exp >>= 1;
        }
        return res;
    }
    public List<Integer> getGoodIndices(int[][] variables, int target) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < variables.length; i++) {
            int a = variables[i][0], b = variables[i][1], c = variables[i][2], m = variables[i][3];
            if (fastPowMod(fastPowMod(a, b, 10), c, m) == target) {
                res.add(i);
            }
        }
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] variables = jsonArrayToInt2DArray(inputJsonValues[0]);
		int target = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(getGoodIndices(variables, target));
    }
}
