package problems.problems_2818;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MOD = 1_000_000_007;
    private static final int MAX_N = 100_001;
    private static final int[] omega = new int[MAX_N];
    static {
        for (int i = 2; i < MAX_N; ++i) {
            if (omega[i] == 0) {
                for (int j = i; j < MAX_N; j += i) {
                    omega[j]++;
                }
            }
        }
    }

    private long fastPow(long a, long b) {
        long res = 1;
        while (b > 0) {
            if ((b & 1) == 1) {
                res = res * a % MOD;
            }
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }

    public int maximumScore(List<Integer> nums, int k) {
        int n = nums.size();
        int[] counts = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        Integer[] idxes = new Integer[n];
        for (int i = 0; i < n; ++i) {
            idxes[i] = i;
            counts[i] = omega[nums.get(i)];
            left[i] = -1;
            right[i] = n;
        }
        Arrays.sort(idxes, (i, j) -> Integer.compare(nums.get(j), nums.get(i)));
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; ++i) {
            while (!stack.isEmpty() && counts[stack.peek()] < counts[i]) {
                right[stack.pop()] = i;
            }
            if (!stack.isEmpty()) {
                left[i] = stack.peek();
            }
            stack.push(i);
        }
        long ans = 1;
        for (int idx : idxes) {
            if (nums.get(idx) <= 1) {
                break;
            }
            int l = left[idx], r = right[idx];
            long take = Math.min((long)(r - idx) * (idx - l), k);
            ans = ans * fastPow(nums.get(idx), take) % MOD;
            k -= (int)take;
            if (k <= 0) {
                break;
            }
        }
        return (int) ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Integer> nums = jsonArrayToIntList(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maximumScore(nums, k));
    }
}
