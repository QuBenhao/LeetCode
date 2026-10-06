# [Python] Memoized search

> slug: python-ji-yi-hua-sou-suo-by-himymben-kdxj
> date: 2024-03-01
> tags: C, Go, Java, Python3, TypeScript
> question: Check if There is a Valid Partition For The Array (check-if-there-is-a-valid-partition-for-the-array)
> url: https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/solutions/ju9xdK/python-ji-yi-hua-sou-suo-by-himymben-kdxj/

---

> Problem: [2369. 检查数组是否存在有效划分](https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/description/)

[TOC]

# Intuition

> At each step, check whether a group of two or three elements can be taken, and cache the result.

# Approach

> Memoized search

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return True
            if n - i < 2:
                return False
            if n - i >= 3:
                if (nums[i] == nums[i + 1] and nums[i] == nums[i + 2]) or (nums[i] == nums[i + 1] - 1 and nums[i] == nums[i + 2] - 2):
                    if dfs(i + 3):
                        return True
            return nums[i] == nums[i + 1] and dfs(i + 2)
        
        return dfs(0)
```
  
