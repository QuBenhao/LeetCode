# [Python/Go/C] 天际线 or 单调栈

> Author: Benhao
> Date: 2024-02-26
> Upvotes: 3
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/description/)

[TOC]

# 思路

> 每一个位置能接到的水是它左右两边最高的柱子的较小的一个，故分别计算每个位置的左右最高柱子（类似前缀和+后缀和）

# 解题方法

> 从左至右扫描得到每个点左边的最高柱子，再从右至左扫描得到每个点右边的最高柱子，依次计算每个点能接到的雨水

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0] * n, [0] * (n + 1)
        for i, h in enumerate(height):
            left[i] = max(left[i - 1], h)
        ans = 0
        for i in range(n - 1, -1, -1):
            right[i] = max(right[i + 1], height[i])
            ans += min(left[i], right[i]) - height[i]
        return ans
```
```Go []
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
func min(a, b int) int {
    if a > b {
        return b
    }
    return a
} 
func trap(height []int) (ans int) {
    n := len(height)
    left := make([]int, n + 1)
    left[0] = 0
    for i, h := range height {
        left[i + 1] = max(left[i], h)
    }
    for i, r := n - 1, 0; i >= 0; i-- {
        r = max(r, height[i])
        ans += min(left[i + 1], r) - height[i]
    }
    return 
}
```
```C []
#define MAX(a, b) ((a) < (b) ? (b) : (a))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
int trap(int* height, int heightSize) {
    int *left = malloc(sizeof(int) * heightSize);
    left[0] = height[0];
    for (int i = 1; i < heightSize; i++) {
        left[i] = MAX(left[i - 1], height[i]);
    }
    int ans = 0;
    for (int i = heightSize - 1, r = 0; i >= 0; i--) {
        r = MAX(r, height[i]);
        ans += MIN(left[i], r) - height[i];
    }
    return ans;
}
```

单调栈解法
```Python3 []
class Solution:
    def trap(self, height: List[int]) -> int:
        stack, ans = [], 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                idx = stack.pop()
                # 左边没有比自身高的柱子了
                if not stack:
                    continue
                # 高度为左右两边最小的减去自身的高度
                he = min(height[stack[-1]], h) - height[idx]
                # 宽度为左右两边的中间距离
                wi = i - stack[-1] - 1
                ans += he * wi
            stack.append(i)
        return ans
```
```Go []
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
func trap(height []int) (ans int) {
    st := make([]int, 0)
    for i := 0; i < len(height); i++ {
        for len(st) > 0 && height[i] > height[st[len(st) - 1]] {
            idx := st[len(st) - 1]
            st = st[:len(st) - 1]
            if len(st) == 0 {
                continue
            }
            left := st[len(st) - 1]
            h := min(height[left], height[i]) - height[idx]
            d := i - left - 1
            ans += h * d
        }
        st = append(st, i)
    }
    return
}
```
  
