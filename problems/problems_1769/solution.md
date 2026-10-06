# The light has gone out, but we are still fighting

> Author: Benhao
> Date: 2022-12-02
> Upvotes: 43
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1769. 移动所有球到每个盒子所需的最小操作数](https://leetcode.cn/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/)

[TOC]

# Intuition
> Method 1: record the positions of all balls.
> Method 2: accumulate distances by position. Derive the left and right distance sums from the neighboring boxes' corresponding sums.

# Approach
> Method 1: brute-force counting
> Method 2: optimize with prefix sums

# Complexity
Method 1:
- Time complexity:
> $O(m * n)$

- Space complexity:
> $O(n)$

Method 2:
- Time complexity:
> $O(n)$

- Space complexity:
> $O(n)$

# Code
```Python3

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        return [sum(abs(j - i) for j in idxes) for i in range(len(boxes))] if (idxes := [i for i, c in enumerate(boxes) if c == '1']) else [0] * len(boxes)

```
```Python3
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left, right = [0] * n, [0] * n
        cur = 0
        for i, c in enumerate(boxes):
            left[i], cur = left[i - 1] + cur, cur + (c == '1')
        cur = int(boxes[-1] == '1')
        for i in range(n - 2, -1, -1):
            right[i], cur = right[i + 1] + cur, cur + (boxes[i] == '1')
        return [left[i] + right[i] for i in range(n)]  
```
