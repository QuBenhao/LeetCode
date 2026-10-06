# [Python/Go/C] Skyline or monotonic stack

> Author: Benhao
> Date: 2024-02-26
> Upvotes: 3
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/description/)

[TOC]

# Intuition

> The water each position can hold is determined by the smaller of the tallest bars on its left and right. Compute those two maximum heights for every position, similarly to prefix and suffix sums.

# Approach

> Scan from left to right to find the tallest bar to the left of each position, then scan from right to left for the tallest bar to its right. Calculate the trapped water at each position.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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

Monotonic stack approach
```Python3 []
class Solution:
    def trap(self, height: List[int]) -> int:
        stack, ans = [], 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                idx = stack.pop()
                # No taller bar remains on the left
                if not stack:
                    continue
                # Height is the smaller of the two boundary heights minus the current height
                he = min(height[stack[-1]], h) - height[idx]
                # Width is the gap between the left and right boundaries
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
  
