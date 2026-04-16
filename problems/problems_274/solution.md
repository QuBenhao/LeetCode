# [Python/Go/C] 计数

> Author: Benhao
> Date: 2024-02-25
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [274. H 指数](https://leetcode.cn/problems/h-index/description/)

[TOC]

# 思路

> 排序固然简单，但没有价值。二分答案也是一个选择（毕竟答案具备二分性质），不过更好的是从三叶那学习O(n)的方法，统计计数后从大到小遍历（类似前缀和），找到第一个满足条件的即为答案

# 解题方法

> 统计后遍历找答案

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnts = [0] * (n + 1)
        for c in citations:
            cnts[min(c, n)] += 1
        total = 0
        for i in range(n, 0, -1):
            total += cnts[i]
            if total >= i:
                return i
        return 0
```
```Go []
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
func hIndex(citations []int) int {
    n := len(citations)
    cnts := make([]int, n + 1)
    for _, c := range citations {
        cnts[min(c, n)]++
    }
    for i, total := n, 0; i > 0; i-- {
        total += cnts[i]
        if total >= i {
            return i
        }
    }
    return 0
}
```
```C []
#define MIN(a, b) ((a) < (b) ? (a) : (b))
int hIndex(int* citations, int citationsSize) {
    int *cnts = malloc(sizeof(int) * (citationsSize + 1));
    memset(cnts, 0, sizeof(int) * (citationsSize + 1));
    for (int i = 0; i < citationsSize; i++) {
        cnts[MIN(citations[i], citationsSize)]++;
    }
    for (int i = citationsSize, total = 0; i > 0; i--) {
        total += cnts[i];
        if (total >= i) {
            return i;
        }
    }
    return 0;
}
```
