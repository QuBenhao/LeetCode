# [Python/Go] 动态规划

> Author: Benhao
> Date: 2022-02-14
> Upvotes: 1
> Tags: Go, Python, Python3

---

### 解题思路
分别维护 买入、卖出 的最大值
卖出在更新时加入交易费用即可

### 代码

```Python3 []
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = -prices[0], 0
        for p in prices:
            buy, sell = max(buy, sell - p), max(sell, buy + p - fee)
        return sell
```
```Go []
func maxProfit(prices []int, fee int) int {
    buy, sell := -prices[0], 0
    for _, p := range prices {
        buy, sell = max(buy, sell - p), max(sell, buy + p - fee)
    }
    return sell
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```