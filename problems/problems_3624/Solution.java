package problems.problems_3624;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private class FenwickTree {
        private final int[] tree;
        private final int n;

        public  FenwickTree(int n) {
            this.n = n;
            this.tree = new int[n + 1];
        }

        private int lowbit(int x) {
            return x & -x;
        }

        public void update(int index, int value) {
            for (; index <= n; index += lowbit(index)) {
                tree[index] += value;
            }
        }

        public int query(int index) {
            int sum = 0;
            for (; index > 0; index -= lowbit(index)) {
                sum += tree[index];
            }
            return sum;
        }

        public int query(int left, int right) {
            return query(right) - query(left - 1);
        }
    }

    private int popcount(long num) {
        int count = 0;
        while (num > 1) {
            ++count;
            num = Long.bitCount(num);
        }
        return count;
    }

    public int[] popcountDepth(long[] nums, long[][] queries) {
        int n = nums.length;
        FenwickTree[] trees = new FenwickTree[6];
        for (int i = 0; i < 6; ++i) {
            trees[i] = new FenwickTree(n);
        }
        for (int i = 0; i < n; ++i) {
            int depth = popcount(nums[i]);
            trees[depth].update(i + 1, 1);
        }
        List<Integer> results = new ArrayList<>();
        for (long[] query: queries) {
            if (query[0] == 1) {
                int l = (int) query[1], r = (int) query[2], k = (int) query[3];
                results.add(trees[k].query(l + 1, r + 1));
            } else {
                int idx = (int) query[1];
                long newValue = query[2];
                int oldDepth = popcount(nums[idx]);
                int newDepth = popcount(newValue);
                nums[idx] = newValue;
                if (oldDepth != newDepth) {
                    trees[oldDepth].update(idx + 1, -1);
                    trees[newDepth].update(idx + 1, 1);
                }
            }
        }
        return results.stream().mapToInt(Integer::intValue).toArray();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long[] nums = jsonArrayToLongArray(inputJsonValues[0]);
		long[][] queries = jsonArrayToLong2DArray(inputJsonValues[1]);
        return JSON.toJSON(popcountDepth(nums, queries));
    }
}
