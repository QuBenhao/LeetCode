package problems.problems_2106;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxTotalFruits(int[][] fruits, int startPos, int k) {
        int n = fruits.length;
        int left = lowerBound(fruits, startPos - k); // The farthest reachable position to the left is fruits[left][0]

        int ans = 0;
        int s = 0;
        // Enumerate fruits[right][0] as the rightmost position visited
        for (int right = left; right < n && fruits[right][0] <= startPos + k; right++) {
            s += fruits[right][1];
            while (fruits[right][0] * 2 - fruits[left][0] - startPos > k &&
                   fruits[right][0] - fruits[left][0] * 2 + startPos > k) {
                s -= fruits[left][1]; // fruits[left][0] is too far away
                left++;
            }
            ans = Math.max(ans, s); // Update the maximum answer
        }
        return ans;
    }

    // See https://www.bilibili.com/video/BV1AP41137w7/
    private int lowerBound(int[][] fruits, int target) {
        int left = -1;
        int right = fruits.length; // Open interval (left, right)
        while (left + 1 < right) { // The open interval is nonempty
            // Loop invariant:
            // fruits[left][0] < target
            // fruits[right][0] >= target
            int mid = left + (right - left) / 2;
            if (fruits[mid][0] < target) {
                left = mid; // Shrink the range to (mid, right)
            } else {
                right = mid; // Shrink the range to (left, mid)
            }
        }
        return right;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] fruits = jsonArrayToInt2DArray(inputJsonValues[0]);
		int startPos = Integer.parseInt(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxTotalFruits(fruits, startPos, k));
    }
}
