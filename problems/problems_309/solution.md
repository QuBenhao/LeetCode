# [Python/Go] 动态规划

> Author: Benhao
> Date: 2022-02-14
> Upvotes: 15
> Tags: Go, Python, Python3

---

### 解题思路
分别维护 买入、卖出、冷冻期 的最大值，答案由最终卖出和冷冻期的最大值组成

### 代码

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