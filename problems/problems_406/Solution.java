package problems.problems_406;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    class FenwickTree {
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

    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            }
            return a[0] - b[0];
        });
        int n = people.length;
        FenwickTree fenwick = new FenwickTree(n);
        int[][] result = new int[n][2];
        for (int[] person : people) {
            int l = 1, r = n;
            while (l < r) {
                int mid = (l + r) / 2;
                if (fenwick.query(mid) >= mid - person[1]) {
                    l = mid + 1;
                } else {
                    r = mid;
                }
            }
            fenwick.update(l, 1);
            result[l - 1] = person;
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] people = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(reconstructQueue(people));
    }
}
