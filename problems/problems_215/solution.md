# [Python] heapq优先队列

> Author: Benhao
> Date: 2024-03-03
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/description/)

[TOC]

# 思路

> 堆排序

# 解题方法

> 取出第k大即可

# 复杂度

时间复杂度:
> $O(nlog_k)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, -num)
        for i in range(k - 1):
            heapq.heappop(pq)
        return -heapq.heappop(pq)
```
  
