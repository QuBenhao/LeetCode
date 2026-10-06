# [Python] Greedy

> Author: Benhao
> Date: 2022-11-15
> Upvotes: 1
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1710. 卡车上的最大单元数](https://leetcode.cn/problems/maximum-units-on-a-truck/description/)

[TOC]

# Intuition
> With different unit counts per box, taking boxes with more units is better.

# Approach
> Sort by units per box and count the maximum units until the boxes or truck capacity run out.

# Complexity
- Time complexity:
> $O(nlog_n)$

- Space complexity:
> $O(n)$

# Code
```Python3 []

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = i = 0
        boxTypes.sort(key=lambda x:(-x[1], -x[0]))
        while i < len(boxTypes) and truckSize:
            cur = min(truckSize, boxTypes[i][0])
            ans += cur * boxTypes[i][1]
            truckSize -= cur
            i += 1
        return ans

```
