# [Python/Go] Dynamic programming

> Author: Benhao
> Date: 2022-02-14
> Upvotes: 1
> Tags: Go, Python, Python3

---

### Approach
Maintain the maximum values for the bought and sold states separately.
Account for the transaction fee when updating the sold state.

### Code

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
