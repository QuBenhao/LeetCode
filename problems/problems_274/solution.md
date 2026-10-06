# [Python/Go/C] Counting

> Author: Benhao
> Date: 2024-02-25
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [274. H 指数](https://leetcode.cn/problems/h-index/description/)

[TOC]

# Intuition

> Sorting is straightforward but offers little insight. Binary search on the answer is also possible because the condition is monotonic. A better option is the O(n) method learned from 三叶: count frequencies, then traverse from large to small, accumulating counts as with prefix sums. The first value satisfying the condition is the answer.

# Approach

> Count, then traverse to find the answer

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
