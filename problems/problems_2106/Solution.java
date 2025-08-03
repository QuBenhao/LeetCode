package problems.problems_2106;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxTotalFruits(int[][] fruits, int startPos, int k) {
        int n = fruits.length;
        int left = lowerBound(fruits, startPos - k); // 向左最远能到 fruits[left][0]

        int ans = 0;
        int s = 0;
        // 枚举最右走到 fruits[right][0]
        for (int right = left; right < n && fruits[right][0] <= startPos + k; right++) {
            s += fruits[right][1];
            while (fruits[right][0] * 2 - fruits[left][0] - startPos > k &&
                   fruits[right][0] - fruits[left][0] * 2 + startPos > k) {
                s -= fruits[left][1]; // fruits[left][0] 太远了
                left++;
            }
            ans = Math.max(ans, s); // 更新答案最大值
        }
        return ans;
    }

    // 见 https://www.bilibili.com/video/BV1AP41137w7/
    private int lowerBound(int[][] fruits, int target) {
        int left = -1;
        int right = fruits.length; // 开区间 (left, right)
        while (left + 1 < right) { // 开区间不为空
            // 循环不变量：
            // fruits[left][0] < target
            // fruits[right][0] >= target
            int mid = left + (right - left) / 2;
            if (fruits[mid][0] < target) {
                left = mid; // 范围缩小到 (mid, right)
            } else {
                right = mid; // 范围缩小到 (left, mid)
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
