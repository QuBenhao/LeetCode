# [Python/Go/C] 动态规划

> Author: Benhao
> Date: 2024-02-24
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/)

[TOC]

# 思路

> 维护当前最大的持股利润、以及当前最大的卖出利润

# 解题方法

> 当前最大的持股利润：上一个最大持股利润，和上一个最大的卖出利润减去当前买入价的最大值构成
当前最大的卖出利润：上一个最大卖出利润，和上一个最大的持股利润加上当前卖出价的最大值构成

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
