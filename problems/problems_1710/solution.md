# [Python] 贪心

> Author: Benhao
> Date: 2022-11-15
> Upvotes: 1
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1710. 卡车上的最大单元数](https://leetcode.cn/problems/maximum-units-on-a-truck/description/)

[TOC]

# 思路
> 给定了不同的单元价值，显然取单元价值更高的更优

# 解题方法
> 将数组按单元价值排序，统计取尽或者卡车用尽所能达到的最大值即可

# 复杂度
- 时间复杂度: 
> $O(nlog_n)$

- 空间复杂度: 
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
