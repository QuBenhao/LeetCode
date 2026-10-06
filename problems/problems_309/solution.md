# [Python/Go] Dynamic programming

> Author: Benhao
> Date: 2022-02-14
> Upvotes: 15
> Tags: Go, Python, Python3

---

### Approach
Maintain the maximum values for buying, selling, and cooldown separately. The answer is the maximum of the final selling and cooldown states.

### Code

```Python3 []
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, cd = -prices[0], 0, 0
        for p in prices:
            buy, sell, cd = max(buy, cd - p), max(sell, buy + p), max(sell, cd)
        return max(sell, cd)
```
```Go []
func maxProfit(prices []int) int {
    buy, sell, cd := -prices[0], 0, 0
    for _, p := range prices {
        buy, sell, cd = max(buy, cd - p), max(sell, buy + p), max(sell, cd)
    }
    return max(sell, cd)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```
