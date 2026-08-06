# [Python] 位运算模拟

> slug: python-wei-yun-suan-mo-ni-by-himymben-khp9
> date: 2024-03-06
> tags: C, Go, Java, Python3, TypeScript
> question: Find the K-or of an Array (find-the-k-or-of-an-array)
> url: https://leetcode.cn/problems/find-the-k-or-of-an-array/solutions/3fFpP7/python-wei-yun-suan-mo-ni-by-himymben-khp9/

---

> Problem: [2917. 找出数组中的 K-or 值](https://leetcode.cn/problems/find-the-k-or-of-an-array/description/)

[TOC]

# 思路

> 遍历二进制的0-30位，遍历数组，统计每一位是1的个数

# 解题方法

> 位运算模拟

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(31):
            cnt = 0
            for num in nums:
                if (num >> i) & 1 == 1:
                    cnt += 1
            if cnt >= k:
                ans |= 1 << i
        return ans
```
  
