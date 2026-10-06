# [Python/Go/C] Greedy

> slug: pythongoc-tan-xin-by-himymben-clbb
> date: 2024-02-28
> tags: C, Go, Java, Python3, TypeScript
> question: Make Costs of Paths Equal in a Binary Tree (make-costs-of-paths-equal-in-a-binary-tree)
> url: https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/solutions/CHxASJ/pythongoc-tan-xin-by-himymben-clbb/

---

> Problem: [2673. 使二叉树所有路径值相等的最小代价](https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/description/)

[TOC]

# Intuition

> Resolve a difference at a higher level when possible, since doing so lower down requires increments to multiple nodes and therefore more operations. Equal path sums require sibling subtrees to match, so process sibling pairs from the bottom up.

# Approach

> Equalize each sibling pair from the bottom up, accumulating path sums to compute differences and required operations at higher levels.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
