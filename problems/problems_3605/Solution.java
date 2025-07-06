package problems.problems_3605;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    private boolean check(int[] nums, int maxC, List<List<int[]>> gs, int k) {
        int count = 0;
        if (k == 0) {
            for (int num: nums) {
                if (num != 1) {
                    if (++count > maxC) {
                        return false;
                    }
                }
            }
        } else {
            for (int i = gs.size() - 1; i >= 0; ) {
                List<int[]> g = gs.get(i);
                boolean found = false;
                for (int j = g.size() - 1; j >= 0; --j) {
                    int[] p = g.get(j);
                    if (p[0] != 1 && i - p[1] + 1 > k) {
                        if (++count > maxC) {
                            return false;
                        }
                        found = true;
                        i = Math.max(i - k, p[1]) - 1;
                        break;
                    }
                }
                if (!found) {
                    --i;
                }
            }
        }
        return true;
    }

    public int minStable(int[] nums, int maxC) {
        int n = nums.length;
        List<List<int[]>> gs = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            List<int[]> g;
            if (i == 0) {
                g = new ArrayList<>();
            } else {
                g = new ArrayList<>(gs.get(i - 1).size());
                for (int[] p : gs.get(i - 1)) {
                    g.add(new int[]{p[0], p[1]});
                }
            }
            g.add(new int[]{nums[i], i});
            int j = 0;
            for (int[] p: g) {
                p[0] = gcd(p[0], nums[i]);
                if (g.get(j)[0] != p[0]) {
                    j++;
                    g.set(j, p);
                }
            }
            g = g.subList(0, j + 1);
            gs.add(g);
        }

        int left = 0, right = n;
        while (left < right) {
            int mid = (left + right) / 2;
            if (check(nums, maxC, gs, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int maxC = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minStable(nums, maxC));
    }
}
