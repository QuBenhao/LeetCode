package problems.problems_2748;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int gcb(int a, int b) {
        return b == 0 ? a : gcb(b, a % b);
    }

    public int countBeautifulPairs(int[] nums) {
        int ans = 0;
        int[] counter = new int[10];
        for (int num: nums) {
            int cur = num % 10;
            for (int i = 1; i < 10; i++) {
                if (counter[i] > 0 && gcb(cur, i) == 1) {
                    ans += counter[i];
                }
            }
            while (num >= 10) {
                num /= 10;
            }
            counter[num]++;
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(countBeautifulPairs(nums));
    }
}
