package problems.problems_2300;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length;
        int[] ans = new int[n];
        int mx = 0;
        for (int p: potions) {
            mx = Math.max(mx, p);
        }
        int[] counts = new int[mx + 1];
        for (int p: potions) {
            ++counts[p];
        }
        for (int i = mx - 1; i >= 0; --i) {
            counts[i]+= counts[i + 1];
        }
        for (int i = 0; i < n; ++i) {
            long c = (success - 1) / spells[i] + 1;
            if (c > mx) {
                continue;
            }
            ans[i] = counts[(int)c];
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] spells = jsonArrayToIntArray(inputJsonValues[0]);
		int[] potions = jsonArrayToIntArray(inputJsonValues[1]);
		long success = Long.parseLong(inputJsonValues[2]);
        return JSON.toJSON(successfulPairs(spells, potions, success));
    }
}
