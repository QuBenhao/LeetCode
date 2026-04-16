# [Python/Go/C] 动态规划

> Author: Benhao
> Date: 2024-02-24
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/)

[TOC]

# 思路

> 当前卖出股票的最大收益由之前的最小值和自身构成，遍历的同时维护目前最小值，与答案比较得到最大的差即可

# 解题方法

> 遍历，动态规划

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
