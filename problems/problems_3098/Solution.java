package problems.problems_3098;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    static final int MOD = 1000000007, INF = 0x3f3f3f3f;

    public int sumOfPowers(int[] nums, int k) {
        int n = nums.length;
        Arrays.sort(nums);
        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                set.add(nums[i] - nums[j]);
            }
        }
        set.add(INF);
        List<Integer> vals = new ArrayList<Integer>(set);
        Collections.sort(vals);

        int[][][] d = new int[n][k + 1][vals.size()];
        int[][] border = new int[n][k + 1];
        int[][] sum = new int[k + 1][vals.size()];
        int[][] suf = new int[n][k + 1];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int pos = binarySearch(vals, nums[i] - nums[j]);
                for (int p = 1; p <= k; p++) {
                    while (border[j][p] < pos) {
                        sum[p][border[j][p]] = (sum[p][border[j][p]] - suf[j][p] + MOD) % MOD;
                        sum[p][border[j][p]] = (sum[p][border[j][p]] + d[j][p][border[j][p]]) % MOD;
                        suf[j][p] = (suf[j][p] - d[j][p][border[j][p]] + MOD) % MOD;
                        border[j][p]++;
                        sum[p][border[j][p]] = (sum[p][border[j][p]] + suf[j][p]);
                    }
                }
            }

            d[i][1][vals.size() - 1] = 1;
            for (int p = 2; p <= k; p++) {
                for (int v = 0; v < vals.size(); v++) {
                    d[i][p][v] = sum[p - 1][v];
                }
            }
            for (int p = 1; p <= k; p++) {
                for (int v = 0; v < vals.size(); v++) {
                    suf[i][p] = (suf[i][p] + d[i][p][v]) % MOD;
                }
                sum[p][0] = (sum[p][0] + suf[i][p]) % MOD;
            }
        }

        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int v = 0; v < vals.size(); v++) {
                res = (int) ((res + 1L * vals.get(v) * d[i][k][v] % MOD) % MOD);
            }
        }
        return res;
    }

    public int binarySearch(List<Integer> vals, int target) {
        int low = 0, high = vals.size();
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (vals.get(mid) >= target) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(sumOfPowers(nums, k));
    }
}
