package problems.problems_887;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int superEggDrop(int k, int n) {
        int[] f = new int[k + 1];
        for (int i = 1; ; i++) {
            for (int j = k; j > 0; j--) {
                f[j] += f[j - 1] + 1;
            }
            if (f[k] >= n) {
                return i;
            }
        }
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int k = Integer.parseInt(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(superEggDrop(k, n));
    }
}
