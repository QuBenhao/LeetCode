package problems.problems_1802;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private boolean check(int n, int index, int maxSum, long x) {
        long leftSum = 0, rightSum = 0;
        if (x > index) {
            leftSum = (x - 1 + x - index) * index / 2;
        } else {
            leftSum = (x - 1 + 1) * (x - 1) / 2 + (index - x + 1);
        }
        if (x > n - index - 1) {
            rightSum = (x - 1 + x - (n - index - 1)) * (n - index - 1) / 2;
        } else {
            rightSum = (x - 1 + 1) * (x - 1) / 2 + (n - index - 1 - x + 1);
        }
        return leftSum + rightSum <= maxSum - x;
    }

    public int maxValue(int n, int index, int maxSum) {
        int left = 1, right = maxSum - n + 1;
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (check(n, index, maxSum, mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int index = Integer.parseInt(inputJsonValues[1]);
		int maxSum = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxValue(n, index, maxSum));
    }
}
