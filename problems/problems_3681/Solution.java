package problems.problems_3681;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;

public class Solution extends BaseSolution {
    public int maxXorSubsequences(int[] nums) {
        int[] base = new int[32];
        for (int x : nums) {
            for (int i = 31; i >= 0; --i) {
                if (((x >> i) & 1) == 1) {
                    if (base[i] != 0) {
                        x ^= base[i];
                    } else {
                        base[i] = x;
                        break;
                    }
                }

            }
        }
        int ans = 0;
        for (int i = 31; i >= 0; --i) {
            if (base[i] != 0 && ((ans >> i) & 1) == 0) {
                ans ^= base[i];
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxXorSubsequences(nums));
    }
}
