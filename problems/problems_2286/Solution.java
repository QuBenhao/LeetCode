package problems.problems_2286;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class BookMyShow {
    private final int n;
    private final int m;
    private final int[] min;
    private final long[] sum;

    public BookMyShow(int n, int m) {
        this.n = n;
        this.m = m;
        int size = 2 << (32 - Integer.numberOfLeadingZeros(n)); // Smaller than 4n
        min = new int[size];
        sum = new long[size];
    }

    public int[] gather(int k, int maxRow) {
        // Find the first bucket that can hold k more liters of water
        int r = findFirst(1, 0, n - 1, maxRow, m - k);
        if (r < 0) { // No such bucket exists
            return new int[]{};
        }
        int c = (int) querySum(1, 0, n - 1, r, r);
        update(1, 0, n - 1, r, k); // Pour water
        return new int[]{r, c};
    }

    public boolean scatter(int k, int maxRow) {
        // Total amount of water in [0,maxRow]
        long s = querySum(1, 0, n - 1, 0, maxRow);
        if (s > (long) m * (maxRow + 1) - k) {
            return false; // The buckets already contain too much water
        }
        // Start with the first bucket that is not full
        int i = findFirst(1, 0, n - 1, maxRow, m - 1);
        while (k > 0) {
            int left = Math.min(m - (int) querySum(1, 0, n - 1, i, i), k);
            update(1, 0, n - 1, i, left); // Pour water
            k -= left;
            i++;
        }
        return true;
    }

    // Increase the element at index i by val
    private void update(int o, int l, int r, int i, int val) {
        if (l == r) {
            min[o] += val;
            sum[o] += val;
            return;
        }
        int m = (l + r) / 2;
        if (i <= m) {
            update(o * 2, l, m, i, val);
        } else {
            update(o * 2 + 1, m + 1, r, i, val);
        }
        min[o] = Math.min(min[o * 2], min[o * 2 + 1]);
        sum[o] = sum[o * 2] + sum[o * 2 + 1];
    }

    // Return the sum of elements in [L,R]
    private long querySum(int o, int l, int r, int L, int R) {
        if (L <= l && r <= R) {
            return sum[o];
        }
        long res = 0;
        int m = (l + r) / 2;
        if (L <= m) {
            res = querySum(o * 2, l, m, L, R);
        }
        if (R > m) {
            res += querySum(o * 2 + 1, m + 1, r, L, R);
        }
        return res;
    }

    // Return the leftmost position in [0,R] whose value is <= val, or -1 if none exists
    private int findFirst(int o, int l, int r, int R, int val) {
        if (min[o] > val) {
            return -1; // Every value in the interval exceeds val
        }
        if (l == r) {
            return l;
        }
        int m = (l + r) / 2;
        if (min[o * 2] <= val) {
            return findFirst(o * 2, l, m, R, val);
        }
        if (R > m) {
            return findFirst(o * 2 + 1, m + 1, r, R, val);
        }
        return -1;
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow obj = new BookMyShow(n, m);
 * int[] param_1 = obj.gather(k,maxRow);
 * boolean param_2 = obj.scatter(k,maxRow);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int n = Integer.parseInt(opValues[0][0]);
		int m = Integer.parseInt(opValues[0][1]);
		BookMyShow obj = new BookMyShow(n, m);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("gather") == 0) {
				int k = Integer.parseInt(opValues[i][0]);
				int maxRow = Integer.parseInt(opValues[i][1]);
				ans.add(obj.gather(k, maxRow));
				continue;
			}
			if (operators[i].compareTo("scatter") == 0) {
				int k = Integer.parseInt(opValues[i][0]);
				int maxRow = Integer.parseInt(opValues[i][1]);
				ans.add(obj.scatter(k, maxRow));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
