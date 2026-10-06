# [Python/Go] Dynamic programming

> Author: Benhao
> Date: 2022-02-13
> Upvotes: 3
> Tags: Go, Python, Python3

---

### Approach
Maintain the maximum earlier `values[i] + i`, then maximize its sum with `values[j] - j` to obtain the answer.

### Code

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
Another implementation
```Python3 []
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = left = 0
        for i, val in enumerate(values):
            ans = max(ans, left + val - i)
            left = max(left, val + i)
        return ans
```
