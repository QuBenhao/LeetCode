package problems.problems_1900;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] earliestAndLatest(int n, int first, int second) {
        if (first + second == n + 1) {
            return new int[]{1, 1};
        }

        if (first + second > n + 1) {
            int tmp = first;
            first = n + 1 - second;
            second = n + 1 - tmp;
        }

        int earliest = calcEarliestRounds(n, first, second);
        int latest = Math.min(32 - Integer.numberOfLeadingZeros(n - 1), n + 1 - second);
        return new int[]{earliest, latest};
    }

    private int calcEarliestRounds(int n, int first, int second) {
        int res = 1;

        if (first + second <= (n + 1) / 2) {
            // 计算满足 first+second > ceil(n / 2^(k+1)) 的最小 k，推导过程见题解
            int k = 32 - Integer.numberOfLeadingZeros((n - 1) / (first + second - 1)) - 1;
            n = ((n - 1) >> k) + 1; // n = ceil(n / 2^k)
            res += k;

            if (second - first > 1) {
                return res + 1;
            }
        }

        // 情况 1 和情况 3 合并，情况 2 合并到最后的 return
        if (second - first == 1 || second > (n + 1) / 2 && second - first == 2) {
            // 先把 n 变成 ceil(n/2)，然后计算需要多少次 ceil(n/2) 的操作才能把 n 变成偶数，推导过程见题解
            // 这里把 (n+1)/2 和 n-1 合并，得到 (n+1)/2-1 = (n-1)/2
            return res + 1 + Integer.numberOfTrailingZeros((n - 1) / 2);
        }

        if (second > (n + 1) / 2 && first % 2 == 0 && first + second == n) {
            res++;
        }

        return res + 1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int firstPlayer = Integer.parseInt(inputJsonValues[1]);
		int secondPlayer = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(earliestAndLatest(n, firstPlayer, secondPlayer));
    }
}
