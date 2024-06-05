package problems.problems_3072;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
class Fenwick {
    private final int[] tree;

    public Fenwick(int n) {
        tree = new int[n];
    }

    // 把下标为 i 的元素增加 v
    public void add(int i, int v) {
        while (i < tree.length) {
            tree[i] += v;
            i += i & -i;
        }
    }

    // 返回下标在 [1,i] 的元素之和
    public int pre(int i) {
        int res = 0;
        while (i > 0) {
            res += tree[i];
            i &= i - 1;
        }
        return res;
    }
}


public class Solution extends BaseSolution {
    public int[] resultArray(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted); // 只排序不去重
        int n = nums.length;

        List<Integer> a = new ArrayList<>(n); // 预分配空间
        List<Integer> b = new ArrayList<>();
        a.add(nums[0]);
        b.add(nums[1]);

        Fenwick t = new Fenwick(n + 1);
        t.add(n - Arrays.binarySearch(sorted, nums[0]), 1);
        t.add(n - Arrays.binarySearch(sorted, nums[1]), -1);

        for (int i = 2; i < nums.length; i++) {
            int x = nums[i];
            int v = n - Arrays.binarySearch(sorted, x);
            int d = t.pre(v - 1); // 转换成 < v 的元素个数之差
            if (d > 0 || d == 0 && a.size() <= b.size()) {
                a.add(x);
                t.add(v, 1);
            } else {
                b.add(x);
                t.add(v, -1);
            }
        }
        a.addAll(b);
        for (int i = 0; i < n; i++) {
            nums[i] = a.get(i);
        }
        return nums;
    }


    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(resultArray(nums));
    }
}
