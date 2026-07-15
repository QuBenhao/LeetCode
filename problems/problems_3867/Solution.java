package problems.problems_3867;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public long gcdSum(int[] nums) {
        int n = nums.length;
        int[] pg = new int[n];
        int mx = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > mx) mx = nums[i];
            pg[i] = gcd(nums[i], mx);
        }
        Arrays.sort(pg);
        long ans = 0;
        int i = 0, j = n - 1;
        while (i < j) {
            ans += gcd(pg[i], pg[j]);
            i++;
            j--;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(gcdSum(nums));
    }
}
