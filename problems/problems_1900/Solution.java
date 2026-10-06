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
            // Compute the smallest k satisfying first+second > ceil(n / 2^(k+1)); see the solution for the derivation
            int k = 32 - Integer.numberOfLeadingZeros((n - 1) / (first + second - 1)) - 1;
            n = ((n - 1) >> k) + 1; // n = ceil(n / 2^k)
            res += k;

            if (second - first > 1) {
                return res + 1;
            }
        }

        // Combine cases 1 and 3; include case 2 in the final return
        if (second - first == 1 || second > (n + 1) / 2 && second - first == 2) {
            // First replace n with ceil(n/2), then count how many ceil(n/2) operations make n even; see the solution for the derivation
            // Combine (n+1)/2 and n-1 to get (n+1)/2-1 = (n-1)/2
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
