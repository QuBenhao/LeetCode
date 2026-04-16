# [Python/Go/C] k分割翻转

> Author: Benhao
> Date: 2024-02-23
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [189. 轮转数组](https://leetcode.cn/problems/rotate-array/description/)

[TOC]

# 思路

> 后面的数要到前面，前面的数要到后面，可以用翻转。最终顺序再分别翻一次即可

# 解题方法

> [5,6,7,1,2,3,4] = [5,6,7] + [1,2,3,4] = [7,6,5] + [4,3,2,1] = [7,6,5,4,3,2,1] = [1,2,3,4,5,6,7]

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for i in range(n // 2):
            nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]
        for i in range(k // 2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]
        for i in range(k, (n + k) // 2):
            nums[i], nums[n - 1 + k - i] = nums[n - 1 + k - i], nums[i]
```
```Go []
```
```C []
```
