# [Python/Go] 动态规划

> Author: Benhao
> Date: 2022-02-13
> Upvotes: 3
> Tags: Go, Python, Python3

---

### 解题思路
维护一个之前的`values[i] + i`的最大值，之后用`values[j] - j`的和的最大值找最大的答案即可

### 代码

```Python3 []
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp, ans = -inf, 0
        for i, v in enumerate(values):
            ans = max(ans, dp + v - i)
            dp = max(dp, v + i)
        return ans
```
```Go []
func maxScoreSightseeingPair(values []int) (ans int) {
    dp := -0x3f3f3f
    for i, v := range values {
        ans = max(ans, dp + v - i)
        dp = max(dp, v + i)
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```
另一个写法
```Python3 []
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = left = 0
        for i, val in enumerate(values):
            ans = max(ans, left + val - i)
            left = max(left, val + i)
        return ans
```