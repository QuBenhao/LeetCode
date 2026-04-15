# 双指针模拟

> Author: Benhao
> Date: 2022-12-17
> Upvotes: 7
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1764. 通过连接另一个数组的子数组得到一个数组](https://leetcode.cn/problems/form-array-by-concatenating-subarrays-of-another-array/description/)

[TOC]

# 思路
> 依次遍历group，只要能与nums的连续一段匹配，就直接匹配即可

# 解题方法
> 使用双指针和py的切片

# Code
```Python3 []

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = idx = 0
        while i < len(groups) and idx < len(nums):
            if nums[idx:idx + len(groups[i])] == groups[i]:
                idx += len(groups[i])
                i += 1
            else:
                idx += 1
        return i == len(groups)

```
