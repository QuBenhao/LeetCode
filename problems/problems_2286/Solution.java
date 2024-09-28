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
        int size = 2 << (32 - Integer.numberOfLeadingZeros(n)); // 比 4n 更小
        min = new int[size];
        sum = new long[size];
    }

    public int[] gather(int k, int maxRow) {
        // 找第一个能倒入 k 升水的水桶
        int r = findFirst(1, 0, n - 1, maxRow, m - k);
        if (r < 0) { // 没有这样的水桶
            return new int[]{};
        }
        int c = (int) querySum(1, 0, n - 1, r, r);
        update(1, 0, n - 1, r, k); // 倒水
        return new int[]{r, c};
    }

    public boolean scatter(int k, int maxRow) {
        // [0,maxRow] 的接水量之和
        long s = querySum(1, 0, n - 1, 0, maxRow);
        if (s > (long) m * (maxRow + 1) - k) {
            return false; // 水桶已经装了太多的水
        }
        // 从第一个没有装满的水桶开始
        int i = findFirst(1, 0, n - 1, maxRow, m - 1);
        while (k > 0) {
            int left = Math.min(m - (int) querySum(1, 0, n - 1, i, i), k);
            update(1, 0, n - 1, i, left); // 倒水
            k -= left;
            i++;
        }
        return true;
    }

    // 把下标 i 上的元素值增加 val
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

    // 返回区间 [L,R] 内的元素和
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

    // 返回区间 [0,R] 中 <= val 的最靠左的位置，不存在时返回 -1
    private int findFirst(int o, int l, int r, int R, int val) {
        if (min[o] > val) {
            return -1; // 整个区间的元素值都大于 val
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
