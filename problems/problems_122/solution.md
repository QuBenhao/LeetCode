# [Python/Go/C] Dynamic programming

> Author: Benhao
> Date: 2024-02-24
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/)

[TOC]

# Intuition

> Maintain the maximum profit while holding stock and the maximum profit after selling.

# Approach

> The current maximum profit while holding stock is the greater of the previous maximum holding profit and the previous maximum selling profit minus the current purchase price.
The current maximum profit after selling is the greater of the previous maximum selling profit and the previous maximum holding profit plus the current sale price.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sell = -prices[0], 0
        for p in prices:
            hold, sell = max(hold, sell - p), max(sell, hold + p)
        return sell
```
```Go []
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
func maxProfit(prices []int) (sell int) {
    hold := -prices[0]
    for _, p := range prices {
        hold, sell = max(hold, sell - p), max(sell, hold + p)
    }
    return
}
```
```C []
#define MAX(a, b) ((a) < (b) ? (b) : (a))
int maxProfit(int* prices, int pricesSize) {
    int hold = -prices[0], sell = 0;
    for (int i = 0; i < pricesSize; i++) {
        int tmp = hold;
        hold = MAX(hold, sell - prices[i]);
        sell = MAX(sell, tmp + prices[i]);
    }
    return sell;
}
```
  
