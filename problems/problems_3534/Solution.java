package problems.problems_3534;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        Integer[] idxes = new Integer[n];
        for (int i = 0; i < n; ++i) {
            idxes[i] = i;
        }
        Arrays.sort(idxes, Comparator.comparingInt(a -> nums[a]));
        int[] mapping = new int[n];
        for (int i = 0; i < n; ++i) {
            mapping[idxes[i]] = i;
        }

        int m = 32 - Integer.numberOfLeadingZeros(n);
        int[][] pa = new int[n][m];
        int left = 0;
        for (int i = 0; i < n; ++i) {
            while (nums[idxes[i]] - nums[idxes[left]] > maxDiff) {
                ++left;
            }
            pa[i][0] = left;
        }
        for (int j = 1; j < m; ++j) {
            for (int i = 0; i < n; ++i) {
                pa[i][j] = pa[pa[i][j - 1]][j - 1];
            }
        }

        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; ++i) {
            int l = mapping[queries[i][0]];
            int r = mapping[queries[i][1]];
            if (l == r) {
                ans[i] = 0;
                continue;
            }
            if (l > r) {
                int tmp = l;
                l = r;
                r = tmp;
            }
            int res = 0;
            for (int k = m-1; k >= 0; --k) {
                if (pa[r][k] > l) {
                    res |= (1 << k);
                    r = pa[r][k];
                }
            }
            ans[i] = pa[r][0] > l ? -1 : res + 1;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[] nums = jsonArrayToIntArray(inputJsonValues[1]);
		int maxDiff = Integer.parseInt(inputJsonValues[2]);
		int[][] queries = jsonArrayToInt2DArray(inputJsonValues[3]);
        return JSON.toJSON(pathExistenceQueries(n, nums, maxDiff, queries));
    }
}
