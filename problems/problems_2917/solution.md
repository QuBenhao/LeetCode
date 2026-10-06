# [Python] Bitwise simulation

> slug: python-wei-yun-suan-mo-ni-by-himymben-khp9
> date: 2024-03-06
> tags: C, Go, Java, Python3, TypeScript
> question: Find the K-or of an Array (find-the-k-or-of-an-array)
> url: https://leetcode.cn/problems/find-the-k-or-of-an-array/solutions/3fFpP7/python-wei-yun-suan-mo-ni-by-himymben-khp9/

---

> Problem: [2917. 找出数组中的 K-or 值](https://leetcode.cn/problems/find-the-k-or-of-an-array/description/)

[TOC]

# Intuition

> For each bit from 0 through 30, scan the array and count how many values have that bit set.

# Approach

> Bitwise simulation

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
  
