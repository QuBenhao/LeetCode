package problems.problems_762;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    static boolean[] hash = new boolean[40];
    static {
        int[] nums = new int[]{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
        for (int x : nums) hash[x] = true;
    }
    public int countPrimeSetBits(int left, int right) {
        int ans = 0;
        for (int i = left; i <= right; i++) {
            int x = i;
            x = (x & 0x55555555) + ((x >>> 1)  & 0x55555555);
            x = (x & 0x33333333) + ((x >>> 2)  & 0x33333333);
            x = (x & 0x0f0f0f0f) + ((x >>> 4)  & 0x0f0f0f0f);
            x = (x & 0x00ff00ff) + ((x >>> 8)  & 0x00ff00ff);
            x = (x & 0x0000ffff) + ((x >>> 16) & 0x0000ffff);
            if (hash[x]) ans++;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int left = Integer.parseInt(inputJsonValues[0]);
		int right = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(countPrimeSetBits(left, right));
    }
}
