# [Python/Go/C] Dynamic programming

> Author: Benhao
> Date: 2024-02-24
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/)

[TOC]

# Intuition

> The maximum profit from selling now is the difference between the current price and the smallest previous price. Maintain the minimum price while traversing, and compare each difference with the answer to find the maximum.

# Approach

> Traversal and dynamic programming

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, mn = 0, inf
        for p in prices:
            ans = max(ans, p - mn)
            mn = min(mn, p)
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
    if a < b {
        return a
    }
    return b
}

func maxProfit(prices []int) (ans int) {
    mn := 10001
    for _, p := range prices {
        ans = max(ans, p - mn)
        mn = min(mn, p)
    }
    return
}
```
```C []
#define MAX(a, b) ((a) < (b) ? (b) : (a))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
int maxProfit(int* prices, int pricesSize) {
    int ans = 0;
    for (int i = 0, mn = 10001; i < pricesSize; i++) {
        ans = MAX(ans, prices[i] - mn);
        mn = MIN(mn, prices[i]);
    }
    return ans;
}
```
  
