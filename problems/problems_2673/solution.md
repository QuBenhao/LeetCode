# [Python/Go/C] 贪心

> slug: pythongoc-tan-xin-by-himymben-clbb
> date: 2024-02-28
> tags: C, Go, Java, Python3, TypeScript
> question: Make Costs of Paths Equal in a Binary Tree (make-costs-of-paths-equal-in-a-binary-tree)
> url: https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/solutions/CHxASJ/pythongoc-tan-xin-by-himymben-clbb/

---

> Problem: [2673. 使二叉树所有路径值相等的最小代价](https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/description/)

[TOC]

# 思路

> 能在上层消除的差异就不要在底层消除，因为底层需要加多个节点，肯定比在上层加操作大。既然要每个路径都一样，那么两两节点都需要一致。故从底层依次两两处理。

# 解题方法

> 每对儿兄弟节点需要保持一致，从底层往上层计算。同时累计和，计算上层差异、上层需要的操作数。

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range(n // 2, 0, -1):
            ans += abs(cost[i * 2] - cost[i * 2 - 1])
            cost[i - 1] += max(cost[i * 2], cost[i * 2 - 1])
        return ans
```
```Go []
func minIncrements(n int, cost []int) (ans int) {
    for i := n / 2; i > 0; i-- {
        if cost[i * 2] > cost[i * 2 - 1] {
            ans += cost[i * 2] - cost[i * 2 - 1]
            cost[i - 1] += cost[i * 2]
        } else {
            ans += cost[i * 2 - 1] - cost[i * 2]
            cost[i - 1] += cost[i * 2 - 1]
        }
    }
    return
}
```
```C []
#define MAX(a, b) ((a) < (b) ? (b) : (a))
#define ABS(a) ((a) < 0 ? -(a) : (a))
int minIncrements(int n, int* cost, int costSize){
    int ans = 0;
    for (int i = n / 2; i > 0; i--) {
        ans += ABS(cost[i * 2 - 1] - cost[i * 2]);
        cost[i - 1] += MAX(cost[i * 2 - 1], cost[i * 2]);
    }
    return ans;
}
```