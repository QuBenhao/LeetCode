# [Python] Mathematics

> slug: python-shu-xue-by-himymben-8zmh
> date: 2024-03-08
> tags: C, Go, Java, Python3, TypeScript
> question: Find the Minimum Possible Sum of a Beautiful Array (find-the-minimum-possible-sum-of-a-beautiful-array)
> url: https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/solutions/VkdDge/python-shu-xue-by-himymben-8zmh/

---

> Problem: [2834. 找出美丽数组的最小和](https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/description/)

[TOC]

# Intuition

> The optimal choice is unique: take values from 1 through floor(target/2), then continue from target until n values have been taken.

# Approach

> Apply the summation formula twice.

# Complexity

Time complexity:
> $O(1)$

Space complexity:
> $O(1)$



# Code
```Python3 []
MOD = int(1e9) + 7
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        return ((1 + m) * m // 2 + (target + target + n - m - 1) * (n - m) // 2) % MOD if (m := min(n, target // 2)) >= 0 else 0
```
  
